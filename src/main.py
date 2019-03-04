# -*- coding: utf-8 -*-
"""

@author: 105083

Funcion ejemplo de como utilizar el logger, plotutils y fileutils desde
un fichero main
"""

import fileutils
import logging
import plotutils
import packglobals

if __name__ == "__main__":

    logger = packglobals.logger
    logger.info('Starting process...' + 'yeahhh...')

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
