#
# Minimal Docker image for a Django project
#
FROM python:3.6

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

# Install the PostgreSQL client
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    postgresql-client

# Set the default workdir
WORKDIR /app

COPY . /app/

RUN pip install -r /app/requirements.txt \
    && pip install -r /app/requirements-test.txt

RUN python manage.py makemigrations \
    && python manage.py migrate

