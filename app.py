from flask import Flask, jsonify

app = Flask(__name__)

purchase_orders = [
{
    'id': 1,
    'description': 'Pedido de compra 1',
    'items': [
    {
        'id': 1,
        'description': 'Item do pedido 1',
        'price': 20.99
    }]
}
]


@app.route('/')
def home():
    return "Hello World!!!"

@app.route('/purchase_orders')
def get_puchase_orders():
    return jsonify(purchase_orders)

app.run(port=5000)