# Git
https://git.code.tecnalia.com/DigitalEnergy/platoon/platoon-visualisation-dashboard-wp-5/-/tree/pynaliaFront_V1.0
branch: pynaliaFront_V1.0

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

We can see api in http://localhost:8000/docs
And Pynalia Front End in http://localhost:4200/

We need to change the comunication between dockers but we dont know if you are using a traeffic
or something similar