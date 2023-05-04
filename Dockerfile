FROM python:3.8
ADD . /code
WORKDIR /code

# Only upgrade pip and install pyomo if necessary
RUN if [ ! -f "glpk-4.65.tar.gz" ]; then \
      pip install --upgrade pip; \
      pip install pyomo; \
    fi

# Only download and install GLPK if the tarball doesn't exist
RUN if [ -f "glpk-4.65.tar.gz" ]; then \
      echo "GLPK found, skipping installation"; \
    else \
      wget https://ftp.gnu.org/gnu/glpk/glpk-4.65.tar.gz; \
      tar -xzvf glpk-4.65.tar.gz; \
      cd glpk-4.65; \
      ./configure; \
      make install; \
      apt-get update && apt-get install -y glpk-utils; \
    fi

WORKDIR /code
COPY . .

# RUN pip install --upgrade pip
# RUN pip install pyomo
# RUN wget https://ftp.gnu.org/gnu/glpk/glpk-4.65.tar.gz
# RUN tar -xzvf glpk-4.65.tar.gz

# WORKDIR /code/glpk-4.65

# RUN bash -c 'ls'
# RUN ./configure
# RUN make install
# RUN apt-get update && apt-get install -y glpk-utils

# WORKDIR /code