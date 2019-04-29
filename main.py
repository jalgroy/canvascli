'''
Usage:
    canvascli.py courses
    canvascli.py assignments <course>
    canvascli.py announcements <course>
'''

from docopt import docopt
from canvasapi import Canvas
from inspect import getmembers, isclass
import json
import os

from commands.courses import courses
from commands.assignments import assignments
from commands.announcements import announcements 

def readConfig():
    if("HOME" in os.environ):
        config_home = os.environ["HOME"] + "/.config"
    elif("%APPDATA%" in os.environ):
        config_home = os.environ["%APPDATA%"]
    else:
        config_home = "./"
    with open(config_home + '/canvascli/config.json') as json_file:
        data = json.load(json_file)
        return data

if __name__ == '__main__':
    arguments = docopt(__doc__)
    config = readConfig()
    canvas = Canvas(config['api_url'], config['api_key'])

    if(arguments["courses"]):
        courses(canvas)
    
    if arguments['assignments']:
        assignments(canvas, arguments['<course>'])

    if arguments['announcements']:
        announcements(canvas, arguments['<course>'])
