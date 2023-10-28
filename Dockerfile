FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

RUN python -m nltk.downloader vader_lexicon

COPY ./src /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]