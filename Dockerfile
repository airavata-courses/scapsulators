FROM python:3.9-alpine

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5016

WORKDIR /satellite_view_reporter

#CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "app:app"]
CMD ["python", "app.py"]