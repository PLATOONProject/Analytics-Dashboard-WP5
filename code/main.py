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
app.templates = Jinja2Templates(directory=".")
app.scatterHtml = None
app.plotsHtml = None

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
        print(plot)
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
        elif plot['name'] == 'xpan':
            print(plot['params'])
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
                        xvar=plot['params'].split(',')[0].strip(),
                        yvar=plot['params'].split(',')[1].strip(), **sc_param)
            # Show scatter
            app.scatterHtml = file_html(c, CDN, "scatter")
            #output_file(f"Scatter_cds_{userid}.html")
            #save(c)

    xpan = time_range_tool(obj=data_cds, yvar=data_cds.columns[0],
                           xrange=p.x_range, width=p_params['width'])
    # Show plots
    #output_file(f"TimeLines_cds_{userid}.html")
    #save(layout([layout(p_lines), xpan]))
    app.plotsHtml = file_html(layout([layout(p_lines), xpan]), CDN, "plots")

@app.get("/showPlot")
async def showplot(request: Request):
    return HTMLResponse(content=app.plotsHtml, status_code=200)

@app.get("/showScatter")
async def showscatter():
    #try:
        #return templates.TemplateResponse('Scatter_cds_'+str(userid)+'.html', context={'request': request})
    return HTMLResponse(content=app.scatterHtml, status_code=200)
    #except TemplateNotFound:
    #    print
    #    'TemplateNotFound error in showScatter'
    #    return 'Scatter Not Found'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
