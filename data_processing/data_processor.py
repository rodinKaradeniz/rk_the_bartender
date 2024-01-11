# Main program that calls the functions to process the raw csv data into a SQLite database.

from data_processing.csv_utils import *
from data_processing.sql_utils import *
import sqlite3


def process_raw_data_into_csv():
    data = pd.read_csv('db/raw/all_drinks.csv', index_col=0)
    new_data = refactor_cocktail_df(data)
    new_data.to_csv('db/processed/cocktails.csv', index=True)


def upload_to_sql():
    pass


def import_from_sql():
    pass


def get_password_hash(username):
    query_file_path = './db/sql_queries/get_user_cred.sql'
    password_hash = execute_query_from_file(query_file_path, get=True, insert=False, data=username)
    return password_hash


def check_password(username: str, password_hash: str) -> bool:
    return password_hash == get_password_hash(username)