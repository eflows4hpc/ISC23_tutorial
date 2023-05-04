from airflow.decorators import dag, task
from airflow.models.param import Param
import pendulum


@dag(
    schedule=None,
    catchup=False,
    start_date=pendulum.datetime(2023, 4, 1, tz="UTC"),
    params={
    		'name': Param('John', type='string'),
            }
)
def hello_world():

    @task
    def print_hello(**context):
        params = context['params']
        name = params.get('name')
        print(f"Hello, world! Nice to meet you {name}!")


    print_hello()

dag = hello_world()
