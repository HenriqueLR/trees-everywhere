The "Trees Everywhere" project objective to create a database of trees planted by
volunteers around the world.

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

    make test
    
    Name                                  Stmts   Miss  Cover   Missing
    -------------------------------------------------------------------
    accounts/__init__.py                      0      0   100%
    accounts/admin.py                        35      3    91%   40, 44, 53
    accounts/apps.py                          4      0   100%
    accounts/decorators.py                    9      0   100%
    accounts/forms.py                        30     12    60%   18-24, 27-31, 44
    accounts/migrations/0001_initial.py       9      0   100%
    accounts/migrations/__init__.py           0      0   100%
    accounts/models.py                       82     24    71%   25, 38, 41-49, 52-61, 64-71, 100, 103, 107, 110, 113
    accounts/urls.py                          3      0   100%
    api/__init__.py                           0      0   100%
    api/apps.py                               4      0   100%
    api/migrations/__init__.py                0      0   100%
    api/serializers.py                       11      0   100%
    api/urls.py                               3      0   100%
    api/views.py                             11      0   100%
    conf/__init__.py                          0      0   100%
    conf/settings.py                         31      0   100%
    conf/urls.py                              4      0   100%
    manage.py                                12      2    83%   12-13
    tests/__init__.py                        53      0   100%
    tests/test_permissions.py                41      0   100%
    tests/test_urls.py                       36      0   100%
    tests/test_views.py                      36      0   100%
    trees/__init__.py                         0      0   100%
    trees/admin.py                           15      1    93%   19
    trees/apps.py                             4      0   100%
    trees/forms.py                           10      0   100%
    trees/migrations/0001_initial.py          7      0   100%
    trees/migrations/__init__.py              0      0   100%
    trees/models.py                          40      5    88%   23, 26, 30, 48, 51
    trees/permissions.py                     15      2    87%   21-22
    trees/urls.py                             3      0   100%
    trees/views.py                           53      0   100%
    -------------------------------------------------------------------
    TOTAL                                   561     49    91%


### Fun

  Access the application demo https://trees-everywhere.herokuapp.com/

    this test users are linked into equal accounts.
    
    email: test@test.com
    password: teste123456

    email: test2@test2.com
    password: teste123456

    email: test3@test3.com
    password: teste123456

  official documentation  https://trees-everywhere.readthedocs.io/en/latest/
