import os
import logging
from utils.extract_all_variables import get_all_configs

logging.basicConfig(level=logging.INFO)
configs = get_all_configs()

# tranfer the config variable XXX to CONFIG_XXX
configs = map(lambda x: 'CONFIG_'+x.split()[1], configs)

# test print
# for config in configs:
#     print(config)

def print_indent(indent, s):
    print(indent * ' ' + s)

LINUX_FODER = os.path.abspath('../linux-5.17.6/')
print(LINUX_FODER)
def search_variable(config):
    indent = 0
    print_indent(indent, config)

    indent = 4
    for folder, dirs, files in os.walk(LINUX_FODER+'/'):
        for file in files:
            full_path = os.path.join(folder, file)
            try:
                with open(full_path, 'r') as f:
                    for no, line in enumerate(f):
                        if config in line:
                            print_indent(indent, "file:"+full_path + ' ' + ':' + str(no))
                            print_indent(indent, line)
            except UnicodeDecodeError:
                # just skip the no-text file
                pass
                        

# search the variable
config_no = 1
for config in configs:
    logging.info(f"CONFIG NO:{config_no}")
    config_no += 1
    search_variable(config)
