import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import TIME



project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))
print(database_file)
app = Flask(__name__)
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = database_file


db = SQLAlchemy(app)


class Device(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    device_name = db.Column(db.String(30), nullable=False) 
    def __repr__(self):
        return "<Device Name: {}>".format(self.device_name)

class Shop(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)
    shop_name = db.Column(db.String(30), nullable=False)
    owner_name = db.Column(db.String(30), nullable=False)
    location = db.Column(db.String(30), nullable=False)
    contact_details = db.Column(db.String(30), nullable=False)
    shop_type = db.Column(db.String(30), nullable=False)
    open_shop_time = db.Column(TIME())
    close_shop_time = db.Column(TIME())
    home_delivery = db.Column(db.Boolean)
    charges_per_km = db.Column(db.Integer)
    critical_time_from = db.Column(TIME())
    critical_time_to = db.Column(TIME())

    def __repr__(self):
        return "<Shop Name: {}>".format(self.shop_name)


class Product(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    product_name = db.Column(db.String(50), nullable=False)
    discount = db.Column(db.Integer)
    available_item = db.Column(db.Boolean)
    def __repr__(self):
        return "<Product Name: {}>".format(self.product_name)

class IOT(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)
    open_door_time = db.Column(db.DateTime, nullable=False)
    close_door_time = db.Column(db.DateTime, nullable=False)
    body_detected = db.Column(db.Boolean)
    no_of_bodies = db.Column(db.Integer)
    ## add status

## add user credentials wala table

    def __repr__(self):
        return "<Open door time: {}>".format(self.open_door_time)


# if __name__ == '__main__':
#     db.drop_all()
#     db.create_all()