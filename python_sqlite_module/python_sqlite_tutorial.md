# Python SQLite Module (import sqlite)

In this Python SQLite tutorial, we will be going over a complete introduction to the sqlite3 built-in module within Python. SQLite allows us to quickly get up and running with databases, without spinning up larger databases like MySQL or Postgres. We will be creating a database, creating a table, insert, select, update, and delete data.
A prior knowledge of SQL is required for this tutorial. Let's get started... 

## Connection Object

```
conn = sqlite3.connect(':memory:')  # in memory database

conn = sqlite3.connect('employee.db')  # Database in persistence storage.
```

an in-memory database is a database that keeps the whole dataset in RAM. What does that mean? It means that each time you query a database or update data in a database, you only access the main memory. So, there’s no disk involved into these operations. And this is good, because the main memory is way faster than any disk. A good example of such a database is Memcached.

with just an in-memory database, there’s no way out. A machine is down — the data is lost. Forget about it.

## Cursor

To execute SQL statements, a work area is used by the sqlite engine for its internal processing and storing the information. This work area is private to SQL’s operations. The ‘Cursor’ is the SQL construct that allows the user to name the work area and access the stored information in it.

```
c = conn.cursor()
```

## Executing SQL Commands

```
syntax: c.execute(<SQL Command>)
```

## Creating a Table

```
c.execute(""" CREATE TABLE employees (
            first TEXT,
            last TEXT,
            pay INTEGER
            ) """)
            
conn.commit()  # The changes created by the statement will become visible after this command.
conn.close()  # Closing the connection.
```

**COMMIT:** The COMMIT command is used to close out the current transaction and commit the changes to the database. Once the COMMIT command executed successfully then all the changes are saved to database and become visible to other clients.

Datatypes in SQLite:



* **NULL**: The value is a NULL value.

* **INTEGER**: The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.

* **REAL**: The value is a floating point value, stored as an 8-byte IEEE floating point number.

* **TEXT**: The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).

* **BLOB**: The value is a blob of data, stored exactly as it was input.

For more information regarding datatypes: [Official SQLite Docs](https://www.sqlite.org/datatype3.html)

## Adding Data into employees Table

```
c.execute("INSERT INTO employees VALUES('Ujjwal', 'Raizada', 50000)")
```

## Querying the Database (Extracting data from tables)


To retrieve data after executing a SELECT statement, you can either treat the cursor as an iterator, call the cursor’s fetchone() method to retrieve a single matching row, or call fetchall() to get a list of the matching rows.

* **fethchone()** : Get the next row in our result as a tuple.
* **fetchmany(<no. of rows>)** : Returns the no. of rows as a list. Parameter: No. of rows.
* **fetchall()** : Returns the remaining rows as a list.

```
c.execute("SELECT * FROM employees WHERE last='Raizada'")  # Hardcoded query
print(c.fetchone())  # OUTPUT: ('Ujjwal', 'Raizada', 50000)
```

## Building SQL query from Python Variables

Usually your SQL operations will need to use values from Python variables. You shouldn’t assemble your query using Python’s string operations because doing so is insecure; it makes your program vulnerable to an SQL injection attack.

Instead, use the DB-API’s parameter substitution. Put ? as a placeholder wherever you want to use a value, and then provide a tuple of values as the second argument to the cursor’s execute() method. 

```
first_name = "Mike"
last_name = "Shinoda"
pay = 70000

c.execute("INSERT INTO employees VALUES(?, ?, ?)", (first_name, last_name, pay))
# Second Argument is a Tuple of values.

```
Other Method:
```
first_name = "Brad"
last_name = "Delson"
pay = 75000

c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", 
    {'first': first_name, 'last': last_name, 'pay': pay})
    
# Second Argument is a dictionary here.
```

The second method according to me is lot more readable as compared to the first method.


## Note
1. We can use in memory database when practicing, as it will create a new instance at every run, so we won't get errors <br>
like ```'this table already exists'``` etc.
2. Official Python Docs: [Python SQLite3](https://docs.python.org/3.8/library/sqlite3.html)
3. Official SQLite Docs: [SQLite](https://www.sqlite.org/index.html)


### Complete Example (Using Classes): [Example](sqlite_example_using_classes.md)

<br><br><br>


