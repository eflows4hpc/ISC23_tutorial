from airflow.providers.sqlite.hooks.sqlite import SqliteHook
from airflow.decorators import dag, task
from airflow.models.param import Param
import pendulum

@dag(
        schedule=None,
        catchup=False,
        start_date=pendulum.datetime(2023,1,4, tz='UTC'),
        params={
            'name': Param('John', type='string'),
            'age': Param(16, type='integer', minimum=16)
        },
)
def db_dag():

    @task
    def setup_db():
        hook = SqliteHook() # it will use sqlite_default connection by default

        hook.run(r"""
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INT PRIMARY KEY,
            first_name TEXT,
            age INT
        );
        """
        )

    @task
    def insert_data(**context):
        hook = SqliteHook(conn_name_attr='sqlite_default')
        parms = context['params']
        name = parms['name']
        age = parms['age']

        rows = [(name, age)]
        hook.insert_rows(table="Customers", rows=rows, target_fields=["first_name", "age"])

    setup_db()
    insert_data()

dag = db_dag()
