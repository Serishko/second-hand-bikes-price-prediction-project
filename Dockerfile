FROM python:3
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python webdevelopment_using_django/manage.py runserver 0.0.0.0:8000
