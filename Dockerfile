FROM python:3.7-bullseye

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

ADD . /app

# install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt
    # OR
## RUN pip3 install -r requirements.txt

# copy project
COPY . /app

# -----------------------FOR LOCAL------------------------
# CMD gunicorn HiTalent.wsgi:application --bind 0.0.0.0:8000

# OR

EXPOSE 8000

CMD = ["gunicorn","--bind",":8000","--workers","3","payment_wallet.wsgi:application"]

# --------------------HEROKU Server-------------------

# CMD gunicorn HiTalent.wsgi:application --bind 0.0.0.0:$PORT