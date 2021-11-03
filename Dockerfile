FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "--host=0.0.0.0", "--port=8000", "main:app"]