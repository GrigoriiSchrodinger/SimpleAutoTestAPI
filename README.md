<div align="center">
    <img src="asset/logo_api.png" alt="API">
</div>

---

<h1 align="center"> API auto-test </h1>
An example of a simple implementation of api auto tests in python, 
the site https://reqres.in/ is used as an example

---

<h1 align="center">launch</h1>

First, install the dependencies:: 
* [requests](https://pypi.org/project/requests/)
* [jsonschema](https://pypi.org/project/jsonschema/)

```
pip install -r requirements.txt
```

Run the tests with the following command:
```
python3 main.py
```

---

<h1 align="center">Project structure</h1>

~~~
SimpleAutoTestApi/
├── asset/
│   └── ...
├── src/   
│   ├── api/
│   │   ├── modules/
│   │   │   └── ...
│   │   ├── schemas/
│   │   │   └── ...
│   │   └── endpoint.py
│   ├── tests/
│   │   └── ...
│   └── utils/
│       └── ...
├── main.py
├── .gitignore
├── README.md
└── requirements.txt
~~~

## asset/
The directory where the resources (such as images) are located.

## src/
The directory that contains the project's source code. It includes several subdirectories:
1. **api/** - This directory contains modules related to the api being tested, such as enpoint or response schemas.
2. **tests/** - This directory contains api test files.
4. **utils/** - This directory contains auxiliary files and modules, such as logger settings.

## main.py
main project file.

---

