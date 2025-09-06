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

    def type_route(self, route: str) -> tuple:
        # 建立在路径合法的情况下判断路径类型
        if route[0] == '.':
            return route, False
        else:
            return route, True

    def judge_route(self, route: str) -> tuple:
        if route:
            # route 合法
            return route, True
        else:

            return route, False
