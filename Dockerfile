FROM continuumio/miniconda:latest

COPY . .

RUN conda env create -f environment.yml

RUN echo "source activate env" > ~/.bashrc

ENV PATH /opt/conda/envs/env/bin:$PATH

EXPOSE 5006

WORKDIR /weather_reporter

#CMD ["python", "app.py"]
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5006", "app:app"]