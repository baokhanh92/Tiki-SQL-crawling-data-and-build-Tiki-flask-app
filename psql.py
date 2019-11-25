import pandas as pd
import requests
import psycopg2
from bs4 import BeautifulSoup

def get_connection():
    connection = psycopg2.connect(user = "khanh",
                                  password = '123456',
                                  port = "5432",
                                  database = "khanhdb")
    return connection


print(get_connection())