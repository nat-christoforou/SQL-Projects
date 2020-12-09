from cs50 import SQL
from sys import argv, exit
import csv

# Check if the program is executed with the correct number of command-line arguments
if len(argv) != 2:
    print("Incorrect number of command-line arguments")
    exit(1)

# Connect to database
db = SQL("sqlite:///students.db")

# Open CSV file
# https://datasets.imdbws.com/title.basics.tsv.gz
with open(argv[1], "r") as characters:
    # Create DictReader
    reader = csv.DictReader(characters)

    # Iterate over CSV file
    for row in reader:
        # Check if there is a middle name
        if len(row['name'].split()) == 3:
            first, middle, last = tuple(row['name'].split())

            # Insert character by substituting values into each ? placeholder
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                        first, middle, last, row['house'], row['birth'])
        else:
            first, last = tuple(row['name'].split())
            # Insert character by substituting values into each ? placeholder
            db.execute("INSERT INTO students (first, last, house, birth) VALUES(?, ?, ?, ?)",
                        first, last, row['house'], row['birth'])