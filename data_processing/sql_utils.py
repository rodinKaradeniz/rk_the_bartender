import os.path
import sqlite3
import pandas as pd

def initialize_cocktails_db():
    # TODO: test this

    db_name = "db/sql/cocktails.db"

    conn = sqlite3.connect(db_name) 
    c = conn.cursor()

    columns = [
        "cocktail_name TEXT",
        "alcoholic TEXT",
        "image_url TEXT",
        "glass_type TEXT",
        "recipe TEXT"
    ] + [f"ingredient{i}" for i in range(1,16)] + [f"measure{i}" for i in range(1,16)]

    create_table_cmd = f"CREATE TABLE IF NOT EXISTS cocktail ({','.join(columns)})"
    c.execute(create_table_cmd)
                        
    conn.commit()


def upload_cocktails_db(df):
    # TODO: test this

    # Check if database exists, then connect
    db_name = "db/sql/cocktails.db"
    if os.path.isfile(db_name):
        conn = sqlite3.connect(db_name)
    else:
        raise Exception("Database does not exist")

    # Upload dataframe to sql
    df.to_sql(db_name, con=conn, schema='cocktail', index=True, if_exists='append')


def load_cocktails_db(ticker: str, debug=False):
    # TODO: Fix and finish this

    db_name = "db/sql/cocktails.db"
    if os.path.isfile(db_name):
        conn = sqlite3.connect(db_name)

        sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM products
                               ''', conn)

        df = pd.DataFrame(sql_query, columns = ['product_id', 'product_name', 'price'])
        print(df)

    else:
        raise Exception("Database does not exist")
    

if __name__ == "__main__":
    # TODO: Test functions, create DB, complete load_db function
    print(1)
