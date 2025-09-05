# -*- coding: UTF-8 -*-
"""
# Basic Information Of The File
    @Project : SimpleSQL 
    @File    : i_route.py
    @Author  : XianZS
# Meaning
"""
from abc import ABC, abstractmethod


class IRoute(ABC):
    @abstractmethod
    def judge_route(self, route: str) -> tuple:
        """
        :return: (route,true/false)
        """

    @abstractmethod
    def type_route(self, route: str) -> tuple:
        """
        绝对路径:1
        相对路径:2
        :return: (route_type,true/false)
        """

    @abstractmethod
    def set_route(self, route: str) -> tuple:
        """
        :return: (route,true/false)
        """
