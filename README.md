# LiteDB

LiteDB is a lightweight and easy-to-use Python library for simplifying SQLite3 database interactions.

## Features
- **Simple Interface:** EasyDB offers a straightforward interface for creating tables, inserting records, querying data, and more.
- **Efficient:** With optimized code and minimal overhead, EasyDB ensures fast database operations.
- **Context Manager Support:** EasyDB supports the context manager protocol, allowing for easy and safe management of database connections.
- **Flexible:** EasyDB supports flexible querying and record manipulation, making it adaptable to various use cases.

## Usage

Creating a Database Connection

```python
db_file = "example.db"
with LieDB(db_file) as db:
    # Your database interactions here...
```
Creating a Table

```python
with LiteDB(db_file) as db:
    db.create_table("students", "id", "name", "age")

#(TableName, *ColumnName(s))
```
Inserting a Record

```python
with LiteDB(db_file) as db:
    db.insert_record("students", {"id": 1, "name": "Alice", "age": 25})

#(TableName, **{ColumnName: Value})
```

Querying Records

```python
with LiteDB(db_file) as db:
    records = db.query_records("students")
    for record in records:
        print(record)

#Query all records from a single table
```

Deleting a Record

```python
with LiteDB(db_file) as db:
    db.delete_record("students", id=1)

#Deleting a record with id=1 from the "students" table
```

Editing a Record

```python
with LiteDB(db_file) as db:
    db.edit_record("students", 1, name="Alice Smith")

#Edit the record with id=1 in the "students" table, changing the name to "Alice"
```

Deleting a Table

```python
with LiteDB(db_file_ as db:
    db.delete_table("students")
```

Querying All Tables

```python
with LiteDB(db_file) as db:
    tables = db.query_tables()
    for table in tables:
        print(table)

#Query all tables in the database
```

Resetting All Tables

```python
with LiteDB(db_file) as db:
    db.reset_all()

#Resets all tables, removes all records
```

Deleting All Content from the Database

```python
with LiteDB(db_file) as db:
    db.delete_all_content()

#Deletes all data in the database file
```

## Contributing

Contributions to LiteDB are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/karlbk/LiteDB/tree/main).
