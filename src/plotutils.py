# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:49:31 2018

@author: 105083

Este fichero esta destinado a que toda funcionalidad de plot se hecha desde
esta clase. De esta forma resulta sencilla deshabilitar dicha funcionalidad
llegado el caso
"""

import logging
import fileutils
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from scipy.integrate import simps


class PlotUtils(object):

    def __init__(self):
        self.data           = None
        self.logger = logging.getLogger("fhp-model")

	'''
	Esta funcion realiza el plot por días, una recomendación es que 
	los plots se vuelquen a fichero.. pero no es mas que una recomendación
	que a mi me resulta comoda.
	
	Ejemplo de código, solo funciones demostrativas...
		
	'''
    def doPlotDaily (self,ind_dct,out_dct,ene_dct):
		
        fu = fileutils.FileUtils()
        for item in ind_dct.keys():
            mm = 1
            columns = ["APT1","APT2","APT3","APT3"]
            aux_ene = ene_dct[item]["DENERGY"]
            aux_tem = out_dct[item]["TEMP"]
            plt.figure(figsize=(20, 10))
            ax = plt.subplot(1,1, 1)
            ax.plot(aux_tem.index, aux_tem)
            ax2 = ax.twinx()
            ax2.plot(aux_tem.index, aux_ene)

            # for col_item in columns:
            #
            #     ax = plt.subplot(2, len(columns) / 2, mm)
            #     # ax.yaxis.set_label_text(year + "_" + col_item)
            #     # ax.xaxis.set_major_formatter(mdates.DateFormatter("%m"))
            #     # ax.plot(ene_dct[item].index, ene_dct[item]["DENERGY"])
            #
            #     aux = ind_dct[item][col_item]
            #     ax.plot(aux.index, aux)
            #     # ax.plot(aux_tem.index, aux_tem)
            #
            #     ax2 = ax.twinx()
            #     ax2.plot(aux_ene.index, aux_ene)
            #     mm += 1
            plt.savefig('../images/'+item + "_" + str(pd.to_datetime(item, format="%Y-%m-%d").dayofyear))
            plt.close()

        return True

	'''
	Esta funcion realizar además de un plot el suaviado
	'''
    def doPlotDailySmoothEnergy (self,data,out_dct,labels):
		'''
		Aquí iría la implementación de la siguiente funcion....
		'''
        return True
