import os
import configparser

def test_if_config_file_exists(config_path):
    if not os.path.isfile(config_path):
        print('Config file *'+config_path +
              '* is missing. Execution will be stopped!')
        exit()

def read_system_config(system_config = "system.config"):
    test_if_config_file_exists(system_config)
    config = configparser.RawConfigParser()
    config.read(system_config)
    return config