# json-data-storage-api

## Overview of the App
The developed API allows for storing and retrieving JSON data without a predefined schema. It supports basic CRUD operations and includes authentication.

## Endpoints

### POST /data
- Accepts a JSON object and stores it in the database.
- Requires Authentication.

Example curl Commands Execution
Below is the example sequence using curl commands:

1. POST Request:
curl -X POST http://loctalhost:5000/data ^
-H "Content-Type: application/json" ^
-H "Authorization: Basic YWRtaW46c2VjcmV0" ^
-d "{\"key\": \"value\"}"

2. GET Request:
curl -X GET http://localhost:5000/data/1 ^
-H "Authorization: Basic YWRtaW46c2VjcmV0"

3. PUT Request:
curl -X PUT http://localhost:5000/data/1 ^
-H "Content-Type: application/json" ^
-H "Authorization: Basic YWRtaW46c2VjcmV0" ^
-d "{\"new_key\": \"new_value\"}"

4. DELETE Request:
curl -X DELETE http://localhost:5000/data/1 ^
-H "Authorization: Basic YWRtaW46c2VjcmV0"


### Instructions for Docker
1. Build the Docker image with command:
docker build -t json-api .
2. Run the Docker container as:
docker run -p 5000:5000 json-api
