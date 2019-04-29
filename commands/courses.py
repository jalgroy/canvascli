#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

from canvasapi import Canvas
from utils import * 

class Courses(object):
    def __init__(self, canvas):
        self.canvas = canvas

    def run(self):
        rows = [[course.course_code, course.name]
                for course in self.canvas.get_courses()]
        widths = [max(map(len, col)) for col in zip(*rows)]
        header = ["Course code", "Course title"]
        print_title("  ".join((val.ljust(width) for val, width in zip(header, widths))))
        for row in rows[1:]:
            print_info("  ".join((val.ljust(width) for val, width in zip(row, widths))))
