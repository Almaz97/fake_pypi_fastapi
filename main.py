import configparser
from pathlib import Path

import fastapi
import uvicorn
import fastapi_chameleon
from fastapi_chameleon import template
from starlette.staticfiles import StaticFiles

from data import db_session
from views import home
from views import account
from views import packages


app = fastapi.FastAPI()


def main():
    configure(dev_mode=True)
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)


def configure(dev_mode: bool):
    configure_templates()
    configure_routers()
    configure_db(dev_mode=dev_mode)


def configure_db(dev_mode: bool):
    file = (Path(__file__).parent / 'db' / 'pypi.sqlite').absolute()
    db_session.global_init(file.as_posix())


def configure_templates():
    fastapi_chameleon.global_init('templates')


def configure_routers():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


if __name__ == '__main__':
    main()
else:
    configure(dev_mode=True)
