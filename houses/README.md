# Houses
Implement a program to import student data into a database, and then produce class rosters.


### Specification
In **import.py**, write a program that imports data from a CSV spreadsheet.
- Our program should accept the name of a CSV file as a command-line argument.
  - If the incorrect number of command-line arguments are provided, our program should print an error and exit.
  - Assume that the CSV file will exist, and will have columns name, house, and birth.
- For each student in the CSV file, insert the student into the students table in the students.db database.
 -While the CSV file provided to us has just a name column, the database has separate columns for first, middle, and last names. We’ll thus want to first parse each name and separate it into first, middle, and last names. We may assume that each person’s name field will contain either two space-separated names (a first and last name) or three space-separated names (a first, middle, and last name). For students without a middle name, we should leave their middle name field as NULL in the table.

In **roster.py**, write a program that prints a list of students for a given house in alphabetical order.

- Our program should accept the name of a house as a command-line argument.
  - If the incorrect number of command-line arguments are provided, our program should print an error and exit.
- Our program should query the students table in the students.db database for all of the students in the specified house.
- Our program should then print out each student’s full name and birth year (formatted as, e.g., Harry James Potter, born 1980 or Luna Lovegood, born 1981).
  - Each student should be printed on their own line.
  - Students should be ordered by last name. For students with the same last name, they should be ordered by first name.


### Reference
<a href="https://cs50.harvard.edu/x/2020/">CS50 - Harvard</a>
