"""
Project: Hello world

Take name and use it in the greetings printed to the output. 

Suggestion:
-check other dags in the folder to see how to handle dag parameters
"""

import pendulum

from airflow.decorators import dag, task


@dag(
    schedule=None,
    catchup=False,
    start_date=pendulum.datetime(2023, 4, 1, tz='UTC'),
    params={},
    tags=['project']
)
def hello_world():
    @task
    def print_hello():
        name = 'jj'
        print(f"Hello, world! Nice to meet you {name}!")

    print_hello()

dag = hello_world()
