# Quickstart
- Create virtual environment with Python >= 3.8
- Install production libraries `pip install -r requirements.txt`
- Export environment variables
  ```
  export FLASK_ENV=development  # optional, if want to run in development mode
  export FLASK_APP=app.api:app
  ```
  
- Run the api `flask run`
- Test the endpoint 
  ```shell
  curl \
    -d '{"pool":[1,7.5,2.3,6], "percentile":100}' \
    -H "Content-Type: application/json" \
    -X POST http://localhost:5000/
  ```
- Response `{"data":7.5}`

# Endpoints
## Percentile of a list 
```
POST /
Content-Type: application/json

{
  "pool": [1, 4, 3.5, 9],
  "percentile": 80
}
```  

Calculate percentile of an array of numbers. Params supplied in request body.

### Request body
JSON object contains
- `pool (array of numbers)`: in body, array of numbers to get percentile from,
  less than 100,000 numbers (this number if configurable).
- `percentile (number)`: in body, percentile P in range 0<P<=100  

Example 
```json
{
  "pool": [1, 4, 3.5, 9],
  "percentile": 80
}
```

### Responses 
`200 OK`  
with result in response body
  {"data": result}

`400 Bad Request`  
in case request body is not correct (missing fields, wrong data types)

### Example
```shell
# server running on localhost:5000
curl \
  -d '{"pool":[1,7,2,6], "percentile":100}' \
  -H "Content-Type: application/json" \
  -X POST http://localhost:5000/

# Response
> HTTP 200 OK
> {"data": 7}
```


# Development  
- Install development libraries `pip install -r requirements-dev.txt`
- Running test with `pytest tests` 

# Production
- The api application should be deployed together with a WSGI server behind a web server.
- A common setup on virtual machine: NGINX <-> Gunicorn <-> API [link](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04). 
  See [link](https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/#gunicorn) for more info on Flask deployment.
- A setup on Kubernetes is to build a Docker image, 
  run that as a k8s Service with the gunicorn command, adding k8s Ingress before that Service.
- Note that the web server should be config to allow bigger request body if
  you want to post a big array. Default request body size for nginx should
  be around 1 MB.
