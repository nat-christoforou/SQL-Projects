from cs50 import SQL
from sys import argv, exit
import csv

# Check if the program is executed with the correct number of command-line arguments
if len(argv) != 2:
    print("Incorrect number of command-line arguments")
    exit(1)

# Connect to databasse
db = SQL("sqlite:///students.db")

# Query database
for row in db.execute("SELECT * FROM students WHERE house = (?) ORDER BY last, first", argv[1]):

    first = row['first']
    middle = row['middle']
    last = row['last']
    birth = row['birth']

    # Check if there is a middle name or not
    if middle:
        print("{} {} {}, born {}".format(first, middle, last, birth))
    else:
        print("{} {}, born {}".format(first, last, birth))

