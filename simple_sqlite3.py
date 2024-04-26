import sqlite3
from typing import Any, List, Dict

class DatabaseInteractions:
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.conn = sqlite3.connect(self.db)
        return self

    def __exit__(self):
        self.conn.close()

    def create_table(self, table: str, *columns: str) -> None:
        with self.conn:
            column_defs = ', '.join([f'{col.upper().replace(" ", "_")} TEXT' for col in columns])
            self.conn.execute(f"CREATE TABLE IF NOT EXISTS {table.upper()} ({column_defs})")

    def insert_record(self, table: str, *records: List[Any]) -> None:
        with self.conn:
            column_names = ', '.join(records[0].keys())
            placeholders = ', '.join(['?' for _ in records[0]])
            query = f"INSERT INTO {table.upper()} ({column_names}) VALUES ({placeholders})"
            self.conn.executemany(query, [tuple(record.values()) for record in records])

    def delete_table(self, *tables: str) -> None:
        with self.conn:
            for table in tables:
                self.conn.execute(f"DROP TABLE IF EXISTS {table.upper()}")

    def edit_record(self, table: str, oid: int, **updates: Dict[str, Any]) -> None:
        with self.conn:
            update_str = ', '.join([f"{key.upper().replace(' ', '_')}=?" for key in updates.keys()])
            query = f"UPDATE {table.upper()} SET {update_str} WHERE OID=?"
            self.conn.execute(query, tuple(updates.values()) + (oid,))

    def delete_record(self, table: str, **conditions: Dict[str, Any]) -> None:
        with self.conn:
            condition_str = ' AND '.join([f"{key.upper().replace(' ', '_')}=?" for key in conditions.keys()])
            query = f"DELETE FROM {table.upper()} WHERE {condition_str}"
            self.conn.execute(query, tuple(conditions.values()))

    def query_records(self, *tables: str) -> List[List[Any]]:
        results = []
        with self.conn:
            for table in tables:
                cursor = self.conn.execute(f"SELECT * FROM {table.upper()}")
                results.extend(cursor.fetchall())
        return results

    def query_tables(self) -> List[str]:
        with self.conn:
            cursor = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
            return [row[0] for row in cursor.fetchall()]

    def reset_all(self) -> None:
        with self.conn:
            tables = self.query_tables()
            for table in tables:
                self.conn.execute(f"DELETE FROM {table.upper()}")

    def delete_all_content(self) -> None:
        with self.conn:
            tables = self.query_tables()
            for table in tables:
                self.conn.execute(f"DROP TABLE IF EXISTS {table}")

def main():
    db = "Database/example.db"

    #Create Table
    with DatabaseInteractions(db) as di:
        di.create_table('students','id','name','age')

    #Insert Record
    with DatabaseInteractions(db) as di:
        di.insert_record("students", {"id": 1, "name": "Alice", "age": 25})
        di.insert_record("students", {"id": 2, "name": "Bob", "age": 30})
    
    #Query Records In A Table
    with DatabaseInteractions(db) as di:
        print(di.query_records("students"))
    #Edit Record
    with DatabaseInteractions(db) as di:
        di.edit_record("students",1,name="Alice Smith")

    #Delete Record
    with DatabaseInteractions(db) as di:
        di.delete_record("students",id=2)

    #Delete Table
    with DatabaseInteractions(db) as di:
        di.delete_table("students")

    #Reset All Tables
    with DatabaseInteractions(db) as di:
        di.reset_all()

    #Delete All Content From Database
    with DatabaseInteractions(db) as di:
        di.delete_all_content()
    
    #Query All Tables In Database
    with DatabaseInteractions(db) as di:
        print(di.query_tables())

if __name__ == "__main__":
    main()