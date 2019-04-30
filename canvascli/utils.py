import html2text
import json
import os

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


def read_config():
    with open(get_config_path()) as config_json:
        try:
            data = json.load(config_json)
            return data
        except:
            return dict()

def get_config_path():
    if 'HOME' in os.environ:
        config_home = os.environ['HOME'] + '/.config'
    elif '%APPDATA%' in os.environ:
        config_home = os.environ['%APPDATA']
    else:
        config_home = './'
    return config_home + '/canvascli/config.json'

def write_to_config(key, value):
    with open(get_config_path(), 'r+') as config_json:
        try:
            data = json.load(config_json)
        except:
            data = dict()
        config_json.truncate(0)
        data[key] = value
        data_as_json = json.dumps(data)
        config_json.write(data_as_json)