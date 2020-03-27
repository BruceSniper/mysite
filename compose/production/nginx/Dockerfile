FROM nginx:1.16.1

RUN apt-get update && apt-get install -y gnupg2

RUN apt-get update && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 40976EAF437D05B5
RUN apt-get update && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32
# 替换为国内源
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY ./compose/production/nginx/sources.list /etc/apt/

#RUN apt-get update && apt-get install gpgv
#RUN apt-get update && apt-get install gnupg2
#RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 40976EAF437D05B5
#RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 3B4FE6ACC0B21F32
#RUN gpg --keyserver keyring.debian.org --recv-keys 40976EAF437D05B5
#RUN gpg --armor --export 40976EAF437D05B5 | apt-key add -



RUN apt-get update && apt-get install -y --allow-unauthenticated certbot python-certbot-nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY ./compose/production/nginx/mysite.conf /etc/nginx/conf.d/mysite.conf