# Project Documentation

This document provides detailed information on how to use the REST API for the "Person" resource. Please refer to this documentation for setup instructions, request/response formats, sample API usage, and any known limitations or assumptions made during development.

> LIVE API Endpoint is https://hgnxbackend-prmpsmart.b4a.run/api
>
> LIVE API Endpoint is https://hgnxbackend-prmpsmart.b4a.run/api

## Table of Contents
* [Setup Instructions](#setup-instructions)
* [API Endpoints](#api-endpoints)
* [Request/Response Formats](#requestresponse-formats)
* [Sample API Usage](#sample-api-usage)
* [Known Limitations and Assumptions](#known-limitations-and-assumptions)

---

## Setup Instructions
To setup the api on your local machine, follow this steps on you command terminal

1. **Clone the Repository:**
```
git clone https://github.com/prmpsmart/hgnx_backend.git
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

5. The API will be available locally at `http://127.0.0.1:8000`.

---

## API Endpoints

The API provides the following endpoints for CRUD operations on the "Person" resource:

* **Create**---
    Adding new person [POST]

    * **`/api`**

* **Read All (List)**---
    Retrieving all persons in database [GET]

    * **`/api`**

* **Read A Single Person**---
    Retrieving one specific person by id or name[GET]
    * **`/api/{id}`** 
    * **`/api/{name}`**
    * **`/api?name={name}`**

* **Update A Person**---
    Updating a single existing person by id or name [PUT]
    * **`/api/{id}`**
    * **`/api/{name}`**

* **Delete A Person**---
    Delete a single existing person by id or name [DELETE]
    * **`/api/{id}`**
    * **`/api/{name}`**




