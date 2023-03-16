# from flask_login import UserMixin
from app import db
from app import ma
# customer_name, email, phone, customer_type, countery_id, c_address, c_bin_nid, c_tin, shipping_countery_id, shipping_address

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    customer_type = db.Column(db.String(100))
    country_id = db.Column(db.String(100))
    c_address = db.Column(db.String(100))
    c_bin_nid = db.Column(db.String(100))
    c_tin = db.Column(db.String(100))
    shipping_country_id = db.Column(db.String(100))
    shipping_address = db.Column(db.String(100))

#schema for get product through API

class CustomerSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id","customer_name", "email", "phone", "customer_type", "country_id", "c_address", "c_bin_nid", "c_tin", "shipping_country_id", "shipping_address")

