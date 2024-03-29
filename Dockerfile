FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN python --version  >"log.txt"
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python ./index.py
