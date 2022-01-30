# python-pants-monorepo-sample

### This is a study of a Python monorepo using Pants. 

The things I tried to achieve here are the following:
- Have several webservices on a single Python project using shared libs
- Have linting working
- Have tests working
- Have docker image creation
- Have a working CI (with cache!)

Also, design the whole thing in a way one can easily integrate with PyCharm in order to use debugging, import checks, run code and tests from the IDE with no workarounds on imports or `__init__` files. The only tweak necessary is setting both `src/py` and `tests/py`as source folders.
