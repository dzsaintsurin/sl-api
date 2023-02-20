# SL-API-APP
This dicrectory hosts the actual Python web-api application.

The app directory structure:
```
sl-api-app
├── README.md
├── main.py
├── models.py
├── reqres_api
│   ├── __init__.py
│   └── reqres.py
└── requirements.txt
```

The application was built with Python 3.10. 

* main.py is the entrypoint of the application. This is where all the HTTP verbs (GET, POST, PUT, PATCH, DELETE) are getting implemented.
* reqres_api contains logic to retrieve and update data of the [REQRES api](https://github.com/public-apis/public-apis#development),  it makes use of the [requests](https://requests.readthedocs.io/en/latest/) library.
* requirements.txt has the library to be installed on the system where where application will running.

# 
### [Back To The Root Repository](https://github.com/dzsaintsurin/sl-api)