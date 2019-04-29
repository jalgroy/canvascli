from utils import * 

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