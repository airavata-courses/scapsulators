# Scapsulators
Spring 2022 Project


# Satellite-View-Reporter Service

## Functionality/Motivation

<ul>
<li>This standalone microservice is intended to fetch an intuitive <b>GIF image</b>, for visualizing a specific radar-station's surroundings at a specific point in time using <b>MERRA's S3 data-lake</b>.</li>
<li>This separated microservice will <b>avoid a single-point of failure</b> for accessing all weather-reporting data.</li>
<li>The logic here focuses on pulling in specific MERRA data subsets into a Network File System and then notifying the downstream Java-microservice via a Kafka-topic message.</li>
</ul>

## Working

<ul>
<li>Satellite-View-Reporter runs a Flask application to accept a JSON-body request and transmit out a GIF image.</li>
<li>The message content should be a bytestream of JSON-like request-parameters.
<code>SAMPLE REQUEST-BODY: {"visualize":"LWGNTICE", "timestamp":"2018-09-01 09:27:53"}</code>
</li>

<li>The <i><b>"visualize"</i></b> parameter can also take on <i>velocity</i>, or <i>spectrum_width</i> values. Some insight into these parameters is <a href="https://github.com/airavata-courses/scapsulators/wiki/Weather-enthusiasts-assemble"> here.</a>
</li>
<li>The response will be the aforementioned data-subset for visualizing the weather-report from a satellite's perspective, at that point in time.</li>
</ul>

## Installation 

### Software Requirements

* Docker 20.10.11

### Firing up the microservice

Run the docker container using the provided `.bat` file:

`> start-app.bat`

### Note:
Building the Docker image takes at most a few minutes.


## Implementation Status

The service uses `Kafka` for asynchronous communication, and message streaming towards the `Java-Redis-Connector` after data-ingestion.

`Satellite_View_Reporter` class in `satellite_view_reporter.py` is used to parse the required MERRA data using the `OPeNDAP` software specifications. There's a good amount of documentation for each function to interpret the underlying data. We don't store the subset data onto a Network-File-System, since we're already subsetting the huge-dataset using `OPeNDAP`, and are parsing the entire response into a manageable (maximum) 120kB response.

`app.py` defines the main application functionality.




## The team


<img src="Documentation/Team-members/Vikrant.jpg" alt="Team member's Image" width="130" ALIGN ="left" style="border-radius:50%;"/><br>

- **Vikrant Deshpande**: Vikrant is a first year Master's student studying at Indiana University Bloomington, majoring in Data Science with a focus on Machine Learning and Statistics. He has full time experience as a Data Engineer working with Data pipelining, Analytics, Machine Learning and Software Development. With this course, he intends to gain practical distributed systems skills as well as learn about good open source practices.


   [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/vikrant-deshpande/)
   [<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/vikrantdeshpande09876/)