#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Seccion de configuracion del logger

Created on 29/08/2017
@author: root
'''
import logging
import logging.handlers as handlers


FORMAT = '%(levelname)s - %(asctime)s - %(filename)s::%(funcName)s - %(message)s'
#logging.basicConfig(level=logging.DEBUG, format ='%(levelname)s - %(asctime)s - %(filename)s:%(lineno)s - %(message)s')
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger("hpplanner")
formatter = logging.Formatter(FORMAT)

# Volcado a fichero plano
handler = logging.FileHandler('./output/fhp.log')
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logger.addHandler(handler)

# Volcado a fichero rotativo
handler = handlers.RotatingFileHandler('./output/rot.log',
                                       maxBytes=50000, backupCount=20)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logger.addHandler(handler)
