from utils import * 

def assignments(canvas, course):
    course = get_course(canvas, course)
    assignments = course.get_assignments()
    # .name     .html_url   .has_submitted_submissions    .points_possible     .description   .due_at

    for assignment in assignments:
        print_title(f"{assignment.name}")
        print_info(f"{assignment.html_url}")

        print()