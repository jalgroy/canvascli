import html2text
import json
import os
import sys

def get_course(canvas, course):
    all_courses = canvas.get_courses()
    all_courses = list(filter(lambda c: c.course_code == course, all_courses))
    
    if not all_courses:
        raise Exception('invalid course')

    choice = 0

    if len(all_courses) > 1:
        print('conflicting courses:')
        for i in range(0, len(all_courses)):
            print(f'\t[{i}]: {all_courses[i].name}')
        choice = input('choose by index: ')
        if not choice.isdigit() or not int(choice) in range(0, len(all_courses)):
            raise Exception('illegal index')

    return all_courses[int(choice)]    

def print_title(message):
    print(f'\033[92;1m{message}\033[0m')

def print_info(message):
    print(f'\033[94m{message}\033[0m')

def print_html(html):
    print_info(html2text.html2text(html))

def print_url(message):
    print(f'\033[97;4m{message}\033[0m')

def check_config(config):
    config_keys = ['api_url', 'api_key', 'files_path']
    config_keys_exist = all([key in config for key in config_keys])
    config_vals_exist = config_keys_exist and all([config[key] for key in config_keys])
    if config_vals_exist:
        return True
    print_info('\nYour canvas-url, api-key and/or output-directory is missing.\n')
    print_info('Use the following commands to set them:')
    print_info('    canvascli set-canvas-url <url>')
    print_info('    canvascli set-api-key <key>')
    print_info('    canvascli set-output-directory <directory>\n')
    print_info('See https://github.com/jalgroy/canvascli for more information.\n')
    return False 

def read_config():
    try:
        with open(get_config_path(), 'r') as config_json:
            return json.load(config_json)
    except:
        return dict()

def get_config_path():
    if 'HOME' in os.environ:
        config_home = os.environ['HOME'] + '/.config'
    elif '%APPDATA%' in os.environ:
        config_home = os.environ['%APPDATA']
    else:
        config_home = './'
    config_path = config_home + '/canvascli/config.json'
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    return config_path 

def write_to_config(key, value):
    current_config = read_config()
    with open(get_config_path(), 'w+') as config_json:
        current_config[key] = value
        data_as_json = json.dumps(current_config)
        config_json.write(data_as_json)
