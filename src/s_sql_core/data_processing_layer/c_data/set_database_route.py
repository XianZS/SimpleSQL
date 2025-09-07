# -*- coding: UTF-8 -*-
"""
# Basic Information Of The File
    @Project : SimpleSQL 
    @File    : set_database_route.py
    @Author  : XianZS
# Meaning
"""
import os
import i_database_route
import time


class SetDataBaseRoute(i_database_route.IDataBaseRoute):
    # Public child
    database_route = os.getcwd()

    def __init__(self):
        """ pass """

    def type_route(self, route: str) -> tuple:
        """
        type_route:
        AP:绝对路径，返回True
        RP:相对路径，返回False
        """
        # 建立在路径合法的情况下判断路径类型
        if route[0] == '.':
            return route, False
        else:
            return route, True

    def judge_route(self, route: str) -> tuple:
        """
        判断路径是否合法，（是否为空，是否存在）
        """
        if route:
            # route is not null
            _route_status = os.path.exists(route)
            if _route_status:
                # route 合法
                return route, True
            else:
                return route, False
        else:
            return route, False

    def set_route(self, route: str) -> tuple:
        """
        借助type_route和judge_route,设置共有属性self.database_route=route
        """
        if route:
            _, ok = self.judge_route(route)
            if ok:
                self.database_route = route
                _type = self.type_route(route)[1]
                if _type:
                    # AP (absolute path)
                    return "AP", True
                else:
                    # RP (relative path)
                    return "RP", True
            else:
                return route, False
        else:
            return route, False
