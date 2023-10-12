import sqlite3 as sq 
db_ = "C:/Users/user/Documents/GitHub/Sqlite3-Simple-Database/database.db"
up = lambda n : str(n).upper().replace(" ","")

class database_interactions:
    def __init__(self,db:str):
        self.db = db
        self.conn = sq.connect(self.db)
        self.c = self.conn.cursor()

    def get_column_number_from_table(self,table:str):
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.c.fetchall()
        col_list = []
        for i in tables:
            for j in i:
                if j == table:
                    self.c.execute("SELECT * FROM "+str(j))
                    for a in self.c.description:
                        col_list.append(a[0])
        return(len(col_list))

    def create_table(self,table:str,*columns:list):
        empty = []
        for i in columns:
            for j in i:
                e = up(j)
                e += " TEXT,"
                empty.append(str(e))
        y = ""
        for j in empty:
            y += str(j)
        x = len(y)
        final = y[0:x-1]
        self.c.execute("CREATE TABLE "+up(table)+"("+final+")")

        self.conn.commit()

    def insert_record(self,table:str,*records:list):
        col_nbr = database_interactions(self.db).get_column_number_from_table(table)
       
        alpha = []
        for j in range(0,int(col_nbr)):
            alpha.append(":%s")
        x = ",".join(alpha)

        recs = ()
        for l in records:
            for y in l:
                y = f"|{y}|"
                recs += (y,)

        self.c.execute("SELECT * FROM "+up(table))
        u = ()
        a1 = ""
        for row in self.c.description:
            u += (row[0],)
            a1 += f":{row[0]},"
    
        t= u + recs
        p = {}
        for q in range(int(len(t)/2)):
            p.update({u[q]:recs[q]})

        self.c.execute("INSERT INTO "+up(table)+" VALUES("+a1[0:-1]+")",p)

        self.conn.commit()

    def delete_table(self,*tables:list):
        for i in tables:
           for j in i:
            self.c.execute("DROP TABLE "+up(j))

        self.conn.commit()

    def edit_record(self,table:str,*new_records:list,**oids_set:int):
        value = ""
        for d in oids_set.values():
            value += str(d)
        
        u = ()
        for k in new_records:
            for t in k:
                u += (str(t).replace(" ","_"),)

        y = ""
        for g in new_records:
            y += str(len(g))

        recs = ()
        for l in new_records:
            for h in l:
                h = f"|{h}|"
                recs += (h,)

        self.c.execute("SELECT * FROM "+up(table))
        beta = []
        for row in self.c.description:
            beta.append(str(row[0]))

        i = ""
        for o in range(int(y)):
            i += "{0} = :{1},".format(beta[o],u[o])
        
        t = u + recs
        p = {}
        for q in range(int(len(t)/2)):
            p.update({u[q]:recs[q]})
        p.update({"oid":str(value)})
        
        
        self.c.execute("UPDATE "+up(table)+" SET "+i[0:-1]+" WHERE oid = :oid ",p)

        self.conn.commit()

    def delete_record(self,table:str,*records:list, **oids:bool):
        
        def delete_record_without_oid():
            self.c.execute("SELECT *,oid FROM "+up(table))
            x = self.c.fetchall()

            emp1 = []
            for i in x:
                emp2 = []
                for j in i:
                    emp2.append(str(j))
                emp1.append(emp2)

            emp3 = []
            for a in emp1: 
                e = "".join(a)
                emp3.append(e)
            
            for l in records:
                for c in l:
                    for d in emp3:
                        s= len(d)
                        if d[0:s-1]==c:
                            self.c.execute("DELETE FROM "+up(table)+" WHERE oid="+str(d[-1]))

        def delete_record_with_oid():
            for i in records:
                for j in i:
                    self.c.execute("DELETE FROM "+up(table)+" WHERE oid ="+str(j))

        for value in oids.values():
            if value == True:
                delete_record_with_oid()
            if value == False:
                delete_record_without_oid()

        self.conn.commit()
        
    def query_all(self,*tables:list):
        for r in tables:
            for table in r:
                self.c.execute("SELECT *,oid FROM "+up(table))
                query = self.c.fetchall()

        self.conn.commit()
        return query

    def query_tables(self):
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.c.fetchall()
        tables_list = []
        for i in tables:
            self.c.execute("SELECT * FROM "+i[0])
            for j in self.c.description:
                i += (j[0],)
            tables_list.append(i)
        return tables_list
    
    def reset_all(self):
        x = database_interactions(self.db).query_tables()
        for i in x:
            database_interactions(self.db).delete_table([str(i[0])])

di = database_interactions(db_)

if __name__ == "__main__":
   pass
