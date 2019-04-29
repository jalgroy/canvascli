'''
Usage:
    canvascli.py courses
    canvascli.py assignments <course>
    canvascli.py announcements <course>
'''

from docopt import docopt
from canvasapi import Canvas
import json

from commands.assignments import assignments

def readConfig():
    with open('./config.json') as json_file:
        data = json.load(json_file)
        return data

if __name__ == '__main__':
    arguments = docopt(__doc__)
    config = readConfig()
    canvas = Canvas(config["api_url"], config["api_key"])

    assignments(canvas, 'INF237') 