# Scapsulators
Spring 2022 Project


# FrontEnd

## Functionality/Motivation

<ul>
  <li>This is the viewing surface of the applications, a very user-friendly and easy on the eyes application for the users.</li>
  <li> This is also been dockerized and can be run by the basic start script. The interface has been designed to be as intuitive as possible. </li>
</ul>

## Working

<ul>
<li>The frontend is a reactjs application which uses axios to make API calls for all the services</li>
<li>The UI is divided into 1) Login Landing Page, 2) Sign-Up/ Reset password page, 3) Home Page</li>
  <br> </br>
  <li> The login page is straight forward it calls onto the authentication microservice via the API gateway </li>
  <li> The sign-up page registers new users and authenticates them </li>
  <br> </br>
  <li> The homepage has brief description on the various services and has 2 types of querry outlets, one via the Audit table, a user can simply click on a particular history row and generate a Gif image </li>
   <li> The second mode of querrying is via specific field drop-box and generate the required querry</li>

## Installation 



### Software Requirements

* Docker 20.10.11
* Works best with Browsers Edge, Mozill Firefox

### Hosting the frontend.

Make sure to run gateway and complete gateway prerequisites. After that

Run the docker container using the provided `docker-compose` file:

`> cd gateway`
<br> </br>
`> docker-compose up`

The server for the frontend app is running on port `1000`.






## The team


<img src="https://i.ibb.co/K72RqYw/personal.jpg" alt="Team member's Image" width="130" ALIGN ="left" style="border-radius:50%;"/><br>

- **Shubham Mohapatra**: Shubham is a DS graduate student at IUB. He's an experienced Software and Cloud Engineer with several years of Experience in the field of Python Programming, Cloud Computing, Full Stack App Development and Machine Learning. When he's not developing stuff, he can be found playing the guitar, scoring a goal in soccer or improving his K/D ratio in Counter Strike.


   [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/shubhammohapatra/)
   [<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/shubhpatr/)
