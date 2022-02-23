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
