# -*- coding: utf-8 -*-
"""

@author: 105083

Funcion ejemplo de como utilizar el logger, plotutils y fileutils desde
un fichero main
"""

import fileutils
import logging
import plotutils
import numpy as np
import pandas as pd


##############################
#### Funciones Auxiliares ####
###############################


APTS = ["APT1","APT2","APT3","APT4","APT5","APT6","APT7","APT8"]

APTS_2_1 = [1,2,3]
ENER_2_1 = [1]
OUTD_2_1 = [1]
BULD_2_1 = "2.1"

APTS_2_3 = [1,2,3,4,5]
ENER_2_3 = [1]
OUTD_2_3 = [1]
BULD_2_3 = "2.3"




'''
    This function converts the excel dataframe into appropiate numpy arrays
    :param df: dataframe containing excel data
    :param X_labels: Labels with the input data we want to work with
    :param Y_label: Output labels (Normally Cu)
    :return:
'''
def df2numpy_soloX(df, X_labels = []):

    X = np.array(df[X_labels])
    return X


def dct2numpy(dct, X_labels = [],transpose = False):
    aux = pd.DataFrame(columns=X_labels)
    is_ini = True
    for item in dct.keys():
        if (is_ini == True):
            aux = dct[item][X_labels]
            aux = aux.set_index(dct[item].index.hour)
            aux = aux.transpose()
            is_ini = False
        else:
            aux_tmp = pd.DataFrame(columns=X_labels)
            aux_tmp = dct[item][X_labels]
            aux_tmp = aux_tmp.set_index(dct[item].index.hour)
            aux_tmp = aux_tmp.transpose()
            aux = aux.append(aux_tmp,ignore_index=True)
    aux = aux.fillna(method='ffill')
    return (np.array(aux[aux.columns]))

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
