FROM python:3.7-slim

RUN pip install flask

WORKDIR /app

COPY app.py /app/app.py

ENV ENVIRONMENT 'production'

ENTRYPOINT ["python"]

CMD ["/app/app.py"]


