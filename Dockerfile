FROM python:3
ENV PYTHONUNBUFFERED=1 APIKEY=98T1QXD61MMBHC3I
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/