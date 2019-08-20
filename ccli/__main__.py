'''Usage:
    ccli courses 
    ccli assignments <course>
    ccli announcements <course> [--last=<n>]
    ccli files <course>
    ccli set-output-directory <directory>
    ccli set-api-key <key>
    ccli set-canvas-url <url>

Options:
    --last=<n>  Get the last n items [default: 100]
'''
import sys

from docopt import docopt
from canvasapi import Canvas
from inspect import getmembers, isclass

from ccli.commands import courses, announcements, files, assignments 

from ccli.utils import (get_config_path, write_to_config, read_config, print_title, print_info, check_config)

def main(args=None):
    arguments = docopt(__doc__)

    if arguments['set-output-directory']:
        write_to_config('files_path', arguments['<directory>'])
        sys.exit(0)

    if arguments['set-api-key']:
        write_to_config('api_key', arguments['<key>'])
        sys.exit(0)
    
    if arguments['set-canvas-url']:
        write_to_config('api_url', arguments['<url>'])
        sys.exit(0)
    
    config = read_config()
    if not check_config(config):
        sys.exit(1)

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
    main()