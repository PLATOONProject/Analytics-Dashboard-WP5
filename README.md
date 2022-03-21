
# PLATOON Batch Data Visualisation Dashboard

Open-source dashboard that provides a collection of reusable  templates for batch data visualisation that can be easily integrated into customer-oriented cloud-based dashboard for predictive analytics and insights analysis. 
Tis tool has been funded by the PLATOON H2020 project funded by the EU commission.

## 1. Purpose

The Visualisation Dashbord is coded in Python and Angular and makes use of existing open source libraries .
The visualisation dashboard includes different type of charts based on the Generic Visualisation Toolbox developed in task T4.6. 
The target user of the tool are energy experts with high domain knowledge but low coding skills. Thus, an intuitive and simple Graphical User Interface (GUI) has been defined in order to configure and visualize the dashboards.  


## 2. Software and Hardware prerequisites

Being a web application, we have to take into account that the requirements are divided into client and server.
On the client side, the requirements are those set by the angular itself. Angular supports most recent browsers. This includes the following specific versions:

Browser Supported versions:
Chrome	latest
Firefox	latest and extended support release (ESR)
Edge	2 most recent major versions
Safari	2 most recent major versions
iOS	2 most recent major versions
Android	2 most recent major versions

In the server part, everything will be deployed in Docker Swarm, with which the requirements part is delegated to it. Docker Swarm is an orchestration management tool that runs on Docker applications. It helps end-users in creating and deploying a cluster of Docker nodes. Each node of a Docker Swarm is a Docker daemon, and all Docker daemons interact using the Docker API.

Regarding the hardware requirements:
•	Minimum hardware: 4 core / 8 GB RAM / 200 GB hard disk for three nodes.
•	Recommended hardware: 8 core / 16 GB RAM / 200 GB hard disk for three nodes.
•	Optional hardware: 8 core+ / 16 GB RAM+ / 200 GB+ hard disk for six nodes.


## 3. Repository Structure

The developed dashboard is formed of 3 main components:
1.	Generic Visualisation Tools
2.	API service
3.	Graphical User interface.
All the different components have been integrated into separate dockers. A FAST API service has been built on top to allow Graphical User Interface to interact with the Generic Visualization Tools.  This provides the required elasticity and flexibility to customize different type of dashboards and be able to scale them according to the user needs.

2 separate modules have been generated. On the one hand, a module containing the Python code with the Generic Visualisation Tools and the API wrapper. On the other hand the module with the Angular front-end (GUI).
Each module has its Dockerfile and later inside the “dev-ops” folder there is a docker-compose for the integration of both.
The module containing the Python code with the Generic Visualisation Tools and the API wrapper has been dockerized with the following Dockerfile:
# Pull base image
FROM python:3.6
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
 
RUN pip install --upgrade pip
WORKDIR /code/
# Install dependencies
COPY code/ ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
 
EXPOSE 8000
CMD ["python", "main.py"]

The module with the Angular front-end (GUI)  has been dockerized with the following Dockerfile:
# Nodejs Base image
FROM node
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
# install and app dependencies
COPY pynalia-front/ ./
RUN npm install
RUN npm install -g @angular/cli
# start app
CMD ng serve --host 0.0.0.0

To execute this project, we will launch a docker-compose with the following instruction:
docker-compose -f dev-ops/docker-compose.yml up -d –build

Once this instruction is executed there will have the 2 dockers uploaded in the following paths:
•	FastApi --> http://localhost:8000/docs
•	Front End --> http://localhost:4200/

The Front End communicates with the FastApi thrugh an environment variable found in 
```
/pynalia-front/src/environments/environment.ts
```

The data between these two modules is exchange through a JSON file that meets the following schema:

```
{
"$schema": "http://json-schema.org/draft-04/schema#",
"type": "object",
"properties": {
"column_name1": {
"type": "object",
"properties": {
"1498867200000": {
"type": "number"
},
"1498870800000": {
"type": "number"
},
............
},
"required": [
"1498867200000",
"1498870800000",
............
]
},
"column_name2": {
"type": "object",
"properties": {
"1498867200000": {
"type": "number"
},
"1498870800000": {
"type": "number"
},
............
},
"required": [
"1498867200000",
"1498870800000",
............
]
},
"column_name3": {
"type": "object",
"properties": {
"1498867200000": {
"type": "number"
},
"1498870800000": {
"type": "number"
},
............
},
"required": [
"1498867200000",
"1498870800000",
............
]
}
},
"required": [
"column_name1",
"column_name2",
"column_name3"
]
}
```
An example of the JSON file is shown below:
{
    "Variable1": {
        "TimeStamp": Value,
        " TimeStamp": Value,
        " TimeStamp ": Value,
    },
    " Variable2": {
        "TimeStamp": Value,
        "TimeStamp": Value,
        "TimeStamp ": Value
    },
    " VariableN": {
        "TimeStamp": Value,
        "TimeStamp": Value,
        "TimeStamp ": Value
    }
}

In addition, a sample JSON file can be found in the "data" folder.

## 4 Built With

* [Bokeh](https://github.com/bokeh/bokeh)
* [Itertools](https://github.com/rust-itertools/itertools)
* [Logging](https://pypi.org/project/logging)
* [Numpy] (https://github.com/numpy/numpy)
* [Pandas] (https://github.com/pandas-dev/pandas)
* [Typping] (https://github.com/python/typing)
* [FastApi] (https://github.com/tiangolo/fastapi)
* [Angular] (https://github.com/angular)


## 5 License

Licensed under the Apache 2.0. See LICENSE.txt for more details. For respective licenses of individual components and libraries please refer to section 4.

## 6 More information
More technical information regarding the developed dashboard is provided in the public deliverable "D5.4-Energy Analytics dashboard for business analysts"