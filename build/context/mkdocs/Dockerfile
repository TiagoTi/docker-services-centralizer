FROM python:3.6
ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /docs && cd /docs && mkdocs new .  && chmod  777 /docs
WORKDIR /docs

EXPOSE 8000
ENTRYPOINT mkdocs serve
