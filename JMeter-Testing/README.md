# Scapsulators
Spring 2022 Project


## JMETER TESTING
1. Download Jmeter from the official [link.](https://jmeter.apache.org/download_jmeter.cgi)

2. Extract the installation folder.

3. Run the `jmeter.sh` or `jmeter.bat` file depending on if you're using Linux or Windows.

4. Open the `Gatway-Test-Plan.jmx` file located in this folder.

5. Note the hardcoding of Gateway URL and parameters is in components like the parent `Thread Group` or individual `HTTP Request` appendages.

6. Configured the number of user-threads to 1000 for now.
>Runs fine for my local machine: 16GB RAM, Intel i7 1165-G7, Octa-core.

7. Requests directed from *Gateway* -> *Python* Weather-reporter service, seem to be processed in a queue-like system due to `gunicorn` as the load-balancer.

8. **First-impressions**: System doesn't crash, but Python reporter only processes massive requests in its own time. Initially sends response in 20 seconds, but slows down to approx. 30 seconds per response.