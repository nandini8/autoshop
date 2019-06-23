import sqlite3
def select_query(query):
        conn = sqlite3.connect('deviceData.db')
        print("Database opened successfully", conn)
        cur = conn.cursor()
        print(query)
        cur.execute(query)       
        rows = cur.fetchall()
        return rows

def sql_edit_insert(query):
        conn = sqlite3.connect('deviceData.db')
        cur = conn.cursor()
        cur.execute(query)     
        conn.commit()

def sql_delete(query):
        conn = sqlite3.connect('deviceData.db')
        cur = conn.cursor()
        cur.execute(query)     

# if __name__ == '__main__':

        ## device data populating
        # for i in range(50):
        #         cmd = "insert into device values ("+str(i)+", 'device"+str(i)+"')"
        #         print(cmd)
        #         sql_edit_insert(cmd)