# -*- coding: utf-8 -*-
"""

@author: 105083

Funcion ejemplo de como utilizar el logger, plotutils y fileutils desde
un fichero main
"""

import fileutils
import logging
import plotutils

if __name__ == "__main__":
   
    FORMAT = '%(levelname)s - %(asctime)s - %(filename)s::%(funcName)s - %(message)s'
    #logging.basicConfig(level=logging.DEBUG, format = '%(levelname)s - %(asctime)s - %(filename)s:%(lineno)s - %(message)s')
    logging.basicConfig(level=logging.DEBUG, format = FORMAT)
    logger = logging.getLogger("fhp-model")
    
    handler = logging.FileHandler('../output/out.log')
    handler.setLevel(logging.DEBUG)
    # create a logging format
    formatter = logging.Formatter(FORMAT)
    handler.setFormatter(formatter)

    # add the handlers to the logge
    logger.addHandler(handler)

    logger.info("Starting main process..")

    BULD = BULD_2_3
    APTS = APTS_2_3
    ENER = ENER_2_3
    OUTD = OUTD_2_3


    fu = fileutils.FileUtils()
    pu = plotutils.PlotUtils()
	"""
	Las llamadas y funciones que se muestran a continuación carecen de funcionalida
	simplemente tratan de ilustrar como se haría uso de las clases anteriormente
	instanciadas, fileutils y plotutils
	"""
    df_out = fu.loadOutdoorData(BULD,OUTD)
    df_ene = fu.loadEnergyData(BULD,ENER) 
    df_ind = fu.loadIndoorData(BULD,APTS)
   
    pu.doPlotDaily(dct_ind, dct_out, dct_ene)
    
    logger.info(".. process ended")
