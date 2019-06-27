#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: insert date (e.g. 2020/12/25)
@author: your name, username or email (e.g. name.surname@tecnalia.com)

Short description of the aims of the script.
"""
from logging import getLogger
from configparser import ConfigParser


class MyClass:
    def __init__(self, logger=None):
        # set logger
        self.logger = getLogger('__main__') if logger is None else logger
        # parse config.ini file
        self.config = ConfigParser(allow_no_value=True)
        self.config.read('config.ini')

    # example of instance method
    def my_instance_method(self, arg1, arg2):
        """Short description of the method.

        Args:
            arg1: object type, description.
            arg2: object type, description.

        Returns:
            output1: object type, description.

        Raises:
            SomeError: condition for the error.

        """
        # insert your code here.

        return None

    # example of class method
    @classmethod
    def my_classmethod(cls, arg1, arg2):
        """Short description of the method.

        Args:
            arg1:
            arg2:

        Returns:

        """

        # insert your code here.

        return None

    # example of static method
    @staticmethod
    def my_staticmethod(arg1, arg2):
        """Short description of the method.

        Args:
            arg1:
            arg2:

        Returns:

        """

        # insert your code here.

        return None
