# **Zoo Employee Credential Database**

## About
This project demonstrates my skills and capabilities in database design, creation, manipulation, and querying. For this enhancement, I created a database using text files that were provided in IT-145: Foundation in Application Development for a zoo employee authentication program. The provided file for IT-145 were a list of access for administrators, a list of access for veterinarians, a list of access for zookeepers, and a file including employee names, login credentials, and role/job title. I also demonstrated my ability to add content to the database, add columns to the database, delete data from the database, and write commonly used queries.  Please read the Narrative below for more detail on my enhancements for this project. 

## Code
[Click Here](https://github.com/troyrushing/troyrushing.github.io/blob/master/sqlfiles.zip) to download the SQL files used to Create, Read, Update, Delete, and Query the database. Once the page opens, click the "View Raw" link to start the download.

## Narrative
I.	Databases

A.	Artifact

The artifact for my database enhancement is a combination of two course. I used the SQL knowledge gained through my course work in DAD-220 to create a database for the authentication program created in IT-145. For IT-145 we were provided various types of data in .txt that we were to use to create an authentication program including a login, and limiting access based on the users role or job title.


B.	Justification

The provided file for IT-145 were a list of access for administrators, a list of access for veterinarians, a list of access for zookeepers, and a file including employee names, login credentials, and role/job title. In a true business environment, this type of data would necessarily be contained in a secure database. This enhancement demonstrates a real world scenario of creating a necessary database for a business. Further, it demonstrates the ability to execute database function such as populating tables, updating data, deleting data, and using queries to display only desired data. These are necessary skills for someone entering into a new career that would involve database work or database management.


C.	Objective Outcome

This enhancement met the objective planned in the submitted plan in module 1. This enhancement includes a sql file (create.sql) to create the database, tables, and populate the tables with the provided data for IT-145, a sql file (update.sql) to update a table adding a new column and adding an additional employee, a sql file (delete.sql) to delete the newly added employee, a sql file (queries.sql) which runs 10 different queries that one might want to use to access specific data of data in a specific format, and a Word document with screenshots of the results of each sql file. These activities were precisely what I planned in my module one enhancement plan.


D.	Reflection

In creating this enhancement, I was given the opportunity to refresh my MySQL skills. I had not used these skills since completing DAD-220 in term 19EW5. In DAD-220, we briefly touched on the concept of “foreign keys” in MySQL databases, but did not go into detail or practice them. I had to do some research on how to properly implement foreign keys on primary keys from other tables within the database to make the tables relational. This took some trial and error to properly implement. Using the foreign keys established in the “employees_jobs” table, I was able to write an INNER JOIN query that displayed data from the two other tables (employees table and jobs table).


