from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    create,
    read,
    update,
    delete,
    count_survivors_by_class,
    avg_fare_by_embarkation,
)

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# CRUD and Additional Queries
print("\nPerforming CRUD operations and SQL queries...")

# Create
print("\nCreating a new entry...")
create()

# Read
print("\nReading all entries...")
read()

# Update
print("\nUpdating an entry...")
update()

# Read again to confirm update
print("\nReading all entries after update...")
read()

# Delete
print("\nDeleting an entry...")
delete()

# Read again to confirm delete
print("\nReading all entries after delete...")
read()

# Additional Queries
print("\nCounting survivors by passenger class...")
count_survivors_by_class()

print("\nCalculating average fare by embarkation port...")
avg_fare_by_embarkation()
