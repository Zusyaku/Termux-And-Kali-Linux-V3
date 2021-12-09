FROM alpine:latest
MAINTAINER Sandesh Yadav <sandeshyadavm46@gmail.com>

RUN apk --no-cache --no-progress add openrc nginx tor torsocks &&\
    openrc default &&\
    rc-update add nginx default &&\
    rc-update add tor default &&\
    rm /etc/nginx/http.d/default.conf &&\
    mkdir /var/www/hidden_service /etc/boot-container

COPY configs/torrc /etc/tor
COPY configs/nginx.conf /etc/nginx/http.d
COPY html/index.html /var/www/hidden_service
COPY scripts/torhost.sh /etc/profile.d
COPY scripts/bootstrap.sh /etc/boot-container

HEALTHCHECK  --interval=4m --timeout=50s --retries=2 \
  CMD torsocks wget --no-verbose --tries=1 --spider `cat /var/lib/tor/hidden_service/hostname` || exit 1

ENTRYPOINT ["sh","/etc/boot-container/bootstrap.sh"]
