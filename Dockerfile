FROM python:3.8

ADD . /code
WORKDIR /code

# COPY  glpk-5.0.tar.gz glpk-5.0.tar.gz
# COPY  glpk-5.0.tar.gz.sig glpk-5.0.tar.gz.sig

RUN pip install --upgrade pip
RUN pip install pyomo
RUN wget https://ftp.gnu.org/gnu/glpk/glpk-4.65.tar.gz
RUN tar -xzvf glpk-4.65.tar.gz

WORKDIR /code/glpk-4.65

RUN bash -c 'ls'
RUN ./configure
RUN make install

WORKDIR /code

# CMD ["python", "investidor.py"]

# RUN wget https://ftp.gnu.org/gnu/glpk/glpk-4.65.tar.gz.sig

# RUN gpg --verify glpk-4.65.tar.gz.sig glpk-4.65.tar.gz
# RUN gpg --keyserver keys.gnupg.net --recv-keys 5981E818

# RUN tar -xzvf glpk-4.65.tar.gz
# RUN 
# CMD ["./configure", "--enable-dl", "--enable-odbc"]
# RUN ./configure --disable-shared
# RUN make --jobs=4
# RUN make check
# RUN make install
# RUN make install

# RUN python .\main.py
# RUN apt-get update && apt-get install glpk && apt-get install glpk-utils libglpk-dev glpk-doc python-glpk


# RUN tar -xvzf glpk-5.0.tar.gz

# RUN gpg --keyserver keys.gnupg.net --recv-keys 5981E818
# RUN gpg --verify glpk-5.0.tar.gz.sig



