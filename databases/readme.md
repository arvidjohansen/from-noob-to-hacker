---
marp: true
class: invert
---



# Python SQLite3 Cheatsheet

Here are some examples using SQLite3 with Python

## Import SQLite3 Module
```python
import sqlite3
```

---

## Connect to Database
```python
conn = sqlite3.connect('database.db')
```

---

## Create a Cursor Object
```python
cursor = conn.cursor()
```

## Create Table
```python
cursor.execute('''
    CREATE TABLE IF NOT EXISTS table_name (
        column1 datatype1,
        column2 datatype2,
        ...
    )
''')
conn.commit()
```

---

## Insert Data
```python
cursor.execute('''
    INSERT INTO table_name (column1, column2, ...) 
    VALUES (value1, value2, ...)
''')
conn.commit()
```

---

## Query Data
```python
cursor.execute('SELECT * FROM table_name')
rows = cursor.fetchall()
for row in rows:
    print(row)
```

---

## Update Data
```python
cursor.execute('''
    UPDATE table_name 
    SET column1 = new_value1 
    WHERE condition
''')
conn.commit()
```

---

## Delete Data
```python
cursor.execute('DELETE FROM table_name WHERE condition')
conn.commit()
```

---

## Commit and Close Connection
```python
conn.commit()
conn.close()
```

---

<style scoped>
    table{
        font-size:90%;
    }
</style>

| Data Type    | Description                          |
|--------------|--------------------------------------|
| `INTEGER`    | Integer                              |
| `REAL`       | Floating-point                       |
| `TEXT`       | Text                                 |
| `BLOB`       | Binary large object                  |
| `NUMERIC`    | Numeric with a fixed precision       |
| `BOOLEAN`    | Boolean (0 for false, 1 for true)    |
| `DATE`       | Date (YYYY-MM-DD)                    |
| `TIME`       | Time (HH:MM:SS)                      |
| `DATETIME`   | Date and time (YYYY-MM-DD HH:MM:SS) |


---

Example

```python
cursor.execute('''
    CREATE TABLE IF NOT EXISTS example_table (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        height REAL,
        is_student BOOLEAN
    )
''')
conn.commit()
```

---

| Property           | Description                                     |
|--------------------|-------------------------------------------------|
| `PRIMARY KEY`      | Uniquely identifies each record in the table    |
| `AUTOINCREMENT`    | Automatically increments the value of the column|
| `NOT NULL`         | Ensures the column cannot contain NULL values   |
| `UNIQUE`           | Ensures all values in the column are unique     |
| `DEFAULT`          | Provides a default value for the column         |
| `CHECK`            | Adds a constraint to check a condition          |
| `FOREIGN KEY`      | Establishes a link between data in two tables   |

---

```py
cursor.execute('''
    CREATE TABLE IF NOT EXISTS example_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER DEFAULT 0,
        height REAL,
        is_student BOOLEAN CHECK (is_student IN (0, 1))
    )
''')
conn.commit()
```

---