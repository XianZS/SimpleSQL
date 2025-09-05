# -*- coding: UTF-8 -*-
"""
# Basic Information Of The File
    @Project : SimpleSQL 
    @File    : set_route.py
    @Author  : XianZS
# Meaning
"""
import i_route
import time


class SetRoute(i_route.IRoute):
    def __init__(self):
        """ pass """

    def judge_route(self, route: str) -> tuple:
        if route == '':
            return ("")
