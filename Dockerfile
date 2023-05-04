FROM python:3.8

ADD . /code
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install pyomo
RUN wget https://ftp.gnu.org/gnu/glpk/glpk-4.65.tar.gz
RUN tar -xzvf glpk-4.65.tar.gz

WORKDIR /code/glpk-4.65

RUN bash -c 'ls'
RUN ./configure
RUN make install
RUN apt-get update && apt-get install -y glpk-utils

WORKDIR /code