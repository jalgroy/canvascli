from utils import (print_title, print_info) 

def courses(canvas):
    rows = [[course.course_code, course.name]
            for course in canvas.get_courses()]
    widths = [max(map(len, col)) for col in zip(*rows)]
    header = ["Course code", "Course title"]
    print_title("  ".join((val.ljust(width) for val, width in zip(header, widths))))
    for row in rows[1:]:
        print_info("  ".join((val.ljust(width) for val, width in zip(row, widths))))
