# Scapsulators
Spring 2022 Project


## Functionality/Motivation

<ul>
  <li>Here lies the <b> pith </b> of entire project: <b>Weatherpedia</b>.</li>
  <li>We've implemented Continuous Integration using Circle-CI, and synchronous communication using REST-based microservices.</li>
  <li>All microservices are completely <b> dockerized </b> and ready to interact with each other over the same docker network.</li>
  <li>All you need to do is run the entry-point script provided in this branch!</li>
  <li><b>Note:</b> There is a known <a href="https://github.com/ARM-DOE/pyart/issues/92" target="__blank">issue</a> for lack of <a href="https://arm-doe.github.io/pyart/INSTALL.html" target="__blank">Pyart</a> support on an Apple Macbook, and it might cause errors in creating the weather-report GIF, inspite of dockerizing the Python service. We couldn't test our system on a Macbook just yet.</li>
</ul>


## Installation 

### Software Requirements

* [Docker Desktop](https://docs.docker.com/desktop/)

### Firing up the entire system

Clone this repository/branch into your machine using `git clone https://github.com/airavata-courses/scapsulators.git` .

Simply click on the entry-point script: `start-Weatherpedia.sh`

Navigate to [localhost:1000](http://localhost:1000) and explore!

## Implementation Status

The services use `REST` for synchronous communication.

View our [current architecture](https://github.com/airavata-courses/scapsulators/wiki/Architecture-and-Documentation), the [user-lifecycle diagram](https://github.com/airavata-courses/scapsulators/wiki/Flow-Diagram-for-user-lifecycle) and a sample [napkin diagram](https://github.com/airavata-courses/scapsulators/wiki/Flow-Diagram-for-user-lifecycle) in the [Wikis](https://github.com/airavata-courses/scapsulators/wiki) for this repository.

We intend to use a containerized `Kafka` streaming-service to implement a scalable and highly-available architecture, in the future.



## The team


<img src="https://i.ibb.co/K72RqYw/personal.jpg" alt="Team member's Image" width="130" ALIGN ="left" style="border-radius:50%;"/><br>

- **Shubham Mohapatra**: Shubham is a DS graduate student at IUB. He's an experienced Software and Cloud Engineer with several years of Experience in the field of Python Programming, Cloud Computing, Full Stack App Development and Machine Learning. When he's not developing stuff, he can be found playing the guitar, scoring a goal in soccer or improving his K/D ratio in Counter Strike.


   [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/shubhammohapatra/)
   [<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/shubhpatr/)




<img src="Documentation/Team-members/Rutuja.jpg" alt="Team member's Image" width="130" ALIGN ="left" style="border-radius:50%;"/><br>

- **Rutuja Jadhav**: Rutuja is a final year Master's student studying at Indiana University Bloomington, majoring in Computer Science. She has full time experience as an Full stack software engineer for around 4 years. With this course, she intends to gain a deeper understanding of concepts in Distributed Systems and understand how to develop end to end applications on distributed systems.


   [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/rutuja-jadhav-89284a126/)
   [<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/RutujaJadhav19/)



<img src="Documentation/Team-members/Vikrant.jpg" alt="Team member's Image" width="130" ALIGN ="left" style="border-radius:50%;"/><br>

- **Vikrant Deshpande**: Vikrant is a first year Master's student studying at Indiana University Bloomington, majoring in Data Science with a focus on Machine Learning and Statistics. He has full time experience as a Data Engineer working with Data pipelining, Analytics, Machine Learning and Software Development. With this course, he intends to gain practical distributed systems skills as well as learn about good open source practices.


   [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/vikrant-deshpande/)
   [<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/vikrantdeshpande09876/)