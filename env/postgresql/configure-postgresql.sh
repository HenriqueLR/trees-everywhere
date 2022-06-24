#!/bin/bash -xe

/etc/init.d/postgresql start
sudo -u postgres psql --command "CREATE USER treeseverywhere WITH SUPERUSER PASSWORD 'treeseverywhere';"
sudo -u postgres psql --command "CREATE DATABASE treeseverywhere;"
sudo -u postgres psql --command "GRANT ALL PRIVILEGES ON DATABASE treeseverywhere to treeseverywhere;"
sudo echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/12/main/pg_hba.conf \
&& echo "listen_addresses='*'" >> /etc/postgresql/12/main/postgresql.conf \
&& /etc/init.d/postgresql restart
