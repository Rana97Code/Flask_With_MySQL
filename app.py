from flask import Flask
from flask import request, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_marshmallow import Marshmallow


app = Flask(__name__)

# Order matters: Initialize SQLAlchemy before Marshmallow
db = SQLAlchemy()
ma = Marshmallow()

mysql = MySQL(app)

app.config['SECRET_KEY'] = 'seCREtKeY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3306/flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



db.init_app(app)
# with app.app_context():
#     db.create_all()

# @app.route('/')
# def index():
#     return render_template('index.html')

# import from model
from model.customer import Customers
from model.customer import CustomerSchema

#schema for get product through API
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

    
@app.route('/customers', methods=['GET'])
def get_customers():
    customer = []
    data = Customers.query.all()
    customer = customers_schema.dump(data)
    return jsonify(customer)


@app.route('/customer_insert', methods = ['POST'])
def customer_insert():
    _json = request.json
    customer_name = _json['customer_name']
    email = _json['email']
    phone = _json['phone']
    customer_type = _json['customer_type']
    country_id = _json['country_id']
    c_address = _json['c_address']
    c_bin_nid = _json['c_bin_nid']
    c_tin = _json['c_tin']
    shipping_country_id = _json['shipping_country_id']
    shipping_address = _json['shipping_address']
    new_customer = Customers(customer_name=customer_name, email=email, phone=phone, customer_type=customer_type, country_id=country_id, 
                            c_address=c_address, c_bin_nid=c_bin_nid, c_tin=c_tin, shipping_country_id=shipping_country_id, shipping_address=shipping_address)
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"Message": "New Customer Added"})

        
@app.route('/get_customer/<id>', methods=['GET'])
def customer_byid(id):
    customer = []
    data = Customers.query.get(id)
    if data is None:
        return jsonify('No Such Customer Found')
    customer = customer_schema.dump(data)  #need to use customer_schema not customers_schema
    return jsonify(customer)       


@app.route('/customer_update/<id>', methods = ['PUT'])
def customer_upd(id):

    _json = request.json
    customer_name = _json['customer_name']
    email = _json['email']
    phone = _json['phone']
    customer_type = _json['customer_type']
    country_id = _json['country_id']
    c_address = _json['c_address']
    c_bin_nid = _json['c_bin_nid']
    c_tin = _json['c_tin']
    shipping_country_id = _json['shipping_country_id']
    shipping_address = _json['shipping_address']

    data = Customers.query.get(id)

    data.customer_name = customer_name
    data.email = customer_name
    data.email = email
    data.phone = phone
    data.customer_type = customer_type
    data.country_id = country_id
    data.c_address = c_address
    data.c_bin_nid = c_bin_nid
    data.c_tin = c_tin
    data.shipping_country_id = shipping_country_id
    data.shipping_address = shipping_address

    db.session.commit()
    return customer_schema.jsonify(data)


@app.route('/get_customer/delete/<id>', methods=['DELETE'])
def customer_delete_byid(id):
    data = Customers.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify('The Customer has been deleted')  


@app.route('/product')
def product():
    return'<h1> Product is there </h1>'


if __name__ == "__main__":
    app.run(debug=True)