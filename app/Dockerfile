FROM python:slim

RUN pip3 install flask, redis

ADD flaskapp.py .
ADD test_base.py .

EXPOSE 80

CMD python3 flaskapp.py