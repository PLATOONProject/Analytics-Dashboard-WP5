#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:49:31 2018

@author: 105083

Este fichero esta destinado a que toda funcionalidad de lectura escritura
de ficheros se realice desde la misma. De esta forma si alguna vez cambia
el origen de la fuente de datoss por ejemplo pasa a ser una base de datos
simplemente hay que generar una clase equivalente
"""
import packglobals
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
from typing import List, Dict, Tuple, Sequence

import pickle
import gc


class FileUtils(object):
    """Exceptions are documented in the same way as classes.

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Either form is acceptable, but the two should not be mixed. Choose one
    convention to document the __init__ method and be consistent with it.

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        msg (str): Human readable string describing the exception.
        code (:obj:`int`, optional): Error code.

    Attributes:
        msg (str): Human readable string describing the exception.
        code (int): Exception error code.

    """

    def __init__(self):
        self.data = None
        self.logger = packglobals.logging.getLogger("hpplanner")

    def dumpPickle(self, data: object, filename: str):
        """Example function with PEP 484 type annotations.

        Args:
            data: puede ser un array, dataframe o dictionary.
            filename: full path del directorio a escribir.

        Returns:
            nothing
        """

        output = open(filename, 'wb')
        gc.disable()
        pickle.dump(data, output, protocol=pickle.HIGHEST_PROTOCOL)
        gc.enable()
        output.close()

    def loadPickle(self, filename: str) -> object:
        """Example function with PEP 484 type annotations.

        Args:
            filename: full path del directorio a escribir.

        Returns:
            data: Devuelve un dataframe o dictionary segun se haya volcado.
        """

        output = open(filename, 'rb')
        gc.disable()
        data = pickle.load(output)
        gc.enable()
        output.close()
        return data

    def loadXXXData(self, subdir: str, cols: List[int]) -> object:
        """Example function with PEP 484 type annotations.

        Args:
            subdir: directorio a añadirr a la ruta ../repo/raw.

        Returns:
            data: dataframe.
        """

        self.logger.debug("Starting outdoor file upload")

        rms_df = pd.DataFrame()
        for filename in glob.glob("../repo/raw/"+subdir+"/*.csv"):
            name = os.path.basename(filename)

            self.logger.debug("Procesing XXXX file.." + name)
            df = pd.read_csv(filename, sep=',', decimal='.')
            aux = pd.DataFrame()

            aux["DATE"] = pd.to_datetime(df.iloc[:, 0].values,
                                         format="%Y-%m-%d %H:%M")
            aux = aux.set_index("DATE")
            aux["TEMP"] = df.iloc[:, cols[0]].values
            # aux["FAKE"] = df.iloc[:, cols[1]].values

            rms_df = pd.concat([rms_df, aux])

            self.logger.debug(".. file procesed")

        rms_df = rms_df.sort_index()
        rms_df.interpolate(inplace=True)
        return rms_df

    def sendToCSV(self, idx_col: int , data_col: int, filename: string):
        """Funcion que genera un cvs con dos columnas.
            Solo a titulo ilustrativo.

        Args:
            idx_col: directorio a añadirr a la ruta ../repo/raw.

        Returns:
            data: dataframe.
        """

        self.logger.debug("Starting CSV dump")

        aux_df = pd.DataFrame()
        aux_df["DATE"] = idx_col
        aux_df = aux_df.set_index("DATE")
        aux_df["POWER"] = data_col
        aux_df = aux_df.resample("15T").pad()
        aux_df.to_csv("../output/"+filename+".csv")

        self.logger.debug("Ending CSV dump")
