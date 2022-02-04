# Scapsulators
Spring 2022 Project


# Gateway Service

## Functionality/Motivation

<ul>
  <li>This is the <b> heart </b> of all microservices. This is the connecting point from the front-end to all the microservices. And believe me it handles all kinds of errors!</li>
  <li>This service is completely <b> dockerized </b> and ready to interact with all microservices. One prerequisite all microservices need to be in the same docker-network. Not thaat a big of a deal with a docker file. </li>
</ul>

## Working

<ul>
<li>Gateway runs a Node.js server powered by express.js, it sends json requests, url-encoded requests to the other microservices, there is also a testing version for kafka which is not included in the project 1</li>
<li>The gateway is divided into three services for now, 1) Authenticate, 2) Audit, and 3) Weather Reporting Gif </li>
  
  <li> Authenticate :- Login, Register and Update Password</li>
  <li> Each request is url-parsed, i.e all parameters will be parsed in the url, for example http://{url}/authenticate?username=shubhpatra </li>
  <br> </br>
  <li> Audit :- Fetch and Update History log of the user. </li>
  <li> Each request is url-parsed, i.e all parameters will be parsed in the url, for example http://{url}/audit/fetch?username=shubhpatra </li>
  <br> </br>
  <li> Weather Reporting Gif :- Sends a byte-array of generated gif image </li>
  <li> <code>SAMPLE REQUEST-BODY: {"visualize":"reflectivity", "station":"KVNX", "timestamp":"2018-12-25 09:27:53"}</code> </li>
  <li> Response : ByteArray[] Gif Image


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


## Implementation Status

The service uses `REST` for asynchronous communication, and we will use `Kafka` in the future to implement a scalable and highly-available architecture.

`Weather_Reporter` class in `weather_reporter.py` is used to parse the required NEXRAD for S3 data using the `s3.boto` module. There's a good amount of documentation for each function to interpret the underlying data, and subsequently generate the GIF iamge.

`app.py` defines the Flask application functionality: `routes` aren't the focus here.




## The team


<img src="Documentation/Team-members/Vikrant.jpg" alt="Team member's Image" width="130" ALIGN ="left" style="border-radius:50%;"/><br>

- **Vikrant Deshpande**: Vikrant is a first year Master's student studying at Indiana University Bloomington, majoring in Data Science with a focus on Machine Learning and Statistics. He has full time experience as a Data Engineer working with Data pipelining, Analytics, Machine Learning and Software Development. With this course, he intends to gain practical distributed systems skills as well as learn about good open source practices.


   [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/vikrant-deshpande/)
   [<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/vikrantdeshpande09876/)
