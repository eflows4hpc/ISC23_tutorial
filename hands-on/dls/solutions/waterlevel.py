"""
Example pipeline for retrieving data about water level in rivers

The source of the data is WSV site, e.g. url
 https://www.pegelonline.wsv.de/webservices/files/Wasserstand+Rohdaten/RHEIN/DÜSSELDORF

 The goal of this task is to get data (published every hour), apply some transformation (e.g. hourly mean value), 
 and upload it to a local database.
"""

import numpy as np
import pandas as pd
import pendulum

from airflow.decorators import dag, task
from airflow.providers.sqlite.hooks.sqlite import SqliteHook



url_template = "https://www.pegelonline.wsv.de/webservices/files/Wasserstand+Rohdaten/RHEIN/D%C3%9CSSELDORF/{day}.{month}.{year}/down.csv"


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


@dag(
    schedule="@daily", catchup=True, start_date=pendulum.datetime(2023, 1, 3, tz="UTC"),
)
def waterg():
    @task
    def get_url(ds=None):
        year, month, day = ds.split("-")
        url = url_template.format(day=day, month=month, year=year)
        print("Url is:", url)
        return url

    @task(multiple_outputs=True)
    def convet_measurements(url):

        print(f"Getting the data from: {url}")
        df = (
            pd.read_csv(
                url, skiprows=1, names=["time", "value"], sep=";", encoding="utf-8"
            )
            .replace("XXX,XXX", pd.NA)
            .dropna()
            .pipe(split_time)
            .groupby("hour")
            .agg({"value": np.mean})
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


waterg()
