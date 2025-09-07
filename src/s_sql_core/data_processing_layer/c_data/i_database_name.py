# -*- coding: UTF-8 -*-
"""
# Basic Information Of The File
    @Project : SimpleSQL 
    @File    : i_database_name.py
    @Author  : XianZS
# Meaning
"""
from abc import ABC, abstractmethod


class IDataBaseName(ABC):
    @abstractmethod
    def database_name(self, database_name: str | None) -> tuple:
        """
        :return: (database_name, true/false)
        """

    def judge_database_name(self, database_name: str | None) -> tuple:
        """
        :return: (database_name, true/false)
        """
