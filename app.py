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

@app.route('/purchase_orders/<int:id>')
def get_puchase_orders_id(id):
    for po in purchase_orders:
        if po['id'] == id:
            return jsonify(po)
    return jsonify({'message': 'Pedido {} não encontrado'.format(id)})

app.run(port=5000)