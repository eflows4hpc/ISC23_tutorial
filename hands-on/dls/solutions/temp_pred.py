"""
Example pipeline for predicting air temperature

The source of the data is Open Meteo site
https://open-meteo.com/en/docs#api_form

(please be gentle with the API)

 The goal of this task is to get the data and make a prediction of the air temperature for the next hour

"""



import requests
import pendulum

from airflow.decorators import dag, task

@dag(
    schedule="@hourly", catchup=False, start_date=pendulum.datetime(2023, 1, 3, tz="UTC"),
)
def weather_predictor():

    @task(multiple_outputs=True)
    def get_temperatures():
        url = 'https://api.open-meteo.com/v1/forecast?latitude=53.55&longitude=9.99&hourly=temperature_2m'
        ret = requests.get(url)
        if not ret.ok:
            print("Error fetching data", ret.content)
            return -1
        
        return ret.json()['hourly']
    
    @task.virtualenv(task_id='make_prediction', requirements=['pandas==1.5.3', 'scikit-learn==1.2.2'], system_site_packages=False)
    def make_prediction(values):
        # to be sure to import from venv
        from sklearn.linear_model import LinearRegression
        import pandas as pd
        import numpy as np

        model = LinearRegression()

        X_train = (pd.to_datetime(values['time']).astype('int64')// 10 ** 9).to_numpy().reshape(-1, 1)
        y_train = np.array(values['temperature_2m'])

        model.fit(X_train, y_train)

        next_hour = model.predict([X_train[-1]+3600])
        print('-'*20)
        print(f"Temperature next hour will be: {next_hour[0]}")
        print('-'*20)

    vals = get_temperatures()
    make_prediction(vals)

weather_predictor()