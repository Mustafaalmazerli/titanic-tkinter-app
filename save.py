import sqlite3

def save_to_db(df, db_name, table_name):
   
    try:
        connection = sqlite3.connect(db_name)
        df.to_sql(table_name, connection, if_exists='replace', index=False)
        connection.commit()
        connection.close()
        print(f"Data successfully saved to {table_name} in {db_name}")

    except Exception as e:
        print(f"Error saving data to database: {e}")
        raise


 
     # Sparar den bearbetade Titanic-train.csv-datan till en SQLite-databas.
