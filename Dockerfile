FROM python:3.10
ADD . /code
WORKDIR /code

# Only download and install GLPK if the tarball doesn't exist
RUN if [ -f "/code/data/glpk-5.0" ]; then \
      echo "GLPK found, skipping installation"; \
    else \
      pip install --upgrade pip; \
      pip install pyomo; \
      wget https://ftp.gnu.org/gnu/glpk/glpk-5.0.tar.gz -P /code/data; \
      tar -xzvf glpk-5.0.tar.gz; -C /code/data; \
      cd glpk-5.0; \
      ./configure; \
      make install; \
      apt-get update && apt-get install -y glpk-utils; \
    fi

WORKDIR /code

COPY . .

# RUN pip install --upgrade pip
# RUN pip install pyomo
# RUN wget https://ftp.gnu.org/gnu/glpk/glpk-5.0.tar.gz
# RUN tar -xzvf glpk-5.0.tar.gz

# WORKDIR /code/glpk-5.0

# RUN bash -c 'ls'
# RUN ./configure
# RUN make install
# RUN apt-get update && apt-get install -y glpk-utils

# WORKDIR /code