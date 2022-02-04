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
  <br> </br>
  <li> <b> Authenticate </b> :- Login, Register and Update Password</li>
  <li> Each request is url-parsed, i.e all parameters will be parsed in the url, for example http://{url}/authenticate?username=shubhpatra </li>
  <br> </br>
  <li> <b> Audit </b> :- Fetch and Update History log of the user. </li>
  <li> Each request is url-parsed, i.e all parameters will be parsed in the url, for example http://{url}/audit/fetch?username=shubhpatra </li>
  <br> </br>
  <li> <b> Weather Reporting Gif </b>:- Sends a byte-array of generated gif image </li>
  <li> <code>SAMPLE REQUEST-BODY: {"visualize":"reflectivity", "station":"KVNX", "timestamp":"2018-12-25 09:27:53"}</code> </li>
  <li> Response : ByteArray[] Gif Image

<br> </br>

## Installation 

### Prerequisites
Before you start testing the gateway, we need to make sure all the other microservices are up and running. Also, please make sure all dockers are in the same network, this can be done by checking the <b> docker-compose.yml </b> file.

Second prerequisite is the .env file in the gateway directory, this contains all the secret information, ideally this not uploaded in git. But for an easier submission we have included it, make sure all the docker names are correct for the respective microservice. 

If you're using current branch, make sure to build the Java Microservice as it creates all the docker networks. All this will be mitigated in the master branch.

### Software Requirements

* Docker 20.10.11

### Firing up the gateway

Run the docker container using the provided `make` file:

`> cd gateway`
<br> </br>
`> make build`

The server for the python app is running on port `5000`. This is configurable from the `.env` file.



## Implementation Status

The service uses `REST` for asynchronous communication, and we will use `Kafka` in the future to implement a scalable and highly-available architecture.

Will suggest using postman to test-run the api's.

## Testing

Basic jest test cases have been implemented for the gateway. 

`> cd gateway`
<br> </br>
`> npm run test`



## The team


<img src="https://i.ibb.co/K72RqYw/personal.jpg" alt="Team member's Image" width="130" ALIGN ="left" style="border-radius:50%;"/><br>

- **Shubham Mohapatra**: Shubham is a DS graduate student at IUB. He's an experienced Software and Cloud Engineer with several years of Experience in the field of Python Programming, Cloud Computing, Full Stack App Development and Machine Learning. When he's not developing stuff, he can be found playing the guitar, scoring a goal in soccer or improving his K/D ratio in Counter Strike.


   [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/shubhammohapatra/)
   [<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/shubhpatr/)
