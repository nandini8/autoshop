import sqlite3

# def add_device_record(ids, name):
#         conn = sqlite3.connect('deviceData.db')
#         c = conn.cursor()
#         print( "Opened database successfully")
#         cmd = 'insert into device values ('+str(ids)+', "'+name+'")'
#         print(cmd)
#         c.execute('insert into device values ('+str(ids)+', "'+name+'")')
#         print ("Record added successfully")
#         c.close()

# def add_shop_record():
#         insert_query = "insert into shopDetails values(id, \
#                 device_id, \
#                 name, \
#                 contact_detils, \
#                 shop_type,\
#                 open_shop_time, \
#                 close_shop_time, \
#                 home_order, \
#                 charges_per_km, \
#                 critical_time_from, \
#                 critical_time_to \
#                 )"
#         conn = sqlite3.connect('deviceData.db')
#         c = conn.execute(insert_query)
#         c.close()

# def add_products_record():
#         insert_query = "insert into products values(id, \
#                 shop_id, \
#                 product_name, \
#                 price, \
#                 discount,\
#                 available, \
#                 available_for_home, \
#                 )"
#         conn = sqlite3.connect('deviceData.db')
#         c = conn.execute(insert_query)
#         c.close()

# def add_realData_record():
#         insert_query = "insert into realData values(id, \
#                 device_id, \
#                 open_door, \
#                 close_door, \
#                 body_detected,\
#                 )"
#         conn = sqlite3.connect('deviceData.db')
#         c = conn.execute(insert_query)
#         c.close()


# def show_device_data():
#         conn = sqlite3.connect('deviceData.db')
#         # print( "Opened database successfully")
#         c = conn.cursor()
#         c.execute('select * from device;') 
#         rows = c.fetchall()
#         for row in rows:
#                 print(row)



def select_query(query):
        conn = sqlite3.connect('../deviceData.db')
        print("Database opened successfully", conn)
        cur = conn.cursor()
        print(query)
        cur.execute('Select * from shopDetails;')       
        rows = cur.fetchall()
        return rows

def sql_edit_insert(query):
        conn = sqlite3.connect('../deviceData.db')
        cur = conn.cursor()
        cur.execute(query)     
        conn.commit()

def sql_delete(query):
        conn = sqlite3.connect('../deviceData.db')
        cur = conn.cursor()
        cur.execute(query)     

# def sql_query2(query):
#         conn = sqlite3.connect('deviceData.db')
#         cur = conn.cursor()
#         cur.execute(query)
#         rows = cur.fetchall()
#         return rows