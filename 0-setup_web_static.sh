#!/usr/bin/env bash
# Sets up web servers for the deployment of web static

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary folders
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/releases/test 
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html

# Create test HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
  </html>" | sudo tee /data/web_static/releases/test/index.html

# Recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="/etc/nginx/sites-enabled/default"
nginx_alias="location /hbnb_static {\n\talias /data/web_static/current/;\n}"

sudo sed -i "/listen 80 default_server/a $nginx_alias"  "$nginx_config"

# Restart Nginx
sudo service nginx restart

exit 0
