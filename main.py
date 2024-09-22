import logging
from read import read_data
from process import process_data
from save import save_to_db
import schedule
import time
import pandas as pd 
def main():
    
    # Huvudfunktionen för att bearbeta och spara Titanic train.csv-data.
    
    try:
        # Ange filvägen till Titanic train.csv-filen
        file_path = 'C:/Users/musta/OneDrive/Skrivbord/ds23_f-rdjupad_python-main/kunskapskontroll_2/train.csv'
        db_name = 'titanic_database.db'
        table_name = 'ReducedTitanicData'  

        # Läs in data
        df = read_data(file_path)
        logging.info("Data successfully read.")

        # Bearbeta och filtrera data, minska kolumner
        processed_data = process_data(df)
        logging.info("Data successfully processed.")

        # Spara till SQL-databas
        save_to_db(processed_data, db_name, table_name)
        logging.info("Data successfully saved to the database.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

def job():
    """
    Den schemalagda uppgiften som körs dagligen.
    """
    print("Running daily job...")
    main()

if __name__ == "__main__":
    # Konfigurera logging
    logging.basicConfig(filename='titanic_data.log', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Schemalägg exekvering varje dag kl 12:00
    schedule.every().day.at("10:50").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
