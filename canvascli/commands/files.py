from utils import (get_course) 

import urllib.request
import os

def files(canvas, course, output_path):
    course = get_course(canvas, course)

    for f in course.get_files():
        sub_folder = canvas.get_folder(f.folder_id).attributes['full_name']
        course_name = course.name.replace('/', '')
        full_path = output_path + course_name + '/' + sub_folder + '/'

        if not os.path.exists(full_path):
            os.makedirs(full_path)

        print(f'Downloading {f.filename}')

        urllib.request.urlretrieve(f.url, f'{full_path}{f.filename}')
