
# Flask JSON Server Application




## Overview

This is a simple Flask application that serves JSON responses. The application provides functionality to add updates and retrieve information.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Docker
* Docker Compose

### Running the Application

* Clone the repository: `git clone https://github.com/Tricked111/Flask-JSON-Server-Application.git`
* Navigate to the client directory: `cd Flask-JSON-Server-Application`
* Build the Docker image: `docker build -t flask-api:1.0 .`
* Start the Docker container: `docker run -d -p 5000:5000 flask-api:1.0`

The application should now be accessible at http://localhost:5000.

## API Endpoints
The following API endpoints are available:

`GET /movies` Returns a list of all movies.

```json
[
  {
    "id": 1,
    "title": "The Matrix",
    "description": "The Matrix is a computer-generated gream world ...",
    "release_year": 1999
  },
  {
    "id": 2,
    "title": "The Matrix Reloaded",
    "description": "Continuation of the cult classic The Matrix",
    "release_year": 2003
  }
]
```
`POST /movies`
Adds a new movie.
```json

  {
    "title": "The Matrix",
    "description": "The Matrix is a computer-generated gream world ...",
    "release_year": 1999
  }
  ```


`GET /movies/id` Returns a movie by ID.
```json
[
  {
    "id": 1,
    "title": "The Matrix",
    "description": "The Matrix is a computer-generated gream world ...",
    "release_year": 1999
  }
]

```
`PUT /movies/id` Update movie by ID or 404 EROR if not found.
The input data must be:
```json

  {
    "id": 1,
    "title": "The Matrix",
    "description": "The Matrix is a computer-generated gream world ...",
    "release_year": 1999
  }


```


## Authors
* Daniil Kniazkin
