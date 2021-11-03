FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app

COPY requirements.txt .

RUN mkdir -p /model

COPY /Users/stash/Desktop/model1.pkl /model

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "--host=0.0.0.0", "--port=80", "main:app"]