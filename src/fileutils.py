# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:49:31 2018

@author: 105083

Este fichero esta destinado a que toda funcionalidad de lectura escritura
de ficheros se realice desde la misma. De esta forma si alguna vez cambia
el origen de la fuente de datoss por ejemplo pasa a ser una base de datos
simplemente hay que generar una clase equivalente
"""
import numpy as np
import pandas as pd
import logging
import glob
import os
import math
import dateutil.parser as DP
import numpy

from os import listdir
from os.path import isfile, join

import pickle
import gc

class FileUtils(object):

    def __init__(self):
        self.data           = None
        self.logger = logging.getLogger("fhp-model")

	"""
	Funcion que vuelca el contenido de data en un pickle
	"""
    def dumpPickle(self,data,filename):
        output = open(filename, 'wb')
        gc.disable()
        pickle.dump(data, output, protocol=pickle.HIGHEST_PROTOCOL)
        gc.enable()
        output.close()

	"""
	Funcion que carga el contenido de un Pickle
	"""
    def loadPickle(self,filename):
        output = open(filename, 'rb')
        gc.disable()
        data = pickle.load(output)
        gc.enable()
        output.close()
        return data

	"""
	Funcion ejemplo de la lectura de csv. Solo a titulo ilustrativo
	"""
    def loadOutdoorData(self,building,cols):

        self.logger.debug("Starting outdoor file upload")

        rms_df = pd.DataFrame()
        for filename in glob.glob("../repo/outdoor/"+building+"/*.csv"):
            name = os.path.basename(filename)

            self.logger.debug("Procesing outdoor file.." + name)
            df = pd.read_csv(filename, sep=',', decimal='.')
            aux = pd.DataFrame()

            aux["DATE"] = pd.to_datetime(df.iloc[:, 0].values, format="%Y-%m-%d %H:%M")
            aux = aux.set_index("DATE")
            aux["TEMP"] = df.iloc[:, cols[0]].values
            # aux["FAKE"] = df.iloc[:, cols[1]].values

            rms_df = pd.concat([rms_df, aux])

            self.logger.debug(".. file procesed")

        rms_df = rms_df.sort_index()
        rms_df.interpolate(inplace=True)
        return rms_df

	"""
	Funcion que genera un cvs con dos columnas. Solo a titulo ilustrativo.
	"""
    def sendToCSV(self,idx_col, data_col,filename):
        self.logger.debug("Starting CSV dump")

        aux_df = pd.DataFrame()
        aux_df["DATE"] = idx_col
        aux_df = aux_df.set_index("DATE")
        aux_df["POWER"] = data_col
        aux_df = aux_df.resample("15T").pad()
        aux_df.to_csv("../output/"+filename+".csv")

        self.logger.debug("Ending CSV dump")
