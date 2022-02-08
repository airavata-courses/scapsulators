# Scapsulators
Spring 2022 Project


# Weather-Reporter Service

## Functionality/Motivation

<ul>
<li>This standalone microservice is intended to fetch an intuitive <b>GIF image</b>, for visualizing a specific radar-station's surroundings at a specific point in time using <b>NEXRAD's S3 data-lake</b>.</li>
<li>This service is kept separate from the <b>radar-stations-fetcher</b> microservice since we don't want to keep the client waiting too long while media streaming is in progress for this service. Similarly, this separation will <b>avoid a single-point of failure</b> for accessing all NEXRAD data.</li>
</ul>

## Working

<ul>
<li>Weather-Reporter runs a Flask application to accept a JSON-body request and transmit out a GIF image.</li>
<li>The message content should be a bytestream of JSON-like request-parameters.
<code>SAMPLE REQUEST-BODY: {"visualize":"reflectivity", "station":"KVNX", "timestamp":"2018-12-25 09:27:53"}</code>
</li>

<li>The <i><b>"visualize"</i></b> parameter can also take on <i>velocity</i>, or <i>spectrum_width</i> values. Some insight into these parameters is <a href="https://github.com/airavata-courses/scapsulators/wiki/Weather-enthusiasts-assemble"> here.</a>
</li>
<li>The response will be the aforementioned GIF image for visualizing the weather-report for a specific radar-station at that point in time.</li>
</ul>

## Installation 

### Software Requirements

* Docker 20.10.11

### Firing up the microservice

Run the docker container using the provided `.bat` file:

`> start-app.bat`

The server for the python app is running on port `5006`. This is configurable from the `config.env` file.

### Note:
Building the Docker image takes time ($\approx$20 minutes)- the Python dependencies of scientific libraries (PyArt, metpy, etc.) are quite heavy.

The image is then pushed to Docker-registry after this build. The central release-branch and main-branch will simply download this image and run the container on port `5006`.


## Implementation Status

The service uses `REST` for asynchronous communication, and we will use `Kafka` in the future to implement a scalable and highly-available architecture.

`Weather_Reporter` class in `weather_reporter.py` is used to parse the required NEXRAD for S3 data using the `s3.boto` module. There's a good amount of documentation for each function to interpret the underlying data, and subsequently generate the GIF iamge.

`app.py` defines the Flask application functionality: `routes` aren't the focus here.




## The team


<img src="Documentation/Team-members/Vikrant.jpg" alt="Team member's Image" width="130" ALIGN ="left" style="border-radius:50%;"/><br>

- **Vikrant Deshpande**: Vikrant is a first year Master's student studying at Indiana University Bloomington, majoring in Data Science with a focus on Machine Learning and Statistics. He has full time experience as a Data Engineer working with Data pipelining, Analytics, Machine Learning and Software Development. With this course, he intends to gain practical distributed systems skills as well as learn about good open source practices.


   [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/vikrant-deshpande/)
   [<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/vikrantdeshpande09876/)