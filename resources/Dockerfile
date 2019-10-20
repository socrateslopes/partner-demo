FROM python:3.7-stretch

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

ENV WEB_CONCURRENCY 4

CMD ["gunicorn","--pythonpath","src","--timeout","120","--graceful-timeout","120","--bind","0.0.0.0:5000","--worker-class","gevent","application:app"]

COPY . /usr/src/app
