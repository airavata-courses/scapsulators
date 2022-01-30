FROM continuumio/anaconda:latest

COPY . .

#RUN chmod +x boot.sh
RUN conda env create -f environment.yml

RUN echo "source activate env" > ~/.bashrc

ENV PATH /opt/conda/envs/env/bin:$PATH

EXPOSE 5000

#ENTRYPOINT [ "./boot.sh" ]

WORKDIR /radar_stations_fetcher

#CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "app:app"]
CMD ["python", "app.py"]