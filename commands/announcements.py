from utils import * 

def announcements(canvas, course):
    course = get_course(canvas, course)
    context_code = "course_" + str(course.id)

    announcements = canvas.get_announcements(context_codes = context_code)

    for announcement in announcements:
        print_title(announcement.title)
        print_html(announcement.message)
        print_url(announcement.url)
        print()
