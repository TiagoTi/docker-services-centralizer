FROM ubuntu

RUN apt update && \
	apt install python3 python3-pip -y && \
	pip3 install pypiserver
RUN \
	mkdir -p /root/packages && \
	chmod -R 777 /root/packages
RUN apt install apache2-utils vim -y && \
	pip3 install htpasswd  && 	\
	echo 'admin:{SHA}0DPiKuNIrrVmD8IUCuw1hQxNqZc=' > /htpasswd.txt
CMD [ "bash"]

EXPOSE 8080