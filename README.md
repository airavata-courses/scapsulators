# Scapsulators
Spring 2022 Project


# Radar-Stations Fetcher Service

## Functionality/Motivation

<ul>
<li>This standalone microservice is intended to fetch a neat <b>JSON data structure</b>, for mapping geographic-regions to individual radar-station codes maintained on <b>NEXRAD's S3 data-lake</b>.</li>
<li>This service is kept separate from the <b>weather-reporter</b> microservice since we don't want to keep the client waiting too long while media streaming over Kafka is in progress for the latter. Similarly this separate service will avoid a single-point of failure for accessing all NEXRAD data.</li>
</ul>

## Working

<ul>
<li>Radar-Stations Fetcher runs a <a href="https://github.com/NimzyMaina/flask_kafka/blob/master/flask_kafka/consumer.py">FlaskKafka</a> thread to constantly listen for incoming Kafka messages over the topic <b><i>REQUEST_STATIONS</i></b>.The message content doesn't matter for now, but enhancement to check if user-validated=True inside message body.</li>
<li>The thread will route outging Kafka messages over the topic <b><i>RADAR_STATIONS</i></b>. The response will be the aforementioned JSON-like object for mapping geographic-regions to granular radar-stations.</li>
<li>The overall service is wrapped inside a <b>Flask application</b> with decorator <i>`@bus.handle`</i> and dependencies are handled using a Conda environment.</li>
<li>Please ensure your containerized Kafka-server is already up and running so that you can test the consume/publish functionalities.</li>
</ul>

## Installation 

### Software Requirements

* Anaconda
* Python 3.8.8
* Virtual Environment configured using `environment.yml`

### Create a virtual environment based on Python `3.8.8`

Install Anaconda from its [official link](https://docs.anaconda.com/anaconda/install/index.html).

All the requirements for the repository are mentioned in the file `environment.yml`.
Once the initial setup is done, go ahead and activate the environment using the command below:

> conda env create -f environment.yml 

or by following the blog [here](https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/use-python-packages/use-conda-environments-and-install-packages/).


### Firing up the microservice

Activate the virtual environment.

> source activate env

The server for the python app is running on port `5000`, consumes the Kafka-topic `REQUEST_STATIONS`, responds over the Kafka-topic `RADAR_STATIONS`. All this is configurable from the `config.env` file.

To start the server, execute the command below in the virtual environment context.

`> python3 radar_stations_fetcher\app.py`


All someone needs to do is publish a message over `REQUEST_STATIONS`, and consume the response over `RADAR_STATIONS`.


## Implementation Status

The service uses `kafka` for asynchronous communication and will help us in the future with implementing a scalable and highly-available architecture. 

I intend to containerize these services but making a containerized Flask application communicate with a containerized Kafka server is harder than it sounds. 

However, the service itself runs perfectly and produces required output.

`Radar_Stations` class in `radar_stations.py` is used to access the NEXRAD `Radar-server` for S3 data using the `siphon` module.

`Consumer`, and `Producer` in `utils\consumer.py`, and `utils\producer.py` are respectively used to wrap all `kafka`  functionalities in an easy-to-read format.

`app.py` defines the Flask application functionality: `routes` aren't the focus here, .




## The team


<img src="Documentation/Team-members/Vikrant.jpg" alt="Team member's Image" width="130" ALIGN ="left" style="border-radius:50%;"/><br>

- **Vikrant Deshpande**: Vikrant is a first year Master's student studying at Indiana University Bloomington, majoring in Data Science with a focus on Machine Learning and Statistics. He has full time experience as a Data Engineer working with Data pipelining, Analytics, Machine Learning and Software Development. With this course, he intends to gain practical distributed systems skills as well as learn about good open source practices.


   [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/vikrant-deshpande/)
   [<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/vikrantdeshpande09876/)