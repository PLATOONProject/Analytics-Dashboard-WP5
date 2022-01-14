from typing import List

import uvicorn

from bokeh.embed import file_html
from bokeh.layouts import layout
from bokeh.resources import CDN
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pandas import read_pickle
from fastapi.responses import HTMLResponse

from plots import time_lines, time_range_tool, time_lines_and_dots, scatter, time_scatter, time_bars

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
app.templates = Jinja2Templates(directory=".")
app.plotsHtml = None
app.xpan = False
app.scatter = False
app.plots = False


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
    app.scatter = False
    app.plots = False

    for plot in plot_list:
        print(plot)
        #  Try to convert list to PlotArray
        if plot['name'] == 'lines':
            if plot_list.index(plot) != 0:
                p = time_lines(obj=data_cds[plot['params']], xrange=p.x_range, **p_params)
            else:
                p = time_lines(obj=data_cds[plot['params']], **p_params)
            p_lines.append(p)
            app.plots = True
        elif plot['name'] == 'timescatter':
            if plot_list.index(plot) != 0:
                p = time_scatter(obj=data_cds[plot['params']], xrange=p.x_range, **p_params)
            else:
                p = time_scatter(obj=data_cds[plot['params']], **p_params)
            p_lines.append(p)
            app.plots = True
        elif plot['name'] == 'bars':
            if plot_list.index(plot) != 0:
                p = time_bars(obj=data_cds[plot['params']], xrange=p.x_range, **p_params)
            else:
                p = time_bars(obj=data_cds[plot['params']], **p_params)
            p_lines.append(p)
            app.plots = True
        elif plot['name'] == 'scatter':
            c = scatter(data_cds, title=f'Scatter',
                        xvar=plot['params'].split(',')[0].strip(),
                        yvar=plot['params'].split(',')[1].strip(), **sc_param)
            app.scatter = True
        elif plot['name'] == 'xpan':
            app.xpan = plot['params']

    if app.plots and app.xpan:
        xpan = time_range_tool(obj=data_cds, yvar=data_cds.columns[0],
                               xrange=p.x_range, width=p_params['width'])

    print(app.plots)
    print(app.xpan)
    print(app.scatter)
    # Visualization
    if app.plots:
        if app.scatter:
            if app.xpan:
                app.plotsHtml = file_html(layout([layout(p_lines), xpan, c]), CDN, "Dashboards")
            else:
                app.plotsHtml = file_html(layout([layout(p_lines), c]), CDN, "Dashboards")
        else:
            if app.xpan:
                app.plotsHtml = file_html(layout([layout(p_lines), xpan]), CDN, "Dashboards")
            else:
                app.plotsHtml = file_html(layout(p_lines), CDN, "Dashboards")
    else:
        if app.scatter:
            app.plotsHtml = file_html(c, CDN, "Dashboards")


@app.get("/showPlot")
async def showplot():
    html = app.plotsHtml
    app.plotsHtml = None
    return HTMLResponse(content=html, status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
