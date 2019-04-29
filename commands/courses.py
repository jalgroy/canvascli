#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

from canvasapi import Canvas

class Courses(object):
    def __init__(self, canvas):
        self.canvas = canvas

    def run(self):
        for course in self.canvas.get_courses():
            print(course.course_code + ": " + course.name)
