'''
Usage:
    canvascli.py courses
    canvascli.py assignments <course>
    canvascli.py announcements <course>
'''
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)