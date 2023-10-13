from simple_sqlite3 import *
di = database_interactions(db_)
up = lambda n : str(n).upper().replace(" ","_")

def create_table():
    try:
        x = input("Enter table name: ")
        x1 = input("Enter the number of columns: ").replace(" ","")
        empty = []
        for i in range(0,int(x1)):
            x2 = input("Column name: ")
            empty.append(str(x2))
        di.create_table(up(x),empty)
    except:
        print("-ERROR-")
        start()

    start()

def delete_table():
    try:
        x = input("Enter the number of tables to delete: ").replace(" ","")
        for i in range(0,int(x)):
            x1 = input("Enter table name: ")
            di.delete_table(x1)
    except:
        print("-ERROR-")
        start()
    start()

def query_records():
    try:
        x = input("Enter the number of tables to query records from: ").replace(" ","")
        for i in range(0,int(x)):
            x1 = input("Enter table name: ")
            print(di.query_all([up(x1)]))
    except:
        print("-ERROR-")
        start()

    start()

def insert_record():
    try:
        x = input("Enter the name of the table you want to insert record in: ")
        x1 = database_interactions(db_).get_column_number_from_table(up(x))
        empty = []
        for i in range(0,int(x1)):
            x2 = input("Enter record: ")
            empty.append(str(x2))
        di.insert_record(up(x),empty)
    except:
        print("-ERROR-")
        start()
   
    start()

def delete_record():
    try:
        x = input("Enter table name to delete records from: ")
        x3 = input("Delete with oid(True/False): ")
        x1 = input("Enter number of records to be deleted: ").replace(" ","")
        empty = []
        if x3.upper().replace(" ","")=="TRUE":
            for i in range(int(x1)):
                x2 = input("Enter oid: ")
                empty.append(str(x2))
            di.delete_record(up(x),empty,oids=True)
        if x3.upper().replace(" ","")=="FALSE":
            for j in range(int(x1)):
                x4 = input("Enter record: ")
                empty.append(str(x4))
            di.delete_record(up(x),empty,oids=False)
        else:
            print("wrong")
    except:
        print("-ERROR-")
        start()
    start()

def edit_record():
    try:
        x = input("Enter table name to edit record from: ")
        x1 = input("Enter the number of columns in that table: ").replace(" ","")
        x3 = input("Enter the oid of the record: ")
        empty = []
        for i in range(int(x1)):
            x2 = input("Enter record: ")
            empty.append(str(x2))
        di.edit_record(up(x),empty,oids_set=x3)

    except:
        print("-ERROR-")
        start()
    start()

def query_tables():
    for i in di.query_tables():
        print(i)

def reset_records():
    try:
        e = input("Enter the number of tables to reset: ").replace(" ","")
        for j in range(int(e)):
            x = input("Enter table name to reset: ")
            y = di.query_all([up(x)])
            baz = []
            for i in y:
                baz.append(str(i[-1]))
            di.delete_record(up(x),baz,oids=True)
    except:
        print("-ERROR-")
        start()
    start()

def reset_all():
    x = di.query_tables()
    for i in x:
        y = di.query_all([up(i[0])])
        baz = []
        for j in y:
            baz.append(str(j[-1]))
        di.delete_record(up(i[0]),baz,oids=True)

        di.delete_table([str(i[0])])

    start()

def start():
    x = """
1- INSERT RECORD
2- EDIT RECORD
3- DELETE RECORD
4- CREATE TABLE
5- DELETE TABLE
6- QUERY RECORDS
7- QUERY TABLES
8- RESET RECORDS
9- RESET ALL
10- QUIT
    """
    print(x)
    x1 = input("Input command: ")
    y = x1.upper().replace(" ","")
    if y =="INSERTRECORD":
        insert_record()
    if y =="EDITRECORD":
        edit_record()
    if y=="DELETERECORD":
        delete_record()
    if y=="CREATETABLE":
        create_table()
    if y=="DELETETABLE":
        delete_table()
    if y=="QUERYRECORDS":
        query_records()
    if y=="QUERYTABLES":
        query_tables()
    if y=="RESETRECORDS":
        reset_records()
    if y=="RESETALL":
        reset_all()
    if y=="QUIT":
        quit()
    else:
        start()

if __name__ == "__main__":
    start()
