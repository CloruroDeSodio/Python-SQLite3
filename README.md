# Python-SQLite3
The idea is simple to manipulate a database with python, in this case as it is my first time it will only be a list of contacts, the database is sqlite3, a "language" extremely similar to sql but it is much faster than this.


## Creation of the database

*The first thing is to download Sqlite3 from the official page the version that the pc supports in my case windows

*The second thing is to play a game of league of legends because... Why not?

*The third thing is to create a folder and create the DaTa.db file that will be the database

*The fourth thing is to download the SQLite and SQLite Viewer extensions from VScode, these will be used to program the database and to see it

* We enter the DaTa.db file and press the "F1" key and look for the option that says "SQL new query"

*With this we can enter our request to the database and to execute it, press "ctrl+shift + q"

This is the database table creation code:

CREATE TABLE contacts(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     INTEGER number,
     Name TEXT,
     Description TEXT
);
This table is made up of the following columns: id, which accepts integer data and auto-increments, telephone number that accepts integer data, name of the owner of the number that only accepts text data, and description, which is a short description to be entered in text type data 👍

*With this and the main.py file in the same folder it should work

## Program
The program is made up of a "login" password, yes, that can be called login, but if you enter the password correctly, you can modify the data, the program is not very safe, but it does what it can and it is appreciated 👍

If the password was correct, the program will be executed that will ask you what action you want to do:

* "y" is for adding data
* "search" is to search for data
* "delete" is to delete data

1) If you chose "y" (add data) It will ask you for the number, name and description of the new number you want to add.

2) If you chose "search" (search data) it will ask you the name of the contact that you want to be displayed in the console and if there is that name it will show it

3) If you chose "delete" (delete data) it will ask you for the name of the contact you want to delete and if there is that name it will delete the data that is in its row
