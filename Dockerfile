FROM docker.io/python:3.13-bookworm

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app/

ENTRYPOINT ["/usr/bin/env", "python3"]
CMD ["app.py"]
