FROM python:3.8

COPY reque.txt .

ADD app.py .

RUN pip install -r reque.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]