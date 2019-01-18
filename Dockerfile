FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements
EXPOSE 80
ENV AWS_SECRET_ACCESS_KEY lies
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
