"""
Project: Example pipeline for predicting air temperature

The source of the data is Open Meteo site
https://open-meteo.com/en/docs#api_form

(please be gentle with the API)

Request for particular location returns json:

{
    "latitude":53.54,"longitude":10.0,
    .....
    "hourly":{
        "time":["2023-05-04T00:00","2023-05-04T01:00",....],
        "temperature_2m":[4.9,4.5,4.0,....]
        }
}


 The goal of this task is to get the data and make a prediction of the air temperature for the next hour.

 Suggestions:
 -first task connects to service and get the data
 -second task uses simple model (e.g. scikit-learn LinearRegresion to make prediction)
 -you will need to convert the time into timestamp, e.g. dateutil.parser.parse(x).timestamp()

"""


import requests

from airflow.decorators import dag, task
from airflow.utils.dates import days_ago


@dag(
    schedule=None, catchup=False, start_date=days_ago(1), tags=['project']
)
def weather_predictor():
    @task(multiple_outputs=True)
    def get_temperatures():
        # fix url
        url = ""
        ret = requests.get(url)
        if not ret.ok:
            print("Error fetching data", ret.content)
            return -1

        return ret.json()["hourly"]

    @task.virtualenv(
        task_id="make_prediction",
        requirements=["numpy", "python-dateutil", "scikit-learn"],
        system_site_packages=False,
    )
    def make_prediction(values):
        # to be sure to import from venv
        import numpy as np
        
        # get scikit-model here
        model = []
        # convert dates to timestamps here:
        X_train = np.array(
           
        ).reshape(-1, 1)
        y_train = np.array(values["temperature_2m"])

        model.fit(X_train, y_train)

        # fix the time value for the prediction
        next_hour = model.predict()
        print("-" * 20)
        print(f"Temperature next hour will be: {next_hour[0]}")
        print("-" * 20)

    vals = get_temperatures()
    make_prediction(vals)


weather_predictor()
