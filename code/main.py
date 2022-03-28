from typing import List

import uvicorn
import pandas as pd
from urllib.request import urlopen
from bokeh.embed import file_html
from bokeh.layouts import layout
from bokeh.resources import CDN
from fastapi import FastAPI, File, UploadFile
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from plots import time_lines, time_range_tool, scatter, time_scatter, time_bars, histograms, correlation, heatmap

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)

app.templates = Jinja2Templates(directory=".")
app.plotsHtml = None
app.xpan = False
app.scatter = False
app.correlation = False
app. histogram = False
app.plots = False
app.bytes_data = None
app.firstPlotWithXRange = False


class Dashboard(BaseModel):
    name: str
    params: str


class Dashboards(BaseModel):
    file_path: str
    selectedDashboards: List[Dashboard]


@app.post("/generate")
async def generate(dashboards: Dashboards):
    # We need list with selected plots with their parameters
    print(f'Starting post')
    try:
        # data_cds = read_pickle("/home/zarateadm/git/meteo_cds.pkl")
        # data_cds = read_pickle("meteo_cds.pkl")
        # data_cds = pd.read_json(file_path)
        # data_cds = pd.read_json(dashboards.file_path)

        # With thumbnail
        # print(app.bytes_data)
        # s = str(app.bytes_data, 'utf-8')
        # data = StringIO(s)
        # data_cds = pd.read_json(data)

        print(dashboards.file_path)
        # store the response of URL
        response = urlopen(dashboards.file_path)

        # storing the JSON response
        # from url in data. Default return DataFrame
        data_cds = pd.read_json(response)
        # Remove missing values.
        data_cds = data_cds.dropna()
    except FileNotFoundError:
        print(f'File does not exist. ')

    # Example of time_lines
    p_lines = []
    p_params = dict(width=1200, height=250)
    sc_param = dict(size=5, width=700, height=700, hist_axes=True,
                    get_regression=False, hoover=True)
    app.correlation = False
    app.scatter = False
    app.histogram = False
    app.plots = False
    app.firstPlotWithXRange = False
    plot_list = dashboards.selectedDashboards

    for plot in plot_list:
        #  Try to convert list to PlotArray
        if plot.name == 'lines':
            if app.firstPlotWithXRange:
                p = time_lines(obj=data_cds[plot.params], xrange=p.x_range, **p_params)
            else:
                p = time_lines(obj=data_cds[plot.params], **p_params)
                app.firstPlotWithXRange = True


            #def plot_blanks(df: DataFrame, title: str, width: int = 400, height: int = 800,
            #                palette: str = "Blues8",
            #                datetime_index: bool = True) -> figure:
            #p = plot_blanks(df=data_cds,title='plots', **p_params)

            #def plot_table(obj: Union[DataFrame, Series], column_names: List[str] = None,
            #               datetime_index: bool = True,
            #               height: int = 600, width: int = 1600, decimals: int = 2,
            #               title: str = None) -> figure:
            #p = plot_table(obj=data_cds)

            #p = lines(obj=data_cds[plot.params], **p_params)

            p_lines.append(p)
            print(p_lines)
            app.plots = True
        elif plot.name == 'dots':
            if app.firstPlotWithXRange:
                p = time_scatter(obj=data_cds[plot.params], xrange=p.x_range, **p_params)
            else:
                p = time_scatter(obj=data_cds[plot.params], **p_params)
                app.firstPlotWithXRange = True
            p_lines.append(p)
            app.plots = True
        elif plot.name == 'bars':
            if app.firstPlotWithXRange:
                p = time_bars(obj=data_cds, yvar=[plot.params], xrange=p.x_range, **p_params)
            else:
                p = time_bars(obj=data_cds, yvar=[plot.params], **p_params)
                app.firstPlotWithXRange = True
            p_lines.append(p)
            app.plots = True
        elif plot.name == 'heatmap':
            if app.firstPlotWithXRange:
                p = heatmap(obj=data_cds, xvar=plot.params, yvar=plot.params, value=plot.params, xrange=p.x_range, **p_params)
            else:
                p = heatmap(obj=data_cds, xvar=plot.params, yvar=plot.params, value=plot.params, **p_params)
                app.firstPlotWithXRange = True
            p_lines.append(p)
            app.plots = True
        elif plot.name == 'correlation':
            c = correlation(obj=data_cds, **p_params)
            app.correlation = True
        elif plot.name == 'histogram':
            h = histograms(obj=data_cds, **p_params, title='histogram')
            app.histogram = True
        elif plot.name == 'scatter':
            s = scatter(data_cds, title=f'Scatter',
                        xvar=plot.params.split(',')[0].strip(),
                        yvar=plot.params.split(',')[1].strip(), **sc_param)
            app.scatter = True
        elif plot.name == 'xpan':
            app.xpan = str_to_bool(plot.params)

    if app.plots and app.xpan:
        xpan = time_range_tool(obj=data_cds, yvar=data_cds.columns[0],
                               xrange=p.x_range, width=p_params['width'])

    # Visualization
    if app.plots and app.scatter and app.correlation and app.histogram:
        if app.xpan:
            app.plotsHtml = file_html(layout([layout(p_lines), xpan, c, s, h]), CDN, "Dashboards")
        else:
            app.plotsHtml = file_html(layout([layout(p_lines), c, s, h]), CDN, "Dashboards")
    elif app.plots and app.scatter and app.correlation:
        if app.xpan:
            app.plotsHtml = file_html(layout([layout(p_lines), xpan, c, s]), CDN, "Dashboards")
        else:
            app.plotsHtml = file_html(layout([layout(p_lines), c, s]), CDN, "Dashboards")
    elif app.plots and app.scatter and app.histogram:
        if app.xpan:
            app.plotsHtml = file_html(layout([layout(p_lines), xpan, s, h]), CDN, "Dashboards")
        else:
            app.plotsHtml = file_html(layout([layout(p_lines), s, h]), CDN, "Dashboards")
    elif app.plots and app.scatter:
        if app.xpan:
            app.plotsHtml = file_html(layout([layout(p_lines), xpan, s]), CDN, "Dashboards")
        else:
            app.plotsHtml = file_html(layout([layout(p_lines), s]), CDN, "Dashboards")
    elif app.plots and app.correlation and app.histogram:
        if app.xpan:
            app.plotsHtml = file_html(layout([layout(p_lines), xpan, c, h]), CDN, "Dashboards")
        else:
            app.plotsHtml = file_html(layout([layout(p_lines), c, h]), CDN, "Dashboards")
    elif app.plots and app.correlation:
        if app.xpan:
            app.plotsHtml = file_html(layout([layout(p_lines), xpan, c]), CDN, "Dashboards")
        else:
            app.plotsHtml = file_html(layout([layout(p_lines), c]), CDN, "Dashboards")
    elif app.plots and app.histogram:
        if app.xpan:
            app.plotsHtml = file_html(layout([layout(p_lines), xpan, h]), CDN, "Dashboards")
        else:
            app.plotsHtml = file_html(layout([layout(p_lines), h]), CDN, "Dashboards")
    elif app.plots:
        if app.xpan:
            app.plotsHtml = file_html(layout([layout(p_lines), xpan]), CDN, "Dashboards")
        else:
            app.plotsHtml = file_html(layout(p_lines), CDN, "Dashboards")
    elif app.scatter and app.correlation and app.histogram:
        app.plotsHtml = file_html(c, s, h, CDN, "Dashboards")
    elif app.scatter and app.correlation:
        app.plotsHtml = file_html(c, s, CDN, "Dashboards")
    elif app.scatter and app.histogram:
        app.plotsHtml = file_html(s, h, CDN, "Dashboards")
    elif app.correlation and app.histogram:
        app.plotsHtml = file_html(c, h, CDN, "Dashboards")
    elif app.scatter:
        app.plotsHtml = file_html(s, CDN, "Dashboards")
    elif app.histogram:
        app.plotsHtml = file_html(h, CDN, "Dashboards")
    elif app.correlation:
        app.plotsHtml = file_html(c, CDN, "Dashboards")

@app.post("/thumbnail-upload")
def create_file(thumbnail: UploadFile = File(...)):
    app.bytes_data = thumbnail.file.read()
    return {"file_size": len(thumbnail.file.read())}


@app.get("/showPlot")
async def showplot():
    html = app.plotsHtml
    app.plotsHtml = None
    return HTMLResponse(content=html, status_code=200)


def str_to_bool(s):
    if s == 'True':
        return True
    elif s == 'False':
        return False


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
