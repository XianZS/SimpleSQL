# -*- coding: UTF-8 -*-
"""
# Basic Information Of The File
    @Project : SimpleSQL 
    @File    : i_name.py
    @Author  : XianZS
# Meaning
"""
from abc import ABC, abstractmethod


class IName(ABC):
    @abstractmethod
    def name(self, database_name: str | None) -> tuple:
        """
        :return: (database_name, true/false)
        """
