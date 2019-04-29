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
from commands.courses import Courses

def readConfig():
    config_home = os.environ["HOME"] + "/.config"
    with open(config_home + '/canvascli/config.json') as json_file:
        data = json.load(json_file)
        return data

if __name__ == '__main__':
    arguments = docopt(__doc__)
    config = readConfig()
    canvas = Canvas(config["api_url"], config["api_key"])

    if(arguments["courses"]):
        courses = Courses(canvas)
        courses.run()
