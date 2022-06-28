import os
import wget
import time
import json
import re
from process import macro_diff_same

# the remote configs
KERNEL_BASE_URL = 'https://mirrors.edge.kernel.org/pub/linux/kernel/'
MAIN_DIRS = ['1.0', '1.1', '1.2', '1.3', '2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '3.0', '3.x', '4.x', '5.x', '6.x']

# base configs
MAIN_VERSION = 5
SUB_VERSION = 17
PATCH_VERSION = 6
MAIN_DIR = '5.x'
TMP_PATH = './tmp'
PATCH_MODE = 'FROM_CUR'  # if FROM_CUR is set, the patches from this patch on
# PATCH_MODE = 'FROM_BEG'  # if FROM_BEG is set, the patches from the first patch on

# some global defination
MAX_RANGE = 30
SPLIT_LINE = '******************************************************'
CONFIG_RE = re.compile('CONFIG_\w+')

print(SPLIT_LINE)


def print_config():
    print('current configurations:')
    print('MAIN_VERSION:%s' % (MAIN_VERSION))
    print('SUB_VERSION:%s' % (SUB_VERSION))
    print('PATCH_VERSION:%s' % (PATCH_VERSION))

    if MAIN_DIR not in MAIN_DIRS:
        print('%s is not legle.' % (MAIN_DIR))
        exit(-1)

    print('CURRENT MAIN DIR:%s' % (MAIN_DIR))
    print('PATCH_FOLDER:%s' % (TMP_PATH))
    print('PATCH_MODE:%s' % (PATCH_MODE))
    print('KERNEL_BASE_RUL:%s' % (PATCH_MODE))
    print(SPLIT_LINE)


# print the config file
print_config()

# the main version dir url
KERNEL_BASE_URL = KERNEL_BASE_URL + 'v' + MAIN_DIR + '/'



def concat_version(main, sub, patch, with_ext=True):
    if with_ext:
        return 'patch-{}.{}.{}.xz'.format(main, sub, patch)
    else:
        return 'patch-{}.{}.{}'.format(main, sub, patch)


def download_file(file_name, out_dir='./tmp/'):
    url = KERNEL_BASE_URL + file_name
    try:
        if not os.path.exists('./tmp/bak/'+file_name+'.bak'):
            print('downloading '+file_name+' from '+' '+url)
            res = os.system('wget  '+url+' -q -O ./tmp/'+file_name)
            if res == 0:
                print('download %s success' % (file_name))
                os.system('cp ./tmp/'+file_name+' ./tmp/bak/'+file_name+'.bak')
                os.system('unxz ./tmp/'+file_name)
                return 0
            else:
                # download failed, file does not exist
                print('detecting end')
                os.system('rm -f ' + './tmp/'+file_name)
                return res
        else:
            print('patch cache %s detected, fast copying...' % file_name)
            os.system('cp -f ./tmp/bak/'+file_name+'.bak'+' '+'./tmp/'+file_name)
            print('copying '+file_name+' success')
            os.system('unxz ./tmp/'+file_name)
            return 0
    except Exception as ec:
        # just can not find the file
        return False


# initialize
cur_main = MAIN_VERSION
cur_sub = SUB_VERSION
cur_patch = PATCH_VERSION

# make the tmp folder to store the patches
if not os.path.exists('./tmp'):
    os.mkdir('./tmp')
    os.mkdir('./tmp/bak')
else:
    os.system('rm -f ./tmp/patch*')

# download the current version patch
file_name = concat_version(cur_main, cur_sub, cur_patch)
base_patch = file_name
download_file(file_name)


if PATCH_MODE == 'FROM_CUR':
    patch_begin = cur_patch
elif PATCH_MODE == 'FROM_BEG':
    patch_begin = 0
else:
    print('unsupported PATCH_MODE:%s' % (PATCH_MODE))
    exit(-1)

patch_count = 0
# for every patch
print('detecting the patch versions...')
for p in range(patch_begin, patch_begin+MAX_RANGE):
    # download
    file_name = concat_version(cur_main, cur_sub, p)
    res = download_file(file_name)
    if res != 0:
        patch_count = p - cur_patch - 1
        break

print('detect the patches end: %d found' % (patch_count))
print(SPLIT_LINE)


'''
{
    patch_version:XXX,
    patch_files:["foo/bar/t.c",
                "a/b/c.txt",
    ],
    file_res:[
        {
            file_name:'',
            file_diff:[
                {
                    config_name:'',
                    cur_diff:''
                    before_diff:'',
                    if_updated:False,
                },
                {
                    config_name:'',
                    cur_diff:'',
                    before_diff:'',
                    if_updated:False,

                }
            ]
        },
        {
            file_name:'',
            file_diff:[
                {
                    config_name:'',
                    cur_diff:''
                    before_diff:'',
                    if_updated:False,
                },
                {
                    config_name:'',
                    cur_diff:'',
                    before_diff:'',
                    if_updated:False,

                }

            ]

        }

    ]

}
'''

# load the json file
# base_patch is the patch of current version
base_patch = concat_version(MAIN_VERSION, SUB_VERSION, PATCH_VERSION, with_ext=False)

# prepare the last_release version
os.system('rm -rf ./last_release && cp -r ./linux-5.17.6 ./last_release')

# for i in range(1, 2):
for i in range(1, patch_count+1):
    patch_file = concat_version(cur_main, cur_sub, cur_patch+i, with_ext=False)
    # back to 5.17.0
    os.system('cd ./linux-5.17.6 && patch  -p1 -R >/dev/null <../tmp/'+base_patch)

    # make patch
    os.system('cd ./linux-5.17.6 && patch  -p1  <../tmp/'+patch_file + ' >../reports/'+patch_file+'.log')


    # make the patch file list
    with open('./reports/'+patch_file+'.log', 'r') as f:
        lines = f.readlines()
        patch_file_list = [line.split()[2] for line in lines]
        with open('./reports/'+patch_file+'.patch_file_list', 'w') as fw:
            json.dump(patch_file_list, fw, indent=2)
        # os.system('rm -f ./reports/'+patch_file+'.log')

    # get config variables list to config_var/patch_file.config_list
    os.system('cd ./linux-5.17.6 && make scriptconfig SCRIPT=Kconfiglib/examples/print_tree.py 2>/dev/null >../config_vars/'+patch_file+'.config_list')
    cur_config_set = set()
    with open('./config_vars/'+patch_file+'.config_list', 'r') as f_config:
        f_config_g = f_config.readlines()
        f_config_l = [x.strip() for x in f_config_g]
        cur_config_set.update(f_config_l)
        with open('./config_vars/'+patch_file+'.config_list', 'w') as f_config:
            json.dump(f_config_l, f_config, indent=2)


    # print(cur_config_set)
    # _ = input()
    res = {}
    concerned_vars = set()
    res['patch_version'] = patch_file
    res['patch_files'] = patch_file_list.copy()
    res['file_res'] = []
    # for each patch_file
    for s_line in patch_file_list:
        # print('./linux-5.17.6/'+s_line)
        if not os.system('diff ./linux-5.17.6/'+s_line + ' ' + './last_release/'+s_line + ' >/dev/null'):
            # nothing changed since last version
            continue

        single_file_res = {}
        single_file_res['path'] = s_line
        try:
            file_str = None
            with open('./linux-5.17.6/'+s_line, 'r') as s_f:
                file_str = s_f.read()
                s_f.close()
                # for fs in fg:
                #     print(fs)
        except Exception:
            # the file has been deleted
            file_str = ''

        search_res = re.findall(CONFIG_RE, file_str)
        # use the set to filter the unreal vars
        tmp_set = set(search_res)
        tmp_set = tmp_set & cur_config_set

        # update the elements to the big set
        concerned_vars = concerned_vars | tmp_set
        # print(search_res)
        # this file do have something to do with configure variables
        tmp_set_cpy = tmp_set.copy()
        if len(tmp_set) > 0:
            # make sure the macro_diff function get different result
            tmp_set = {x for x in tmp_set if not macro_diff_same('./linux-5.17.6/'+s_line, './last_release/'+s_line, x)}

            single_file_res['concerned_vars'] = list(tmp_set.copy())
            res['file_res'].append(single_file_res.copy())
        else:
            # the current file does not contain config vars
            continue

    res['global_concerned_vars'] = list(concerned_vars)
    with open('./patch_res/'+patch_file+'.json', 'w') as patch_f:
        json.dump(res, patch_f, indent=2)

    # copy to last_release

    # prepare the last_release version
    os.system('rm -rf ./last_release && cp -r ./linux-5.17.6 ./last_release')

    # patch back
    os.system('cd ./linux-5.17.6 && patch  -p1   -R >/dev/null <../tmp/'+patch_file)
    os.system('cd ./linux-5.17.6 && patch  -p1   >/dev/null <../tmp/'+base_patch)

# with open('data.json') as json_file:
#     data = json.load(json_file)
#     data_pretty = json.dumps(data, indent=2)
#     for config in data:
#         config_name = config['config_name']
#         # print(config['config_name'])
#         search_res = config['search_res']
#         for f in search_res:
#             print(f['path'])
