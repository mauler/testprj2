FROM python:3.6

ENV APP_DIR /usr/src/app

RUN mkdir -pv ${APP_DIR}

WORKDIR ${APP_DIR}

ADD . ${APP_DIR}

RUN pip install -r requirements/production.txt

RUN python setup.py install

RUN rm -rfv ${APP_DIR}/* /src/

CMD task2-http-server
