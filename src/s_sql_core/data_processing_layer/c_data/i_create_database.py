# -*- coding: UTF-8 -*-
"""
# Basic Information Of The File
    @Project : SimpleSQL 
    @File    : i_create_database.py
    @Author  : XianZS
# Meaning
    创建数据库基础部分
"""
import sqlite3
from typing import Any
from abc import ABC, abstractmethod


class create_database(ABC):
    """
    ## Interface Method

    - cd(self) -> tuple
    - set_database_name(self,database_name) -> tuple
    - other -> Any
    """

    @abstractmethod
    def create_database(self) -> tuple:
        """
        create database method
        :return: (true/false,database_name)
        """

    @abstractmethod
    def set_database_name(self, database_name: str) -> tuple:
        """
        set database name method
        :return: (true/false,database_name)
        """

    @abstractmethod
    def set_database_route(self, database_route: str) -> tuple:
        """
        set database route method
        :return: (true/false,database_route)
        """

    @abstractmethod
    def pr(self, *args, **kwargs) -> tuple:
        """ print something """

    @abstractmethod
    def other(self) -> Any:
        """
        Temporary code
        :return: None
        """
