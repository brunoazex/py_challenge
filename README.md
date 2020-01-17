# Data Analysis Challenge in Python

## Overview

The challenges are separated on two methods within `Challenge` class (challenge.py).

Challenge one Dataset is produced from a Pivot table.

Challenge two Dataset is produced from a SQL.

**Note**: Challenge two uses pandas dataframe for csv export simplicity convenience.

Database (database.py) class is just a simple abstraction of `psycopg2.

### Exported data

File mask of exported data is `[dataset-name][Year-Month-Day_Hour-Minute-Second].csv`.

The produced CSV will be stored on `./output` folder

### Docker

Running on a docker container requires to configure .env file with this environment variables:

```bash   
    DB_HOST= #<for hostname>
    DB_NAME= #<for database name>
    DB_USER= #<for database user>
    DB_PASS= #<for database user's password>
```

For convenience you can run automatically on docker container:

```bash
    ./run.sh
```