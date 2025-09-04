# -*- coding: UTF-8 -*-
"""
# Basic Information Of The File
    @Project : SimpleSQL 
    @File    : dpl_c_main.py
    @Author  : XianZS
# Meaning
"""
from typing import Any
from time import time
import sqlite3
from i_create_database import create_database


class c_data(create_database):
    database_name: str = str(time())

    def __init__(self, db_name: str, db_route: str):
        """ pass """
        self.set_database_name(db_name)
        self.pr("set_database_name:{}".format(self.database_name))

    def create_database(self) -> tuple:
        """ pass """
        conn = sqlite3.connect(self.database_name)
        if conn:
            return conn, True
        else:
            return "ERROR", False

    def set_database_name(self, database_name) -> tuple:
        """ pass """
        self.database_name = database_name

    def set_database_route(self, database_route) -> tuple:
        """ pass """

    def pr(self, *args, **kwargs) -> tuple:
        """ pass """
        if args and kwargs:
            print(args)
            print(kwargs)
            return (args, kwargs), True
        elif args:
            print(args)
            return args, True
        elif kwargs:
            print(kwargs)
            return kwargs, True
        else:
            return "None:data is None", False

    def other(self) -> Any:
        """ other """
