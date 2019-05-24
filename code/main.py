#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: insert date (e.g. 2020/12/25)
@author: your name, username or email (e.g. name.surname@tecnalia.com)

Short description of the aims of the script.
"""

from logging import getLogger
from logging.config import fileConfig
from configparser import ConfigParser
from my_module import MyClass


if __name__ == "__main__":

    # --------------------------------------------------------------------------
    # Logger configuration
    # --------------------------------------------------------------------------
    fileConfig('logging_config.ini')
    logger = getLogger(__name__)

    logger.info('Starting process.')

    # --------------------------------------------------------------------------
    # Application configuration
    # --------------------------------------------------------------------------
    config = ConfigParser(allow_no_value=True)
    config.read('config.ini')

    # --------------------------------------------------------------------------
    # Code referring to my_module
    # --------------------------------------------------------------------------
    myclass = MyClass()

    # insert your code here

    # --------------------------------------------------------------------------
    # Code referring to other module
    # --------------------------------------------------------------------------
    # insert your code here

    logger.info("The End")
