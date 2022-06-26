==========================
Guide Start
==========================

The "Trees Everywhere" project objective to create a database of trees planted by
volunteers around the world.

https://trees-everywhere.herokuapp.com/

Steps
================================
1. Requirements
2. Deployment
3. Start


Requirements
================

Is recommended, use docker to run the project, it is not mandatory,you will 
need to install docker and docker-compose
  
    docker.io
    
    docker-compose

All you need to run the application is to have python and its package manager
    
    python3
    
    pip3


Deployment
================

deploy with docker:
  
    make build
  
deploy in local:
    
    make install


Start
================

If the deployment of the application happened as expected,
we can access it and create the superuser for the application.
  
  -docker
    http://localhost:8002/admin

    make createsuperuser_app

  -local
    http://localhost:8003/admin

    make createsuperuser

Code
================

https://github.com/HenriqueLR/trees-everywhere

https://trees-everywhere.herokuapp.com/



==========================
Version
==========================
.. include:: ../../VERSION
