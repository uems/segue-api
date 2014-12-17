# SEGUE API

Requirements:
- Ubuntu server 12.04 LTS or higher

Instructions:
- clone the repository
- make a virtualenv for the project, and ```workon``` it
- run ```docs/install_os_deps.sh``` (to install both the OS and the virtual environment dependencies)
- run ```python manage.py create_tables``` (to create the tables)
- run ```python manage.py populate``` (to populate the cities and countries)
- run ```python manage.py runserver``` (to run the server in development mode)

With the application running:
- Register a JWT (JSON Web Token), making the following request:

```json
POST /api/v1/auth
Content-Type:application/json;
{
  "username": "segue",
  "password": "segue"
}
```

The system will respond with the token:

```json
{
    "token": <jwt-token>
}
```

Use the token with all requests to the API, with the following header:
```
Authorization: Bearer <jwt-token>
```

For more information about the queries that you can make on the objects, plase visit: https://flask-restless.readthedocs.org/en/latest/searchformat.html