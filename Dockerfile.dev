FROM python:3.9.13

RUN mkdir -p /home/app

COPY . /home/app

EXPOSE 8000

CMD ["uvicorn", "/home/app/app:app", "--host", "0.0.0.0", "--port", "8000"]

