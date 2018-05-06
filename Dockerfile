 FROM python:3
 ENV PYTHONUNBUFFERED 1
 WORKDIR /data/tpp_brutus
 ADD ./requirements.txt /data/tpp_brutus/
 RUN pip3 install -r requirements.txt
 ADD . /data/tpp_brutus/
