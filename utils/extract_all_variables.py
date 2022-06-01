import pathlib
import os
import logging

LINUX_FOLDER = "linux-5.17.6"
logging.basicConfig(level=logging.INFO)


def generate_config_file():
    logging.info("linux folder:%s", LINUX_FOLDER)

    parent_dir = pathlib.Path(__file__).parent
    target_dir = os.path.abspath(os.path.join(parent_dir, '..', LINUX_FOLDER))
    logging.info("the target dir:%s", target_dir)

    os.chdir(target_dir)
    logging.info("current working directory:%s", os.getcwd())

    cmd_str = 'make scriptconfig ' + 'SCRIPT=Kconfiglib/examples/print_tree.py ' + '>../config_list_' + LINUX_FOLDER.replace('.', '_') + '.txt'
    os.system(cmd_str)


def get_all_configs():
    parent_dir = pathlib.Path(__file__).parent
    target_dir = os.path.abspath(os.path.join(parent_dir, '..', LINUX_FOLDER))
    logging.info("the target dir:%s", target_dir)

    os.chdir(target_dir)

    with open('../config_list_' + LINUX_FOLDER.replace('.', '_') + '.txt') as f:
        configs = [line.strip() for line in f.readlines()]
        return configs
