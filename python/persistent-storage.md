# Persistent storage

There are several different ways we can store data using Python:

## Text Files
- **Pros**
  - Simple to implement
  - Human-readable
- **Cons**
  - Not efficient for large data
  - Not suitable for complex data structures
- **Example**
  ```python
  with open('data.txt', 'w') as f:
      f.write(str(data))
  ```

## Binary Files (pickle)
- **Pros**
  - Efficient for large data
  - Can handle complex data structures
- **Cons**
  - Not human-readable
  - Data can only be read by Python
- **Example**
  ```python
  import pickle
  with open('data.pkl', 'wb') as f:
      pickle.dump(data, f)
  ```

## Databases (SQLAlchemy)
- **Pros**
  - Very efficient for large data
  - Supports complex queries and transactions
- **Cons**
  - More complex to set up and use
  - Requires a running database server (except for SQLite)
- **Example**
  ```python
  from sqlalchemy import create_engine
  engine = create_engine('sqlite:///data.db')
  session = Session(bind=engine)
  session.add(data)
  session.commit()
  ```

## JSON Files
- **Pros**
  - Good compromise between simplicity and efficiency
  - Human-readable
  - Data can be read by many programming languages
- **Cons**
  - Not as efficient as binary files or databases for large data
- **Example**
  ```python
  import json
  with open('data.json', 'w') as f:
      json.dump(data, f)
  ```

## CSV Files
- **Pros**
  - Simple and efficient for tabular data
  - Data can be easily imported into other programs like Excel
- **Cons**
  - Only suitable for tabular data
- **Example**
  ```python
  import csv
  with open('data.csv', 'w', newline='') as f:
      writer = csv.writer(f)
      writer.writerows(data)
  ```