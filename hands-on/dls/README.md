# Data Logistics Hands-on

This part will cover the introduction to Airflow and creation of data pipelines


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

To start airflow in standalone mode call:
```
airflow standalone
```

and go to http://localhost:8080


