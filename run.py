# -*- coding: utf-8 -*-


from pathlib import Path

from example_app_01 import app
from example_app_01.data_fixtures import add_data_fixtures, recreate_db


PROJECT_BASE_FILEPATH = Path(__file__).resolve().parent
APP_01_FILEPATH = Path(PROJECT_BASE_FILEPATH).joinpath('example_app_01')
APP_01_DB_FILEPATH = Path(APP_01_FILEPATH).joinpath(app.config['DATABASE_FILENAME'])


if not APP_01_DB_FILEPATH.exists():
    recreate_db()
    add_data_fixtures()


app.run(debug=True)
