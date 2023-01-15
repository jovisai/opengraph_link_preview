# Opengraph based link preview service
A simple python service to return link preview metadata, also has memcache for caching 

### Design
WIP

### Development Setup
This project a regular flask based python app which you can clone and open up in pycharm IDE.

### Pre-requisites
- You should have memcached server installed in your operating system. For ubuntu linux OS, it can be installed 
using the below command
```commandline
sudo apt install memecached -y
```

### With docker
You need not use the docker files if you don't wish to containerize the service, You can use this as a regular
flask application. 
But if you would like to use the docker enginer, you can refer to the [docker setup guide ](https://docs.docker.com/get-docker/)

To build the docker container you can run the below command
```commandline
docker compose build
```

To start the container after building it, execute
```commandline
docker compose start
```
The output should look something like this
```commandline
[+] Running 1/1
 ⠿ Container opengraph_link_preview-opengraph_link_preview-1  Started  
```

### No docker? How to start the app from command line?
```commandline
sh entrypoint.sh
```

The output of the above script should resemble something like this:
```commandline
[2023-01-15 18:04:46 +0530] [41496] [INFO] Starting gunicorn 20.1.0
[2023-01-15 18:04:46 +0530] [41496] [INFO] Listening at: http://0.0.0.0:8000 (41496)
[2023-01-15 18:04:46 +0530] [41496] [INFO] Using worker: sync
[2023-01-15 18:04:46 +0530] [41507] [INFO] Booting worker with pid: 41507
memcache initialization 127.0.0.1 11211
```

As you can see, the project uses gunicorn WSGI server for deployment. 
The last line confirms that memcache connection successfull. If you wish to change the connection parameters in case
your memcache is hosted somewhere else then change the config in the .env file. 

To test the api from command line you can try the below-mentioned curl command:
```commandline
curl --location --request POST 'http://localhost:8000/v1' \
--header 'Content-Type: application/json' \
--data-raw '{
	"link": "https://en.wikipedia.org/wiki/Twenty_Thousand_Leagues_Under_the_Seas"
}'
```

You can expect a json output in the below format

```commandline
{
    "description": "1870 novel by Jules Verne",
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Houghton_FC8_V5946_869ve_-_Verne%2C_frontispiece.jpg/1200px-Houghton_FC8_V5946_869ve_-_Verne%2C_frontispiece.jpg",
    "title": "Twenty Thousand Leagues Under the Seas - Wikipedia",
    "url": "https://en.wikipedia.org/wiki/Twenty_Thousand_Leagues_Under_the_Seas"
}
```

### The public docker respository for this project
https://hub.docker.com/r/jovisai/opengraph_link_preview


