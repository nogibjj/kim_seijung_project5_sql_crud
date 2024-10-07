"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,
ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv

def load(dataset="data/titanic.csv"):
    """Transforms and Loads Titanic data into the local SQLite3 database"""

    with open(dataset, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        conn = sqlite3.connect('TitanicDB.db')
        c = conn.cursor()
        
        # Drop existing table if it exists
        c.execute("DROP TABLE IF EXISTS Titanic")

        # Create table schema based on Titanic dataset structure
        c.execute(
            """
            CREATE TABLE Titanic (
                PassengerId INTEGER,
                Survived INTEGER,
                Pclass INTEGER,
                Name TEXT,
                Sex TEXT,
                Age REAL,
                SibSp INTEGER,
                Parch INTEGER,
                Ticket TEXT,
                Fare REAL,
                Cabin TEXT,
                Embarked TEXT
            )
            """
        )
        
        # Prepare data for insertion
        data = []
        for row in reader:
            data.append((
                int(row['PassengerId']),
                int(row['Survived']),
                int(row['Pclass']),
                row['Name'],
                row['Sex'],
                float(row['Age']) if row['Age'] else None,
                int(row['SibSp']),
                int(row['Parch']),
                row['Ticket'],
                float(row['Fare']),
                row['Cabin'],
                row['Embarked']
            ))
        
        # Insert data into the database
        c.executemany(
            "INSERT INTO Titanic VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
            data
        )
        
        conn.commit()
        conn.close()
    
    return "TitanicDB.db"

if __name__ == "__main__":
    load()
