FROM python:3.6.4
RUN pip install --upgrade pip
RUN pip install jupyter
EXPOSE 8888

RUN groupadd -r jupyter && useradd --no-log-init -r -g jupyter jupyter
RUN mkdir -p /home/jupyter/nootebook && chown jupyter -R /home/jupyter
WORKDIR /home/jupyter
USER jupyter
CMD [ "jupyter", "notebook" ,"--ip='0.0.0.0'", "--port=8888", "--notebook-dir=/home/jupyter/nootebook"]


