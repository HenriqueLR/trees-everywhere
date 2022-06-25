Trees-everywhere is a web application that objective to keep a record of planted trees, keeping information
such as, who planted the tree, location and other information.

### Requirements
  
  Is recommended, use docker to run the project, it is not mandatory,
  you will need to install docker and docker-compose
  
    docker.io
    docker-compose

  All you need to run the application is to have python and its package manager
    
    python3
    pip3

### Deployment

  deploy with docker:
  
    make build
  
  deploy in local:
    
    make install

### Start

  If the deployment of the application happened as expected,
  we can access it and create the superuser for the application.
  
  docker
    
    http://localhost:8002/
    http://localhost:8002/admin

    make createsuperuser_app

  local

    http://localhost:8003/
    http://localhost:8003/admin

    make createsuperuser

### Manual deployment in local

    pip install -r requirements.txt
    python app/manage.py makemigrations --settings=conf.settings
    python app/manage.py migrate --settings=conf.settings
    python app/manage.py collectstatic --no-input
    python app/manage.py createsuperuser
    python app/manage.py runserver 0.0.0.0:8003 --settings=conf.settings

    http://localhost:8003/

### Run Tests

    make tests

### Fun

  Access the application demo
  
    https://trees-everywhere.herokuapp.com/
    email: teste@teste.com
    password: teste123456

    email: teste2@teste2.com
    password: teste123456

  official documentation
    
    https://tree-everywhere.readthedocs.io/en/latest/
