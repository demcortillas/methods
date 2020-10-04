import pandas as pd
import sqlite3

def sql2df(link_bd,query=None):
    con = sqlite3.connect(link_bd)
    df = pd.read_sql_query(str(query),con)
    con.close()
    return df