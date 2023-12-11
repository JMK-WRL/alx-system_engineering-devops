# Web Stack Debugging 1

This repository contains solutions to debugging tasks related to web stack configuration using Nginx. The tasks involve troubleshooting and fixing issues to ensure Nginx is running and listening on port 80.

## Task 0: Nginx Likes Port 80

### Problem
The Nginx installation in an Ubuntu container is not listening on port 80. The task requires identifying and fixing the issue using debugging skills.

### Solution
A Bash script (`0-nginx_likes_port_80`) is provided to automate the fix. It ensures that Nginx is running and listening on port 80 for all active IPv4 IPs.

```bash
./0-nginx_likes_port_80 > /dev/null 2>&1

