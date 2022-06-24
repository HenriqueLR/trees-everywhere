#!/bin/sh

cp /deploy/apps/trees-everywhere/env/nginx/default /etc/nginx/sites-enabled/default

exec nginx -g 'daemon off;' "$@"
