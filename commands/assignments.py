from utils import * 

def assignments(canvas, course):
    course = get_course(canvas, course)
    assignments = course.get_assignments()

    for assignment in assignments:
        print_title(f"{assignment.name}")
        print_info(f"{assignment.html_url}")
        print_info(f"due: {assignment.due_at}")