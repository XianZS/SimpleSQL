# -*- coding: UTF-8 -*-
"""
# Basic Information Of The File
    @Project : SimpleSQL 
    @File    : set_database_name.py
    @Author  : XianZS
# Meaning
"""
import i_database_name
import time
import re


class SetDataBaseName(i_database_name.IDataBaseName):
    # Private child
    __pattern = r'^[a-zA-Z0-9_]+\Z'  # \Z表示字符串结尾

    def __init__(self):
        """ pass """

    def __get_timestamp(self) -> tuple:
        """
        在数据库名称为None/不正确时，将数据库名设置为当前时间戳的小数点后位
        """
        time_1 = str(time.time()).split(".")[0]
        if time_1 != '0' and time_1:
            return time_1, True
        else:
            return "000_000_000", False

    def judge_database_name(self, database_name: str | None) -> tuple:
        new_database_name, ok = self.__get_timestamp()
        if database_name is None:
            if ok:
                return new_database_name, False
            else:
                return new_database_name, False
        else:
            # 是否只包含数字字母下划线
            res_1 = bool(re.match(self.__pattern, database_name))
            if res_1:
                return database_name, True
            else:
                return database_name, False

    def set_database_name(self, database_name: str | None) -> tuple:
        pass
