def get_course(canvas, course):
    all_courses = canvas.get_courses()
    all_courses = list(filter(lambda c: c.course_code == course, all_courses))
    
    if not all_courses:
        raise Exception('invalid course')

    if len(all_courses) > 1:
        raise Exception('conflicting course names')

    return all_courses[0]    

def print_title(message):
    print(f'\033[95m{message}\033[0m')

def print_info(message):
    print(f'\033[94m{message}\033[0m')

def print_warning(message):
    print(f'\033[93m{message}\033[0m')
