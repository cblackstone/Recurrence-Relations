# Recurrence-Relations
This program was created on the Longwood Computer Science lab machines. 

A simple Recurrence Relation program with an html user interface. Program languages used were html, python and c++ to execute the program. 
An SQL database was used to store user given values. 

Flow of the program:
- User inputs their values into the html form and given a confirmation number to user later to obtain their results. 
- Program adds the values to SQL database. (python)
- Python code gets the values from the SQL database and launches the c++ program.
- The c++ program computes the recurrence relation equations with the user given values. 
- The c++ program then creates a textfile containing the users results.

When the user wants to obtain their results they can input a confirmation number into the html form.
If the users results are complete, they will be redirected to page containing the textfile with the results.
If the users results are not complete, they will recieve a message "Results are not complete. Try again later.". 
