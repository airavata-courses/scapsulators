FROM continuumio/miniconda:latest

COPY . .

RUN chmod +x boot.sh
RUN conda env create -f environment.yml

RUN echo "source activate env" > ~/.bashrc

ENV PATH /opt/conda/envs/env/bin:$PATH

EXPOSE 5000

ENTRYPOINT [ "./boot.sh" ]