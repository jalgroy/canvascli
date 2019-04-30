from utils import (get_course, print_title, print_html, print_url) 
import datetime
import re

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
