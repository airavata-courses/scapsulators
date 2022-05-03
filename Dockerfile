FROM python:slim

#RUN echo "machine urs.earthdata.nasa.gov login vikrant.deshpande098 password tokyo098#VIK098" > ~/.netrc
RUN pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple custos-sdk==1.0.18

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5005

WORKDIR /custos-testing-app

CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:5005", "app:app"]