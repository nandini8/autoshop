import createDB as DB
from datetime import time
from datetime import datetime

def insertDeviceData():
    for i in range(1, 5):
        device = DB.Device()
        device.id = i
        device.device_name = "device"+str(i)
        DB.db.session.add(device)    
        DB.db.session.commit()

def insertShopData():
    device = DB.Device.query.all()
    shop = DB.Shop(id=1, device_id=device[0].id, shop_name="shop1", owner_name="owner1", location="53 Rajat path, Mansarovar, Jaipur", contact_details="9109827354", shop_type="medical", open_shop_time=time(9,0,0), close_shop_time=time(22,0,0), home_delivery=True, charges_per_km=5, critical_time_from=time(22,0,0), critical_time_to=time(9,0,0))
    DB.db.session.add(shop)    
    DB.db.session.commit()

    
    shop = DB.Shop(id=2, device_id=device[1].id, shop_name="shop2", owner_name="owner2", location="60 Rajat Path, Mansarovar, Jaipur", contact_details="9103527354", shop_type="general", open_shop_time=time(8,0,0), close_shop_time=time(20,0,0), home_delivery=False, critical_time_from=time(20,0,0), critical_time_to=time(8,0,0))
    DB.db.session.add(shop)    
    DB.db.session.commit()   
    
    
    shop = DB.Shop(id=3, device_id=device[2].id, shop_name="shop3", owner_name="owner3", location="60 Shipra Path, Mansarovar, Jaipur", contact_details="8790765422", shop_type="photocopy", open_shop_time=time(9,0,0), close_shop_time=time(20,0,0), home_delivery=False, critical_time_from=time(20,0,0), critical_time_to=time(9,0,0))
    DB.db.session.add(shop)    
    DB.db.session.commit()
    
    shop = DB.Shop(id=4, device_id=device[3].id, shop_name="shop4", owner_name="owner4", location="57 Shipra Path, Mansarovar, Jaipur", contact_details="9867564532", shop_type="food", open_shop_time=time(11,0,0), close_shop_time=time(23,0,0), home_delivery=False, critical_time_from=time(23,0,0), critical_time_to=time(10,0,0))
    DB.db.session.add(shop)    
    DB.db.session.commit()

def insetIOTdata():
    device = DB.Device.query.all()
    data = DB.IOT(id=1, device_id=device[0].id, open_door_time=datetime(2019, 6, 14, 13,5,20), close_door_time=datetime(2019, 6, 14,13,10,35), body_detected=True, no_of_bodies=2)
    DB.db.session.add(data)    
    DB.db.session.commit()
    data = DB.IOT(id=2, device_id=device[0].id, open_door_time=datetime(2019,6,14,13,7,50), close_door_time=datetime(2019,6,14,13,20,9), body_detected=True, no_of_bodies=1)
    DB.db.session.add(data)    
    DB.db.session.commit()
    data = DB.IOT(id=3, device_id=device[0].id, open_door_time=datetime(2019,6,14,13,30,0), close_door_time=datetime(2019, 6,14,13,50,3), body_detected=True, no_of_bodies=3)
    DB.db.session.add(data)    
    DB.db.session.commit()
    data = DB.IOT(id=4, device_id=device[1].id, open_door_time=datetime(2019,6,14,10,5,10), close_door_time=datetime(2019,6,14,10,30,12), body_detected=True, no_of_bodies=2)
    DB.db.session.add(data)    
    DB.db.session.commit()
    data = DB.IOT(id=5, device_id=device[1].id, open_door_time=datetime(2019,6,14,10,30,22), close_door_time=datetime(2019,6,14,10,32,5), body_detected=True, no_of_bodies=1)
    DB.db.session.add(data)    
    DB.db.session.commit()
    data = DB.IOT(id=6, device_id=device[1].id, open_door_time=datetime(2019,6,14,11,50,2), close_door_time=datetime(2019,6,14,11,56,17), body_detected=True, no_of_bodies=1)
    DB.db.session.add(data)    
    DB.db.session.commit()


if __name__ == '__main__':
    # insetIOTdata()
#     insertDeviceData()
#     insertShopData()
