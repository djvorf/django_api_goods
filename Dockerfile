FROM python:3.9
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /goods_api
COPY requirements /goods_api/requirements
RUN pip install -r requirements/prod.txt
COPY . /goods_api/
CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000