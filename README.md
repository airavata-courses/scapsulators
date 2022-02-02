# Scapsulators
Spring 2022 Project


# Radar-Stations Fetcher Service

## Functionality/Motivation

<ul>
<li>This standalone microservice is intended to fetch a neat <b>JSON data structure</b>, for mapping geographic-regions to individual radar-station codes maintained on <b>NEXRAD's S3 data-lake</b>.</li>
<li>This service is kept separate from the <b>weather-reporter</b> microservice since we don't want to keep the client waiting too long while media streaming is in progress for the latter service. Similarly this separate service will avoid a single-point of failure for accessing all NEXRAD data.</li>
</ul>

## Working

<ul>
<li>Radar-Stations Fetcher runs a Flask application to accept a GET-request and transmit out a JSON-object.</li>.The message content doesn't matter for now, but enhancement to check if user-validated=True inside message body.</li>
<li>The response will be the aforementioned JSON-like object for mapping geographic-regions to granular radar-stations.</li>
<li>The overall service is wrapped inside a <b>Flask application</b> and dependencies are handled using a Conda environment.</li>
</ul>

## Installation 

### Software Requirements

* Docker 20.10.11

### Firing up the microservice

Run the docker container using the provided `.bat` file:

`> start-app.bat`

The server for the python app is running on port `5001`.
This is configurable from the `config.env` file.


## Implementation Status

The service uses `REST` for asynchronous communication, and we will use `Kafka` in the future to implement a scalable and highly-available architecture.

`Radar_Stations` class in `radar_stations.py` is used to access the NEXRAD `Radar-server` for S3 data using the `siphon` module.

`app.py` defines the Flask application functionality: `routes` aren't the focus here.




## The team


<img src="Documentation/Team-members/Vikrant.jpg" alt="Team member's Image" width="130" ALIGN ="left" style="border-radius:50%;"/><br>

- **Vikrant Deshpande**: Vikrant is a first year Master's student studying at Indiana University Bloomington, majoring in Data Science with a focus on Machine Learning and Statistics. He has full time experience as a Data Engineer working with Data pipelining, Analytics, Machine Learning and Software Development. With this course, he intends to gain practical distributed systems skills as well as learn about good open source practices.


   [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/vikrant-deshpande/)
   [<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/vikrantdeshpande09876/)