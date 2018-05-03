 FROM python:3
 ENV PYTHONUNBUFFERED 1
 WORKDIR /data/tpp_bruto
 ADD ./requirements.txt /data/tpp_bruto/
 RUN pip3 install -r requirements.txt
 ADD . /data/tpp_bruto/
