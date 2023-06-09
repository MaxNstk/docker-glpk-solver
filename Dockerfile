FROM python:3.10
ADD . /code
WORKDIR /code

# Only upgrade pip and install pyomo if necessary
RUN if [ ! -f "glpk-5.0.tar.gz" ]; then \
      pip install --upgrade pip; \
      pip install pyomo; \
    fi

# Only download and install GLPK if the tarball doesn't exist
RUN if [ -f "glpk-5.0.tar.gz" ]; then \
      echo "GLPK found, skipping installation"; \
    else \
      wget https://ftp.gnu.org/gnu/glpk/glpk-5.0.tar.gz; \
      tar -xzvf glpk-5.0.tar.gz; \
      cd glpk-5.0; \
      ./configure; \
      make install; \
      apt-get update && apt-get install -y glpk-utils; \
    fi

WORKDIR /code
COPY . .
