Cookiecutter Django by Codevance
================================

Requirements
-----------

- Docker / Docker-compose
- Python 3.7

Usage
-----

First, create an virtualenv and activate it.

Install cookiecutter and setup the project:

```bash
pip install cookiecutter
cookiecutter https://github.com/codevance/cookiecutter-django -f -o ..
```

Setup the first configurations:

```bash
pip install -r requirements-test.txt
cp -r env-sample .env
```

Commands
-------

Run postgresql and redis:
```bash
make docker-compose-up
```

Run django development server:
```bash
make dev
```

Run tests:
```bash
make test
```


