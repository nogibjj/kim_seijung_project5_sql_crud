"""Query the database: include CRUD and additional SQL query"""

import sqlite3

def create():
    """Insert a row into the Titanic table."""
    conn = sqlite3.connect("TitanicDB.db")
    cursor = conn.cursor()
    
    query = """
        INSERT INTO Titanic (
            PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, 
            Parch, Ticket, Fare, Cabin, Embarked
        ) VALUES (1001, 1, 1, 'Seijung Kim', 'female', 24.0, 0, 0, 
            'PC 17599', 72.0, 'C85', 'C')
    """
    cursor.execute(query)
    conn.commit()
    
    conn.close()
    return "Create Success"

def read():
    """Select and print all rows from the Titanic table."""
    conn = sqlite3.connect("TitanicDB.db")
    cursor = conn.cursor()
    
    query = "SELECT * FROM Titanic"
    cursor.execute(query)
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    conn.close()
    return "Read Success"

def update():
    """Update a specific row in the Titanic table."""
    conn = sqlite3.connect("TitanicDB.db")
    cursor = conn.cursor()
    
    query = """
        UPDATE Titanic 
        SET Age = 30.0, Fare = 80.0
        WHERE PassengerId = 1001
    """
    cursor.execute(query)
    conn.commit()
    
    conn.close()
    return "Update Success"

def delete():
    """Delete a specific row from the Titanic table."""
    conn = sqlite3.connect("TitanicDB.db")
    cursor = conn.cursor()
    
    query = """
        DELETE FROM Titanic 
        WHERE PassengerId = 1001
    """
    cursor.execute(query)
    conn.commit()
    
    conn.close()
    return "Delete Success"

def count_survivors_by_class():
    """Count the number of survivors by passenger class."""
    conn = sqlite3.connect("TitanicDB.db")
    cursor = conn.cursor()
    
    query = """
        SELECT Pclass, COUNT(*) as SurvivorCount
        FROM Titanic
        WHERE Survived = 1
        GROUP BY Pclass
        ORDER BY Pclass
    """
    cursor.execute(query)
    results = cursor.fetchall()
    
    for result in results:
        print(f"Class {result[0]}: {result[1]} survivors")
    
    conn.close()
    return "Count Survivors by Class Success"

def avg_fare_by_embarkation():
    """Generate average fare by embarkation port."""
    conn = sqlite3.connect("TitanicDB.db")
    cursor = conn.cursor()
    
    query = """
        SELECT 
            Embarked,
            AVG(Fare) as AverageFare
        FROM Titanic
        WHERE Embarked IS NOT NULL
        GROUP BY Embarked
        ORDER BY Embarked
    """
    cursor.execute(query)
    results = cursor.fetchall()
    
    for result in results:
        print(f"Embarked: {result[0]}, Average Fare: {result[1]:.2f}")
    
    conn.close()
    return "Average Fare by Embarkation Success"

# Testing CRUD operations and additional query
if __name__ == "__main__":
    print(create())
    print(read())
    print(update())
    print(read())
    print(delete())
    print(read())
    print(count_survivors_by_class())
    print(avg_fare_by_embarkation())