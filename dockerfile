FROM python:3.9-slim


RUN pip3 install flask


WORKDIR /app

COPY . /app


EXPOSE 5000

CMD ["python","-u", "app.py"]
