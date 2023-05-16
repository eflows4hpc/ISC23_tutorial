"""
Solution: Example pipeline for retrieving data about water level in rivers

The source of the data is WSV site, e.g. url
https://www.pegelonline.wsv.de/webservices/files/Wasserstand+Rohdaten

(this allows you to select a river to download raw data from, choose a river and location), e.g.

 https://www.pegelonline.wsv.de/webservices/files/Wasserstand+Rohdaten/RHEIN/DÜSSELDORF

 The goal of this task is to get data (published every hour), apply some transformation (e.g. hourly mean value), 
 and upload it to a local database.

 Suggestions:
 -the down.csv has following format:
 "04.04.2023";"Standort Köln";"RHEIN";"DÜSSELDORF";"2750010";"W_O";"cm";"524";"04.04.2023";"12:40";"PNP";"24,529"
"00:15";"514"
"00:30";"514"
"00:45";"514"
...
you can skip the header line, and use ; as separator and parse the numbers (pandas can download directly from an url)
-note that sometimes values are missing and replaced with XXX,XXX
-the time should be split in two (hours:minutes), check pd.Series.str.split(delimiter, expand=True)
-also the values should be converted to numeric (pd.to_numeric)
-to get the current date in a airflow way you can use ds argument which is injected in each task 
-check other dags to see how to connect to database (use sqlite default connection)
-use virtualenv  
 
"""
from airflow.decorators import dag, task
from airflow.providers.sqlite.hooks.sqlite import SqliteHook
from airflow.utils.dates import days_ago

url_template = "https://www.pegelonline.wsv.de/webservices/files/Wasserstand+Rohdaten/RHEIN/D%C3%9CSSELDORF/{day:02d}.{month:02d}.{year}/down.csv"


@dag(
    schedule="@daily", catchup=False, start_date=days_ago(2),tags=['project']
)
def waterg():
    @task
    def get_url(ds=None):
        year, month, day = ds.split("-")
        url = url_template.format(day=int(day), month=int(month), year=year)
        print("Url is:", url)
        return url

    @task.virtualenv(
        requirements=["pandas==1.5.3"],
        system_site_packages=False,
        multiple_outputs=True,
    )
    def convet_measurements(url):
        import pandas as pd

        # virtualenv has also some drawbacks
        def convert(x, year, month, day):
            return tuple([year, month, day, x[0], x[1]])

        def split_time(col):
            col[["hour", "min"]] = (
                col["time"]
                .str.split(pat=":", expand=True)
                .rename({0: "hour", 1: "minute"}, axis=1)
            )
            col["value"] = col["value"].apply(pd.to_numeric)
            return col

        print(f"Getting the data from: {url}")
        df = (
            pd.read_csv(
                url, skiprows=1, names=["time", "value"], sep=";", encoding="utf-8"
            )
            .replace("XXX,XXX", pd.NA)
            .dropna()
            .pipe(split_time)
            .groupby("hour")
            .agg({"value": "mean"})
        )

        print(f"Retrieved {len(df)} measurements")

        return df.value.to_dict()

    @task
    def store_in_db(values, ds=None):
        year, month, day = ds.split("-")

        hook = SqliteHook()
        hook.run(
            r"""
        CREATE TABLE IF NOT EXISTS Measurements (
            year INT,
            month INT,
            day INT,
            hour INT,
            value INT
        );
        """
        )
        rows = [(year, month, day, hour, val) for hour, val in values]
        hook.insert_rows(
            "Measurements",
            rows=rows,
            target_fields=["year", "month", "day", "hour", "value"],
        )

    url = get_url()
    vals = convet_measurements(url=url)
    store_in_db(values=vals)


dag = waterg()
