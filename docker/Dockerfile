FROM mysql:5.7.24

ENV GOROOT /data/env/go
ENV WEB /data/release/web/
ENV GOPATH /data/release/web
ENV PATH ${WEB}:$GOROOT/bin:$PATH
ENV MYSQL_ROOT_PASSWORD "123456"

ADD sources.list  /etc/apt/sources.list

###
# 基础安装
RUN apt-get update \
    && apt-get install -y --allow-unauthenticated curl wget gcc g++ make git vim tar 

###
# go 环境安装
RUN mkdir /data/env/go -p \
    mkdir /data/release/web/conf -p \
    && cd /data/env/go/ \
    && wget http://10.26.22.185:9000/psop/soft/go1.11.2.linux-amd64.tar.gz \
    && tar -zxf go1.11.2.linux-amd64.tar.gz \
    && rm ./*.tar.gz \
    && mv ./go/* ./ \
    && rm -fr ./go/ 

COPY go/conf /data/release/web/conf
COPY go/main /data/release/web/main
 
###
# 复制源码
RUN cd $WEB \
    && main > /dev/null

CMD ["mysqld"]

