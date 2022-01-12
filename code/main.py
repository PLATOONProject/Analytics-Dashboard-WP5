from typing import List

import uvicorn
from bokeh.layouts import layout
from bokeh.plotting import output_file, save
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pandas import read_pickle

from plots import time_lines, time_range_tool, time_lines_and_dots, time_scatter, scatter

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


# Python3 code here for creating class
class Plot:
    def __init__(self, name, params):
        self.name = name
        self.params = params


@app.post("/generate")
async def generate(plot_list: List):
    # We need list with selected plots with their parameters
    print(f'Starting post')
    # print(plots)
    # plot_list = [Plot(*plot) for plot in plots]
    # plot_list = [Plot('time_lines', '2m_temperature'), Plot('time_lines', 'snowfall'),
    #             Plot('time_lines', 'clear_sky_direct_solar_radiation_at_surface')]
    # get data from CDS
    try:
        # data_cds = read_pickle("./code/meteo_cds.pkl")
        data_cds = read_pickle("meteo_cds.pkl")
        data_cds = data_cds.dropna()
    except FileNotFoundError:
        print(f'File does not exist. ')

    # Example of time_lines
    p_lines = []
    p_params = dict(width=1200, height=250)
    sc_param = dict(size=5, width=700, height=700, hist_axes=True,
                    get_regression=False, hoover=True)
    for plot in plot_list:
        # switch
        if plot['name'] == 'lines':
            # Try to convert list to PlotArray
            if plot_list.index(plot) != 0:
                p = time_lines(obj=data_cds[plot['params']], xrange=p.x_range, **p_params)
            else:
                p = time_lines(obj=data_cds[plot['params']], **p_params)
            p_lines.append(p)
        elif plot['name'] == 'dots':
            # Try to convert list to PlotArray
            if plot_list.index(plot) != 0:
                p = time_lines_and_dots(obj=data_cds[plot['params']], xrange=p.x_range, **p_params)
            else:
                p = time_lines_and_dots(obj=data_cds[plot['params']], **p_params)
            p_lines.append(p)
        elif plot['name'] == 'scatter':
            # Try to convert list to PlotArray
            #if plot_list.index(plot) != 0:
            #    p = time_scatter(obj=data_cds[plot['params']], xrange=p.x_range, **p_params)
            #else:
            #    p = time_scatter(obj=data_cds[plot['params']], **p_params)
            #p = scatter(data_cds, title=f'Figure example {NAME_DEMO}',
            #            xvar='clear_sky_direct_solar_radiation_at_surface',
            #            yvar='2m_temperature', **sc_param)
            c = scatter(data_cds, title=f'Scatter',
                        xvar=plot['params'].split(',')[0],
                        yvar=plot['params'].split(',')[1], **sc_param)
            # Show scatter
            output_file(f"Scatter_cds.html")
            save(c)

    xpan = time_range_tool(obj=data_cds, yvar=data_cds.columns[0],
                           xrange=p.x_range, width=p_params['width'])
    # Show plots
    output_file(f"TimeLines_cds.html")
    save(layout([layout(p_lines), xpan]))



@app.get("/showPlot")
async def home(request: Request):
    return templates.TemplateResponse('TimeLines_cds.html', context={'request': request})

@app.get("/showScatter")
async def home(request: Request):
    return templates.TemplateResponse('Scatter_cds.html', context={'request': request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
