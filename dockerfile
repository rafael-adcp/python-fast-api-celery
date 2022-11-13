
FROM python:3.9-slim-buster

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
#   # psycopg2 dependencies
#   && apt-get install -y libpq-dev \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# the SED command process the line endings of the shell scripts, which converts Windows line endings to UNIX line endings.

#copying the different service start shell scripts to the root directory of the final image.

#COPY ./app/entrypoint.sh /entrypoint.sh
COPY ./app /app
RUN chmod +x app/entrypoint.sh

WORKDIR /app

USER nobody