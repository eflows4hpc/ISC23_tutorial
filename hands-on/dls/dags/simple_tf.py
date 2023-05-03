from airflow.decorators import dag, task
import pendulum

@dag(
    dag_id="simpleft",
    schedule="@daily",
    catchup=False,
    start_date=pendulum.datetime(2023, 4, 1, tz="UTC"),
)
def simpletf():
    @task
    def task1():
        print("Hello world")
        return "Prompt"

    @task
    def task2(prompt):
        print(prompt)
        return 0
    
    prompt = task1()
    r = task2(prompt)

dag = simpletf()
