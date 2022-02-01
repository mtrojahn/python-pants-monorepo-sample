# python-pants-monorepo-sample

### This is a study of a Python monorepo using Pants. 

The things I tried to achieve here are the following:
- Have several webservices on a single Python project using shared libs
- Have linting working
- Have tests working
- Have docker image creation
- Have a working CI (with cache!)

Also, design the whole thing in a way one can easily integrate with PyCharm in order to use debugging, import checks, run code and tests from the IDE with no workarounds on imports or `__init__` files. The only tweak necessary is setting both `src/py` and `tests/py`as source folders.

### Usage
- Clone the repo.
- Run `./pants --version`. This will bootstrap Pants and set up the initial dependencies.
- Many common tasks are listed on the `Makefile` for easy use. Like `make format`, `make lint`, `make test`, etc...
- To run a webservice you can try `./pants run /src/py/webservices/name_of_the_service:app`
- To create a Docker image for the service `./pants package /src/py/webservices/name_of_the_service/Dockerfile`

