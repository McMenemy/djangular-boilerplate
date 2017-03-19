FROM python:2.7

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
