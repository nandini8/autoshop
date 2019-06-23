#!/usr/bin/python3
import json
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import inspect
from database import createDB as DB
from datetime import datetime, time

api = Api(DB.app)
def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]

def load_datetime(value):
    if value is None:
        return None
    return datetime.strptime(value, '%H:%M').time()


class AllShopDetails(Resource):
    def get(self):
        shops = DB.Shop.query.all()
        print(shops)
        # shop_details = []
        shop_details = {}
        for shop in shops:
            data = shop.__dict__
            data.pop('_sa_instance_state')
            data['open_shop_time'] = dump_datetime(data['open_shop_time'])
            data['close_shop_time'] = dump_datetime(data['close_shop_time'])
            data['critical_time_from'] = dump_datetime(data['critical_time_from'])
            data['critical_time_to'] = dump_datetime(data['critical_time_to'])
            # shop_details.append({data['id']: data})
            shop_details[data['id']] = data
            
        ## return a list of dictionaries with shop details
        return {'shop_data': shop_details}


    def post(self):
     
        shop = DB.Shop()
        shop.id = request.form['id']
        shop.device_id = request.form['device_id']
        shop.shop_name= request.form['shop_name']
        shop.owner_name = request.form['owner_name']
        shop.location = request.form['location']
        shop.contact_details = request.form['contact_details']
        shop.shop_type = request.form['shop_type']
        shop.open_shop_time = load_datetime(request.form['open_shop_time'])
        shop.close_shop_time = load_datetime(request.form['close_shop_time'])
        shop.home_delivery = bool(request.form['home_delivery'])
        shop.charges_per_km = request.form['charges_per_km']
        shop.critical_time_from = load_datetime(request.form['critical_time_from'])
        shop.critical_time_to = load_datetime(request.form['critical_time_to'])

        DB.db.session.add(shop)    
        DB.db.session.commit()
        return shop ## Return this page to sign in url

    
class SearchShopDetails(Resource):
    def get(self, shop_name):
        shops = DB.Shop.query.filter_by(shop_name = shop_name).all()
        print(shops)
        shop_details = []
        for shop in shops:
            data = shop.__dict__
            data.pop('_sa_instance_state')
            data['open_shop_time'] = dump_datetime(data['open_shop_time'])
            data['close_shop_time'] = dump_datetime(data['close_shop_time'])
            data['critical_time_from'] = dump_datetime(data['critical_time_from'])
            data['critical_time_to'] = dump_datetime(data['critical_time_to'])
            shop_details.append(data)
        ## return a list of dictionaries with shop details of specified name
        return {'shop_data': shop_details}


class AllProductDetails(Resource):
    def get(self):
        products = DB.Product.query.all()
        print(products)
        product_details = {}
        for product in products:
            data = product.__dict__
            data.pop('_sa_instance_state')
            product_details[data['id']] = data
        ## return a list of dictionaries with product details
        return {'product_data': product_details}


    def post(self):
     
        product = DB.Product()
        product.id = request.form['id']
        product.shop_id = request.form['shop_id']
        product.product_name= request.form['product_name']
        product.discount = request.form['discount']
        product.available_item = bool(request.form['available_item'])
        DB.db.session.add(product)    
        DB.db.session.commit()
        return product

    
class SearchProductDetails(Resource):
    def get(self, product_name):
        products = DB.Product.query.filter_by(product_name = product_name).all()
        print(products)
        product_details = []
        for product in products:
            data = product.__dict__
            data.pop('_sa_instance_state')
            product_details.append(data)
        ## return a list of dictionaries with shop details of specified name
        return {'product_data': product_details}


api.add_resource(AllShopDetails, '/shops')
api.add_resource(SearchShopDetails, '/shops/<string:shop_name>')
api.add_resource(AllProductDetails, '/products')
api.add_resource(SearchProductDetails, '/products/<string:product_name>')

if __name__ == '__main__':
    DB.app.run()
  