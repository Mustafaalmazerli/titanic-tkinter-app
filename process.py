import pandas as pd

def process_data(df):
    """
    Bearbetar och formaterar Titanic train.csv-data och minskar datan som sparas.
    """
    try:
        # Konvertera 'Age' till float och hantera saknade värden
        df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
        df['Age'] = df['Age'].fillna(df['Age'].median()).astype(float)  # Konvertera till float

        # Konvertera 'Fare' till float och hantera saknade värden
        df['Fare'] = pd.to_numeric(df['Fare'], errors='coerce')

        # Skapa en ny kolumn 'IsChild' där passagerare under 18 år är markerade som barn
        df['IsChild'] = df['Age'].apply(lambda x: 'Child' if x < 18 else 'Adult')

        # Behåll endast specifika kolumner som är relevanta
        columns_to_keep = ['Survived', 'Pclass', 'Sex', 'Age', 'Fare', 'IsChild']
        df = df[columns_to_keep]

        return df

    except Exception as e:
        print(f"Error during data processing: {e}")
        raise
