from database import dataManipulationDB as db
def get_shop_details(query):
    rows = db.select_query(query)
    print(rows)


def put_device_details(values):
    print(values)
    string = "insert into device values ("+str(values['id'])+", '"+values['name']+"')"
    print(string)
    db.sql_edit_insert(string)



if __name__ == '__main__':
    get_shop_details('Select * from device')
    # values = {'id': 1, 'name': 'first'}
    # put_device_details(values)
