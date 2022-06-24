FROM henriquelr89/ubuntu-versions:20.04
MAINTAINER henrique.lr89@gmail.com

RUN mkdir -p /deploy/apps/trees-everywhere/
ADD . /deploy/apps/trees-everywhere/

WORKDIR /deploy/apps/trees-everywhere
RUN ./env/app/install.sh
COPY ./env/app/entrypoint.sh /deploy/apps/trees-everywhere

RUN chown -R treeseverywhere:treeseverywhere /deploy/apps/trees-everywhere/

USER treeseverywhere

ENTRYPOINT ["sh", "/deploy/apps/trees-everywhere/env/app/entrypoint.sh"]
