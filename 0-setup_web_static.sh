#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static.
sudo apt update -y
sudo apt install nginx -y
mkdir -p '/data/web_static/releases/test/'
mkdir -p '/data/web_static/shared/'
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > '/data/web_static/releases/test/index.html'
ln -sf '/data/web_static/releases/test/' '/data/web_static/current'
sudo chown -R ubuntu:ubuntu /data/
printf %s "server {
	listen 80 default_server;
	location /hbnb_static/ {
		alias /data/web_static/current/;
		index index.html;
	}
}" > etc/nginx/sites-enabled/default
sudo systemctl restart nginx
