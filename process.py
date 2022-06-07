'''
open the grep file res.txt and process it
'''
import json
import os
import re


# get the blocks of the search file
# one block is a config search result
def get_blocks(file_name):
    blocks = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        block_no = 1
        cur_block = []
        for line in lines:
            # next block begins
            if line == str(block_no+1):
                blocks.append(cur_block.copy())
                cur_block.clear()
                cur_block.append(line)
                block_no += 1
            else:  # add the current line to the block
                cur_block.append(line)
        blocks.append(cur_block)
    return blocks 


'''
    one block is the search result of a config variable
    the basic pattern
    
    config number
    CONFIG_NAME::CONFIG_XXXXX
    FILE_NAME
    line_number:line-content
    line_number:line-content

    FILE_NAME
    line_number:line-content
    line_number:line-content

    the transfered json pattern
    {
        "config_name:" "XXXX"
        "search_res": [
            {
                "file_path": "./linux-5.17.6/arch/XXXX",
                "hits":
                    [
                        {
                            "line_no" : XXX,
                            "content" : XXX
                        },
                        {
                            "line_no" : XXX,
                            "content" : XXX
                        }


                    ]

            },
            {
                "file_path": "./linux-5.17.6/...",
                "hits": 
                    [
                        {
                            "line_no" : XXX,
                            "content" : XXXX,

                        }

                        {
                            "line_no" : XXX,
                            "content" : XXXX,

                        }

                    ]

            }
        ]
'''


def block_to_json(block):
    cur_config = {}

    # extract the config name
    config_name = block[1].split('::')[1]
    cur_config['config_name'] = config_name

    # print(config_name)

    file_blocks = []
    cur_block = []
    
    for line in block[2:]:
        # print(line)
        if line == '':
            if len(cur_block) > 0:
                if cur_block != []:
                    file_blocks.append(cur_block.copy())
                    cur_block.clear()
        else:  # push it cur_block
            cur_block.append(line)
    if cur_block != []:
        file_blocks.append(cur_block)
    # print(file_blocks)

    file_blocks_json = []
    single_block_json = {}
    for file_block in file_blocks:  # file_block 
        single_block_json['path'] = file_block[0]
        single_block_json['hits'] = []
        for hit in file_block[1:]: 
            # print('hit:' + hit)
            line_no = int(hit.split(':')[0])
            content = hit[len(hit.split(':')[0])+1:]
            cur_hit = {
                    "line_no": line_no,
                    "content": content
                    }

            single_block_json['hits'].append(cur_hit.copy())
            cur_hit.clear()

        file_blocks_json.append(single_block_json.copy())
        single_block_json.clear()

    cur_config["search_res"] = file_blocks_json
    return cur_config


# from the json file, get all the extension
#     if it ends with .XXX, then the extension is XXX
#     if it not, it will return the filename
def get_all_extension(config_list):
    # the rule string and its corresponding res
    rules_str = ['[mM]akefile', '[\w-]+.c', '[\w-]+.h', '\w*_defconfig', '[\w-]+.md', '[\w-]+.py', '[\w-]+.S']
    rules_res = ['makefile', 'source', 'header', 'deconfig', 'markdown', 'python', 'assembly']

    # match hits
    rules_hits = [0] * len(rules_str)

    # compile the re string
    rules_re = map(re.compile, rules_str)
    rules = dict(zip(rules_re, rules_res))

    unmathed_file = []
    for conf in config_list:
        search_res = conf["search_res"]
        for file_block in search_res:
            path = file_block['path']
            file_name = os.path.basename(path)

            for i, (rule, res) in enumerate(rules.items()):
                if rule.match(file_name):
                    rules_hits[i] += 1
                    break
            else:
                unmathed_file.append(file_name)

                    
    print(unmathed_file)
            # print(file_name)


if __name__ == '__main__':
    # blocks = get_blocks("./res.txt")
    # res = map(block_to_json, blocks)
    # res = list(res)
    # pretty_res = json.dumps(res, indent=2)
    # print(pretty_res)
    # with open('data.txt', 'w') as f:
    #     json.dump(res, f, indent=2)
    with open('data.json', 'r') as f:
        data = json.load(f)
    get_all_extension(data)
    # print(data)
    # s = json.dumps(data, indent=2)
    # print(s)
