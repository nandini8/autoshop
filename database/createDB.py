import sqlite3, os

def create_device_db():
    create_query = "CREATE TABLE device (id INT primary key not null, name TEXT)"
    conn = sqlite3.connect('../deviceData.db')
    print( "Opened database successfully")
    conn.execute(create_query)
    conn.commit()
    conn.close()


## database for shop details
def create_shop_db():
    create_query = "create table shopDetails (id int primary key, device_id int not null,\
        shop_name text, owner_name text not null, location text not null, contact_details text not null, shop_type text not null, open_shop_time text, close_shop_time text,\
        home_order numeric not null, charges_per_km numeric, critical_time_from text, critical_time_to text, foreign key (device_id) references device(id))"
    conn = sqlite3.connect('../deviceData.db')
    print( "Opened database successfully")
    conn.execute(create_query)
    conn.commit()
    conn.close()


## database for products available in the shop
def products():
    create_query = "create table products (id int primary key, shop_id int not null,\
        product_name text not null, price int not null, discount int, available numeric, available_for_home numeric,\
        foreign key (shop_id) references shopDetails(id))"
    conn = sqlite3.connect('../deviceData.db')
    print( "Opened database successfully")
    conn.execute(create_query)
    conn.commit()
    conn.close()


## database for data obtained from the IoT
# add number of bodies detected
def iot_data():
    create_query = "create table realData (id int primary key, device_id int not null, open_door text not null, close_door text not null,\
        body_detected numeric not null, no_of_people int not null, foreign key (device_id) references device(id))"
    conn = sqlite3.connect('../deviceData.db')
    print( "Opened database successfully")
    conn.execute(create_query)
    conn.commit()
    conn.close()



if __name__ == '__main__':
    create_device_db()
    create_shop_db()
    products()
    iot_data()

