'''Usage:
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

from commands.courses import courses
from commands.assignments import assignments
from commands.announcements import announcements 
from commands.files import files

from utils import (get_config_path, write_to_config, read_config, print_title, print_info)

config_keys = ['api_url', 'api_key', 'files_path']

def check_config(config):
    files_in_config = all([key in config for key in config_keys])
    valid = files_in_config and all([config[key] for key in config_keys])

    if not 'api_url' in config or not config['api_url']:
        print_title('you have to specify your canvas url')
        print_info('canvascli set-canvas-url <url>')

    if not 'api_key' in config or not config['api_key']:
        print_title('you have to specify your canvas api key')
        print_info('canvascli set-api-key <key>')

    if not 'files_path' in config or not config['files_path']:
        print_title('you have to specify your output directory')
        print_info('canvascli set-output-directory <directory>')

    return valid 

def start():
    arguments = docopt(__doc__)

    if arguments['set-output-directory']:
        write_to_config('files_path', arguments['<directory>'])
        return

    if arguments['set-api-key']:
        write_to_config('api_key', arguments['<key>'])
        return
    
    if arguments['set-canvas-url']:
        write_to_config('api_url', arguments['<url>'])
        return

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