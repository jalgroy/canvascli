#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

from canvasapi import Canvas



class Courses(object):
    def __init__(self, api_url, api_key):
        self.canvas = Canvas(api_url, api_key)

    def run():
        for course in canvas.get_courses():
            print(course.course_code + ": " + course.name)
