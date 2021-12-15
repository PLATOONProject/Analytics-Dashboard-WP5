# platoon_demo.py -> AUTHOR: Tecnalia Research and Innovation (Sandra Riaño and Miguel Esteras)

from plots import time_lines, scatter, time_range_tool
from bokeh.plotting import output_file, show, figure, save
from bokeh.layouts import layout, row
from pathlib import Path
import datetime
from datetime import timedelta
from pandas import read_pickle

NAME_DEMO = 'platoon_demo'

print(f'Starting {NAME_DEMO}')

# Read data
variables = ['2m_temperature', 'snowfall',
             'clear_sky_direct_solar_radiation_at_surface']
pklpath_cds = 'meteo_cds.pkl'

# get data from CDS
data_cds = read_pickle(pklpath_cds)

data_cds = data_cds.dropna()
        

# Example of time_lines
p_lines = []
p_params = dict(width=1200, height=250)
p = time_lines(obj=data_cds['2m_temperature'], **p_params)

p_lines.append(p)
p_lines.append(time_lines(obj=data_cds['snowfall'], xrange=p.x_range,
                          **p_params))
p_lines.append(time_lines(obj=data_cds['clear_sky_direct_solar_radiation_at_surface'],
                          xrange=p.x_range, **p_params))
xpan = time_range_tool(obj=data_cds, yvar=data_cds.columns[0],
                       xrange=p.x_range, width=p_params['width'])
output_file(f"{NAME_DEMO}_TimeLines_cds.html")
show(layout([layout(p_lines), xpan]))

# Example of scatter
sc_param = dict(size=5, width=700, height=700, hist_axes=True,
                get_regression=False, hoover=True)
p = scatter(data_cds, title=f'Figure example {NAME_DEMO}',
            xvar='clear_sky_direct_solar_radiation_at_surface',
            yvar='2m_temperature', **sc_param)
output_file(f"{NAME_DEMO}_Scatter_cds.html")
show(p)

print(f'Endind {NAME_DEMO}')
