<h2>Assignment 01</h2>

<h3>Create and start python3 environment using the following command</h3>

```
# Create environment
python -m venv <env_name>

# Activating environment
# For mac and linux os users
source <env_name>/bin/activate
# For windows users
<env_name>/Scripts/activate
```

<h3>Install required packages from the requirements file</h3>

```
pip install -r requirements.txt
```

<h3>Create .env file in daryl_fernandes_002834250_01/ with the following key value pairs</h3>

```
SQLALCHEMY_DATABASE_URI_DEV = "mysql://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DBNAME>"
# The following flag can toggle on/off the tracking of inserts, updates, and deletes for models
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

`` Note: Make sure to create the database with the name (<DBNAME>) mentioned above before proceeding further``

<h3>Run the following scripts to create database file</h3>

```
flask db migrate
flask db migrate -m "initial commit"
flask db upgrade
```

<h3>Update the dev_config.py, production_config.py files in daryl_fernandes_002834250_01/src/config (if required)</h3>

<h3>To run the app</h3>

```
# Navigate to daryl_fernandes_002834250_01
cd daryl_fernandes_002834250_01

# Run the following command to start the server
python ./app.py
```