FROM jenkins:1.609.3

USER root
RUN echo "deb http://apt.dockerproject.org/repo debian-jessie main" /etc/apt/sources.list.d/docker.list 
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyserver.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D 
RUN apt-get update 
RUN apt-get install -y apt-transport-https 
RUN apt-get install -y 
RUN apt-get install -y docker-engine 
RUN rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
RUN curl -L https://github.com/docker/compose/releases/download/1.4.1/ \
docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose; \
chmod +x /usr/local/bin/docker-compose 
USER jenkins
COPY plugins.txt /usr/share/jenkins/plugins.txt 
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt