# Git
```
https://git.code.tecnalia.com/DigitalEnergy/platoon/platoon-visualisation-dashboard-wp-5/-/tree/pynaliaFront_V1.0
branch: pynaliaFront_V1.0
```

# Pynalia
In this project 2 separate modules have been generated. 
On the one hand a Python API to wrap the Pynalia code and 
on the other a front-end to interact with said API

Each module has its Dockerfile and later inside the dev-ops folder 
there is a docker-compose for the integration of both 

To execute this project we will launch said docker-compose with the instruction

```
docker-compose -f dev-ops/docker-compose.yml up -d --build
```

Now we will have 2 dockers upload.

FastApi --> http://localhost:8000/docs

Front End --> http://localhost:4200/

In the second endpoint you only have to select you json and select the dashboards you want to see.
In the data folder there are 2 json with which the tests have been carried out.
We'll need to change the communication between the dockers, but we don't know if you're using a traeffic 
or something similar. 
Our frontend communicates with the api thanks to an environment variable found in 
```
/pynalia-front/src/environments/environment.ts
```

Here I leave a schema of how the received json should be

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
