from ccli.utils import (get_course, print_info, print_title, print_html, print_url) 
import urllib.request
import datetime
import re
import os

def courses(canvas):
    rows = [[course.course_code, course.name]
            for course in canvas.get_courses()]
    print()
    widths = [max(map(len, col)) for col in zip(*rows)]
    header = ["Course code", "Course title"]
    print_title("  ".join((val.ljust(width) for val, width in zip(header, widths))))
    for row in rows[1:]:
        print_info("  ".join((val.ljust(width) for val, width in zip(row, widths))))
    print()

def announcements(canvas, course, lastN):
    course = get_course(canvas, course)
    context_code = "course_" + str(course.id)
    delta = datetime.timedelta(10000)
    start = (datetime.datetime.now() - delta).isoformat()
    end = datetime.datetime.now().isoformat()

    announcements = canvas.get_announcements(context_codes = context_code, start_date = start, end_date = end)

    for announcement in list(announcements)[0:int(lastN)][::-1]:
        date = re.sub('T.*','',announcement.posted_at)
        print_title("[{}] {}".format(date, announcement.title))
        print_html(announcement.message)
        print_url(announcement.url)
        print()

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

def assignments(canvas, course):
    course = get_course(canvas, course)
    assignments = course.get_assignments()
    for assignment in assignments:
        print_title(assignment.name)
        # print_html(assignment.attributes['description'])
        print_info(f"due: {assignment.due_at}")
        print_info(f"submitted: {assignment.has_submitted_submissions}")
        print_info(f'published: {assignment.published}')
        print_url(assignment.html_url)
        print()