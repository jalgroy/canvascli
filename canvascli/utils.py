import html2text

def get_course(canvas, course):
    all_courses = canvas.get_courses()
    all_courses = list(filter(lambda c: c.course_code == course, all_courses))
    
    if not all_courses:
        raise Exception('invalid course')

    choice = 0

    if len(all_courses) > 1:
        print('conflicting courses:')
        for i in range(0, len(all_courses)):
            print(f'\t[{i}]: {all_courses[i].name}')
        choice = input('choose by index: ')
        if not choice.isdigit() or not int(choice) in range(0, len(all_courses)):
            raise Exception('illegal index')

    return all_courses[int(choice)]    

def print_title(message):
    print(f'\033[92;1m{message}\033[0m')

def print_info(message):
    print(f'\033[94m{message}\033[0m')

def print_html(html):
    print_info(html2text.html2text(html))

def print_url(message):
    print(f'\033[97;4m{message}\033[0m')
