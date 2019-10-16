FROM python:3.6.4

RUN adduser --system --disabled-password --gecos ""  --uid 1000 jupyter && \
    apt update -y && \
    apt install -y vim && \
    pip install --upgrade pip


WORKDIR /home/jupyter

USER jupyter

RUN pip3 install --user jupyter scikit-learn pandas plotly lime matplotlib seaborn && \
    mkdir notebooks && \
    mkdir -p /home/jupyter/.jupyter/

ADD bashrc.sh /home/jupyter/.bashrc
ADD jupyter_notebook_config.json /home/jupyter/.jupyter/jupyter_notebook_config.json

EXPOSE 8888

ENTRYPOINT ["/home/jupyter/.local/bin/jupyter", "notebook", "--ip=0.0.0.0", "--notebook-dir=/home/jupyter/notebooks", "--no-browser"]

