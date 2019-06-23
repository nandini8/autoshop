#!/usr/bin/python3
import json
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import inspect
from database import createDB as DB

api = Api(DB.app)
def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


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
        mapper = inspect(DB.Shop)
        shop = DB.Shop()
        for column, fields in zip(mapper.attrs, request.form):
            print(column, fields)
            if "Shop."+fields == column:
                column = request.form[fields]
            DB.db.session.add(shop)    
            DB.db.session.commit()


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

api.add_resource(AllShopDetails, '/shops')
api.add_resource(SearchShopDetails, '/shops/<string:shop_name>')

if __name__ == '__main__':
    DB.app.run()
