# Data Logistics Hands-on

This part will cover the introduction to Airflow and creation of data pipelines

## Prerequisites
Python and python venv module should be installed on your machine. See platform specific details: https://www.python.org/downloads/. For Windows you will require [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) installed, you can also use Docker if available on your system. 

## Setup
Check-out the repository
```
git clone https://github.com/eflows4hpc/ISC23_tutorial.git
```
(you can also download it from https://github.com/eflows4hpc/ISC23_tutorial/archive/refs/heads/main.zip)


Navigate to the hands-on directory, create and activate a Python virtual environment:
```
cd ISC23_tutorial/hands-on/dls
python -m venv tutorial-env
source tutorial-env/bin/activate
```

Install airflow and optional depenendices
```
python -m pip install apache-airflow==2.5.0 virtualenv
```

Configure airflow
```
export AIRFLOW_HOME=`pwd`/airflow 
export AIRFLOW__CORE__DAGS_FOLDER=`pwd`/dags
export AIRFLOW__CORE__LOAD_EXAMPLES=False
airflow db init 
```

Add admin user to the airflow (this is optional, otherwise the admin user with random password will be added automatically)
```
airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
```

To start airflow in standalone mode call:
```
airflow standalone
```

and go to http://localhost:8080


## Projects
There are three projects you can select from. The scaffoldings for the project are provided and marked with the tag *project*. In the code there are suggestions and some places marked to be fixed. Projects

1. hello_world (the easiest project, accepts parameter and print greetings out)
2. temp_pred (predict air temperature for given location)
3. waterlevel (retrieve water level value, store in local database)

There are also solutions for the projects in the *solution* folder. You can peek inside if you stuck.

## Docker setup

Check-out the repository
```
git clone https://github.com/eflows4hpc/ISC23_tutorial.git
```
(you can also download it from https://github.com/eflows4hpc/ISC23_tutorial/archive/refs/heads/main.zip)

Get apache airflow image

```
docker pull apache/airflow:latest
```

Start in standalone mode

```
cd ISC23_tutorial/hands-on/dls
docker run -p 8080:8080 -v `pwd`/dags:/opt/airflow/dags apache/airflow:latest standalone
```

wait a little bit get the admin password and go to localhost:8080




