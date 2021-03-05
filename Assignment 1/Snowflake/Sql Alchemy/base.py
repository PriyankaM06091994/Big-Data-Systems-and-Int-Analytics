# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#import snowflake.connector as sf

engine = create_engine("snowflake://malpekarpriyanka6:Manisha!1994@tza57982.us-east-1/sevir")

engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")

Session = sessionmaker(bind=engine)

Base = declarative_base()
