import html2text

def get_course(canvas, course):
    all_courses = canvas.get_courses()
    all_courses = list(filter(lambda c: c.course_code == course, all_courses))
    
    if not all_courses:
        raise Exception('invalid course')

    if len(all_courses) > 1:
        raise Exception('conflicting course names')

    return all_courses[0]    

def print_title(message):
    print(f'\033[92;1m{message}\033[0m')

def print_info(message):
    print(f'\033[94m{message}\033[0m')

def print_html(html):
    print_info(html2text.html2text(html))

def print_url(message):
    print(f'\033[97;4m{message}\033[0m')
