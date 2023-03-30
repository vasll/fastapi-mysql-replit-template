# FastAPI + MySQL replit template

This template allows you to run a FastAPI server and a MySQL database on Replit.

## Getting started
1. Fork this template
2. Inside the [secrets tab](https://docs.replit.com/programming-ide/workspace-features/storing-sensitive-information-environment-variables) in the replit tools add the following:
	- `db_user` Name of the user that will have full access to the db
	- `db_pass` Password for the user
    - `db_name` Name of the database to be created
3. Click the `Run` button and the MySQL database, credentials and [Python venv](https://docs.python.org/3/library/venv.html) will be created for you using the given secrets

## Files and folders
### `app/`
Contains example FastAPI code to connect to a database using [SQLAlchemy](https://fastapi.tiangolo.com/tutorial/sql-databases/).
- `main.py`: sets up a FastAPI instance and stars the uvicorn server
- `database.py`: establishes a db connection and contains the [db dependency](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)
- `schemas.py`: contains db schemas (tables)
- `models.py`: contains models based on db schemas, used for data validation

### `startup.sh` 
Creates a venv in `.venv/`and installs a MySQL server instance into `sql_data/`

## Credits
The MySQL database creation .sh script was forked from this repl: [@dprevedello/PHP-MySQL](https://replit.com/@dprevedello/PHP-MySQL)

