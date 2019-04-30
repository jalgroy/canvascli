'''
Usage:
    canvascli.py courses
    canvascli.py assignments <course>
    canvascli.py announcements <course> [--last=<n>]
    canvascli.py files <course>

    canvascli.py set-output-directory <directory>
    canvascli.py set-api-key <key>
    canvascli.py set-canvas-url <url>

Options:
    --last=<n>  Get the last n items [default: 100]
'''

from docopt import docopt
from canvasapi import Canvas
from inspect import getmembers, isclass
import json
import os

from commands.courses import courses
from commands.assignments import assignments
from commands.announcements import announcements 
from commands.files import files

def read_config():
    if("HOME" in os.environ):
        config_home = os.environ["HOME"] + "/.config"
    elif("%APPDATA%" in os.environ):
        config_home = os.environ["%APPDATA%"]
    else:
        config_home = "./"
    with open(config_home + '/canvascli/config.json') as json_file:
        data = json.load(json_file)
        return data

def check_config(config):
    valid_config = config['api_url'] and config['api_key'] and config['files_path']
    if not config['api_url']:
        print('please specify your canvas url')
    if not config['api_key']:
        print('please specify your canvas api key')
    if not config['files_path']:
        print('please specify your output directory')
    return valid_config

def start():
    arguments = docopt(__doc__)

    if arguments['set-output-directory']:
        pass # todo: write to config.json

    if arguments['set-api-key']:
        pass # todo: write to config.json
    
    if arguments['set-canvas-url']:
        pass # todo: write to config.json

    config = read_config()
    if not check_config(config):
        return

    canvas = Canvas(config['api_url'], config['api_key'])

    if arguments["courses"]:
        courses(canvas)
    
    if arguments['assignments']:
        assignments(canvas, arguments['<course>'])

    if arguments['announcements']:
        announcements(canvas, arguments["<course>"], arguments["--last"])

    if arguments['files']:
        files(canvas, arguments['<course>'], config['files_path'])


if __name__ == '__main__':
    start()