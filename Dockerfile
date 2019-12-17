FROM python:3.7
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./learningdjangowithppop .
CMD  ["python","manage.py","runserver", "0.0.0.0:8000"]

