from sqlalchemy import Table, Float, Column, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy import insert
import csv

engine = create_engine('sqlite:///hawaii.db')

meta = MetaData()

stations = Table(
   'Stations', meta,
   Column('id', Integer, primary_key=True),
   Column('station', String),
   Column('latitude', String),
   Column('longitude', String),
   Column('elevation', String),
   Column('name', String),
   Column('country', String),
   Column('state', String),
)

measures = Table(
   'Measures', meta,
   Column('id', Integer, primary_key=True),
   Column('station', String),
   Column('date', String),
   Column('precip', String),
   Column('tobs', String)
)

meta.create_all(engine)
print(engine.table_names())

conn = engine.connect()

with open("clean_stations.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        stmt = insert(stations).values(
            station=row["station"],
            latitude=float(row["latitude"]),
            longitude=float(row["longitude"]),
            elevation=float(row["elevation"]),
            name=row["name"],
            country=row["country"],
            state=row["state"]
        )
        conn.execute(stmt)

with open("clean_measure.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        stmt = insert(measures).values(
            station=row["station"],
            date=row['date'],
            precip=row['precip'],
            tobs=row["tobs"]
        )
        conn.execute(stmt)