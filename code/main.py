import json
import uvicorn
import pandas as pd
from urllib import request
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Dict, Iterable, Tuple, Union, Sequence, List
from pandas import notnull, DataFrame, Series

from pandas import read_pickle
from plots import time_lines, scatter, time_range_tool
from bokeh.plotting import output_file, show, figure, save
from bokeh.layouts import layout, row

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory=".")

@app.get("/time_lines")
async def get_time_lines(request: Request):
    """Creates a time series scatter plot.

    :param obj: input data.
    :param yvar: columns names in data to plot in the y axis.
    :param xvar: column or index name to plot in the x axis. Default None. If None the index
                will plot on the x axis.
    :param xrange: x range in the format (min, max) or bokeh.figure.x_range. Default None.
                If None the x axis shows the first 1/10 of the x variable data.
    :param yrange: y range in the format (min, max). If None the default y axis range is shown.
    :param groupby: name of column to used to group the data. If None data is not grouped.
    :param highlight: columns names of variables in the y axis to be ploted with a thicker line.
    :param line_width: width of lines.
    :param color: color of line.
    :param color_palette: palette of color as list of HEX codes to use in case of more than one
            group of data or variable per plot. Default None. In None, a comination of brewer
            palettes is used.
    :param height: height of plot in pixels. Default 400.
    :param width: width of plot in pixels. Default 1600.
    :param legend_location: legend location.
    :param title: title of plot. Default None. If None the title is a list of the names of the
                variables plotted in the y axis.
    :param toolbar: tools to include in the tool bar.
    :param hoover: include a hoover tool. Default True.
    :param hoover_tips: variables to include in the hoover tool. Default None. If None the
                hoover tool shows the y axis value. v.g. [('label', '@column_name')]
    :return: bokeh figure.
    :author: miguel.esteras@tecnalia.com
    """
    print(f'Starting ')
    variables = ['2m_temperature', 'snowfall',
                 'clear_sky_direct_solar_radiation_at_surface']

    # get data from CDS
    try:
        #data_cds = read_pickle("./code/meteo_cds.pkl")
        data_cds = read_pickle("meteo_cds.pkl")
        data_cds = data_cds.dropna()
    except FileNotFoundError:
        print(f'File does not exist. ')

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
    output_file(f"TimeLines_cds.html")
    show(layout([layout(p_lines), xpan]))

    # Example of scatter
    print("time_lines")
    return templates.TemplateResponse('TimeLines_cds.html', context={'request': request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
