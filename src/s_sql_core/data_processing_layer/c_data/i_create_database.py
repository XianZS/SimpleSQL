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
    @abstractmethod
    def cd(self) -> tuple:
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
    def other(self):
        """
        Temporary code
        :return: None
        """
