FROM python:3.7
WORKDIR /app
COPY Pipfile .
RUN pip3 install pipenv
RUN pipenv install
COPY ./learningdjangowithppop .
CMD  ["pipenv","run","python","manage.py","runserver", "0.0.0.0:8000"]

