FROM python:3.8
WORKDIR /code
ADD . /code
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]