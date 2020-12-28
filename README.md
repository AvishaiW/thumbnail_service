# Thumbnail Service
An interview assignment which fetches a JPEG image from a given URL 
and returns it within the given dimensions while retaining the aspect ratio.

### Installation & Execution  

####Server Side
We are going to see 2 ways to get the server up and running 
(and of course we have the Heroku app running in the background as well)  

#####Docker
- [Install Docker](https://docs.docker.com/get-docker/) on your machine.
- open your CLI and run `docker run -p 5000:5000 -d avishaiw/thumbnail-service`. 
  The command will pull the image from docker hub and create a new container that 
  maps the 5000 port on the container to the 5000 port on the host (your machine).
  by running the command you'll have a server running on your machine.    

#####Local via Github
- [Install Python](https://www.python.org/downloads/) 3.x if you don't have it yet on your machine.
- [install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- open the CLI and pull the project repository running: `git clone https://github.com/AvishaiW/thumbnail_service.git`
- run `cd thumbnail_service`
- run `pip install -r requirements.txt` to install the dependencies
- run `python main.py` and you'll have the server up and running 
on your machine exposing the localhost on port 5000  

#### Client side
If your brought up the server side locally you can:
- open your browser and run the following URL:
`localhost:5000/thumbnail?url={URL}&width={Width}&height={Height}`  
where:  
   - URL: url of a JPEG image of your choice.    
   - Width: the target width of the thumbnail (positive number).  
   - Height: the target height of the thumbnail (positive number).     
Note that if you enter wrong parameters you'll receive errors.  

#####Heroku App
The app is also deployed on heroku, so even if you don't run the server locally,
you can access the app on your browser using the following link:  
`https://thumbnail-service1.herokuapp.com/thumbnail?url={URL}&width={Width}&height={Height}`  
where you can fill in the URL,Width & Height as mentioned above.    

####Further Steps   
-[ ] tests  


####Scaling Up  
Since Flask is a development server, we must add a 
production ready WSGI server (uWSGI/Gunicorn/etc.), 
then we will want to be able to multiply the number of instances (AWS EC2 instances perhaps) running the app 
and a load balancer (such as NGINX) which distributes the traffic across the different instances, 
all of this will be done behind a DNS server (and not the localhost of course) such as the Heroku app 
and scaling up the number of dynos serving the app will also scale up the project. all of which should reduce the 
load off of the given app a be able to maintain durability, stability and stay secure over time. 
