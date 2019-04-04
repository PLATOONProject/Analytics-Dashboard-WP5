#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Seccion de configuracion del logger

Created on 29/08/2017
@author: root
'''

import logging
import logging.handlers as handlers
import traceback

FORMAT = '%(levelname)s - %(asctime)s - %(filename)s::%(funcName)s - %(message)s'
#logging.basicConfig(level=logging.DEBUG, format ='%(levelname)s - %(asctime)s - %(filename)s:%(lineno)s - %(message)s')
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger("hpplanner")
formatter = logging.Formatter(FORMAT)

# Volcado a fichero plano, cuando vayas a pasar a producción tu aplicación comenta esta sección
handler = logging.FileHandler('../results/logs/fhp.log')
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logger.addHandler(handler)

# Volcado a fichero rotativo,en producción solo debería estar este handle activo
handler = handlers.RotatingFileHandler('../results/logs/rot.log',
                                       maxBytes=5000000, backupCount=10)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logger.addHandler(handler)
