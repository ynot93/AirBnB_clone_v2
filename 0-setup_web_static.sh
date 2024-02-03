#!/usr/bin/env bash
# Sets up web servers for the deployment of web static

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo chown -R ubuntu:ubuntu /data/

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

# Update Nginx configuration
nginx_config="/etc/nginx/sites-enabled/default"
nginx_alias="location /hbnb_static {\n\talias /data/web_static/current/;\n}\n"
sudo sed -i "37i $nginx_alias" "$nginx_config"

# Restart Nginx
sudo service nginx restart

exit 0
