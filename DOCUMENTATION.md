# Project Documentation

This document provides detailed information on how to use the REST API for the "Person" resource. Please refer to this documentation for setup instructions, request/response formats, sample API usage, and any known limitations or assumptions made during development.

> LIVE API Endpoint are https://person-api-rgv0.onrender.com/api for GET and POST requests and https://person-api-rgv0.onrender.com/api/{id} ,for PUT,DELETE and GET requests
>


## Table of Contents
* [Setup Instructions](#setup-instructions)
* [API Endpoints](#api-endpoints)
* [Request/Response Formats](#requestresponse-formats)
* [Data Validation](#data-validation)
* [Sample API Usage](#sample-api-usage)
* [Known Limitations and Assumptions](#known-limitations-and-assumptions)

---

## Setup Instructions
To setup the api on your local machine, follow this steps on you command terminal

1. **Clone the Repository:**
```
git clone https://github.com/Nathan-Yinka/HNG-user-Api.git
cd stage2
```

2. **Setup the Virtual Environment**
For Mac
```
source venv/bin/activate
```
For windows
```
source script/bin/activate
```

3. **Install Requirements:**
```
pip install -r requirements.txt
```

4. **Run the Server Locally:**
```
python manage.py runserver
```

5. The API will be available locally at `https://person-api-rgv0.onrender.com/`.

---

## API Endpoints

The API provides the following endpoints for CRUD operations on the "Person" resource:

* **[Create](#create-a-person-post-api)**---
    Adding new person [POST]

    * **`/api`**

* **[Read All (List)](#read-a-person-get-api-apiid-apiname-apinamename)**---
    Retrieving all persons in database [GET]

    * **`/api`**

* **Read A Single Person**---
    Retrieving one specific person by id or name[GET]
    * **`/api/{id}`** 
    * **`/api/{name}`**
    * **`/api?name={name}`**

* **[Update A Person](#update-a-person-put-apiname-apiid)**---
    Updating a single existing person by id or name [PUT]
    * **`/api/{id}`**
    * **`/api/{name}`**

* **[Delete A Person](#delete-a-person-delete-apinameapiid)**---
    Delete a single existing person by id or name [DELETE]
    * **`/api/{id}`**
    * **`/api/{name}`**

## Request/Response Formats

* ### Create A Person (POST /api)

    **Request Format (/api):**
    ```python
    import requests

    api_url = "https://person-api-rgv0.onrender.com/api"

    data = {
        "name": "Oludare Nathaniel"
    }

    response = requests.post(api_url, json=data)
    print(response.json())
    ```

    **Response Format (Created - 201):**
    ```json
    {
        "id":1,
        "name": "oludare nathaniel",
    }
    ```

    **Response Format (Bad Request - 400):**
    ```json
    {
        "name": [
            "Person with this Name already exists."
        ]
    }
    ```

* ### Read a Person (GET /api, /api/{id}, /api/{name}, /api?name={name})

    **Request Format (/api):**
    ```python
    import requests

    url = "https://person-api-rgv0.onrender.com/api"

    response = requests.request("GET", url)

    print(response.json())
    ```

    **Response Format (Ok- 200):**
    ```json
    [
        {
            "id": 1,
            "name": "oludare nathaniel"
        },
        {
            "id": 2,
            "name": "adeyinka"
        },
        {
            "id": 3,
            "name": "nathan yinka"
        }
    ]
    ```

    **Request Format (/api/{id}):**
    ```python
    import requests

    url = "https://person-api-rgv0.onrender.com/api/1"

    response = requests.request("GET", url)

    print(response.json())
    ```

    **Response Format (Ok- 200):**
    ```json
    {
        "id": 1,
        "name": "oludare nathaniel"
    }
    ```

    **Request Format (/api/{name}):**
    ```python
    import requests

    url = "http://127.0.0.1:8002/api/adeyinka"

    response = requests.request("GET", url)

    print(response.json())
    ```

    **Response Format (Ok- 200):**
    ```json
    {
        "id": 2,
        "name": "adeyinka"
    }
    ```

    **Request Format (/api?name={name}):**
    ```python
    import requests

    url = "http://127.0.0.1:8002/api/adeyinka"

    response = requests.request("GET", url)

    print(response.json())
    ```

    **Response Format (Ok- 200):**
    ```json
    {
        "id": 2,
        "name": "adeyinka"
    }
    ```

    **Response Format (Not Found - 404):**
    ```json
    {
        "detail": "Not found."
    }
    ```

* ### Update a Person (PUT /api/{name}, /api/{id})
    **Request Format:(/api/{name})**
    ```python
    import requests

    api_url = "https://person-api-rgv0.onrender.com/api/adeyinka"

    data = {
        "name": "Oludare Adeyinka"
    }

    response = requests.put(api_url, json=data)
    print(response.json())
    ```

    **Response Format (Ok - 200):**
    ```json
    {
        "id": 2,
        "name": "oludare adeyinka"
    }
    ```

    **Request Format:(/api/{id})**
    ```python
    import requests

    api_url = "https://person-api-rgv0.onrender.com/api/1"

    data = {
        "name": "Daniel"
    }

    response = requests.put(api_url, json=data)
    print(response.json())
    ```

    **Response Format (Ok - 200):**
    ```json
    {
        "id": 1,
        "name": "daniel"
    }
    ```

    **Response Format (Not Found - 404):**
    ```json
    {
        "detail": "Not found."
    }
    ```

* ### Delete a Person (DELETE /api/{name},/api/{id})
    **Request Format(/api/{name}):**
    ```python
    import requests

    api_url = "https://person-api-rgv0.onrender.com/api/daniel"

    response = requests.delete(api_url)
    print(response.json())
    ```

    **Request Format(api/{id}):**
    ```python
    import requests

    api_url = "https://person-api-rgv0.onrender.com/api/daniel"

    response = requests.delete(api_url)
    print(response.json())
    ```

    **Response Format (NO_CONTENT - 204):**
    ```json

    ```

    **Response Format (Not Found - 404):**
    ```json
    {
        "detail": "Not found."
    }
    ```

## Data Validation
The following validations are performed on the data received from the user when creating or updating a person record in the database using POST and PUT methods respectively.
* When data from the user is sent, the data is validated, so as to contain only string data type. That is any other data type isnt allowed.
    Example
    **Request Format (/api):**
    ```python
    import requests

    api_url = "https://person-api-rgv0.onrender.com/api"

    data = {
        "name": "Oludare Nathaniel2333"   #data containing other data types isnt allowed
    }

    response = requests.post(api_url, json=data)
    print(response.json())
    ```

    **Response Format (Bad Request - 400):**
    ```json
    {
        "name": [
            "field must be a string"
        ]
    }
    ```

* When data from the user sent, the data is validated by removing extra trailing white spaces and is stored in lowercase.
    Example
    **Request Format (/api):**
    ```python
    import requests

    api_url = "https://person-api-rgv0.onrender.com/api"

    data = {
        "name": "  OLUdare       Nathaniel        "   #data cotaining excess white spaces and upper and lower case 
    }

    response = requests.post(api_url, json=data)
    print(response.json())
    ```

    **Response Format (Created - 201):**
    ```json
    {
        "id":1,
        "name": "oludare nathaniel",
    }
    ```

* When black data is sent the data is validated and a bad request response is sent.
    **Request Format (/api):**
    ```python
    import requests

    api_url = "https://person-api-rgv0.onrender.com/api"

    data = {
        "name": "      "   #empty data sent to the backend
    }

    response = requests.post(api_url, json=data)
    print(response.json())
    ```

    **Response Format (Bad Request - 400):**
    ```json
    {
        "name": [
            "This field may not be blank."
        ]
    }
    ```

*  When no data key **name** is sent to a bad request error response is raised
     **Request Format (/api):**
    ```python
    import requests

    api_url = "https://person-api-rgv0.onrender.com/api"

    data = {
       #no data with key "name' sent
    }

    response = requests.post(api_url, json=data)
    print(response.json())
    ```

    **Response Format (Bad Request - 400):**
    ```json
    {
        "name": [
            "This field is required."
        ]
    }
    ```

* When creating a new Person, if the name already exist,it sends a 400 bad request error

    **Response Format (Bad Request - 400):**
    ```json
    {
        "name": [
           "person with this name already exists."
        ]
    }
    ```

## Sample API Usage
Here are some sample API usage scenarios with Python code examples:

1. **Read all Persons:**
``` javascript
var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

fetch("https://person-api-rgv0.onrender.com/api", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

2. **Read a Person using the user_id:**
```javascript
var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

fetch("https://person-api-rgv0.onrender.com/api/2", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
3. **Read a person using the unique name**
```javascript
var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

fetch("https://person-api-rgv0.onrender.com/api/nathan", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

4. **Read a person using query parameters**
```javascript
var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

fetch("https://person-api-rgv0.onrender.com/api?name=nathan", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
5. **Create new person with POST requests to /api**
```javascript
var formdata = new FormData();
formdata.append("name", "Pelumi");

var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("https://person-api-rgv0.onrender.com/api", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

6. **Update a person with id with PUT request**
```javascript
var formdata = new FormData();
formdata.append("name", "Alex");

var requestOptions = {
  method: 'PUT',
  body: formdata,
  redirect: 'follow'
};

fetch("https://person-api-rgv0.onrender.com/api/2", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
7. **Update a person with name with PUT request**
```javascript
var formdata = new FormData();
formdata.append("name", "David");

var requestOptions = {
  method: 'PUT',
  body: formdata,
  redirect: 'follow'
};

fetch("https://person-api-rgv0.onrender.com/api/alex", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
8. **Delete a person by ID or Name (DELETE)**
```javascript
var requestOptions = {
  method: 'DELETE',
  redirect: 'follow'
};

fetch("https://person-api-rgv0.onrender.com/api/4", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
```javascript
 var requestOptions = {
  method: 'DELETE',
  redirect: 'follow'
};

fetch("https://person-api-rgv0.onrender.com/api/david", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

---

## Known Limitations and Assumptions
1. The API is not secured in any way so it's recommended to use this only for local development purposes as you can update,create and delete without authorization
2. The API saves all the names in lower case letters
3. THE API doesnt accept and charaters or symbol to be saved in the database expect letters
4. The API cannot have the same names save in the data base, names are unique.