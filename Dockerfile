FROM python:3-alpine
MAINTAINER SHIVASHANKERPANDIRI
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","app.py"]
