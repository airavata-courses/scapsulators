FROM python:3.9-alpine

RUN echo "machine urs.earthdata.nasa.gov login vikrant.deshpande098 password tokyo098#VIK098" > ~/.netrc

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5016

WORKDIR /satellite_view_reporter

#CMD ["python", "app.py"]
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5016", "app:app"]