FROM nginx
EXPOSE 80
COPY index.html /usr/share/nginx/html/index.html
# The custom nginx config file is used to forward api requests to the backend.
# The internal service address and port is hardcoded into nginx.conf.
# Not necessarily good practice for a real system.
COPY nginx.conf /etc/nginx/conf.d/default.conf
