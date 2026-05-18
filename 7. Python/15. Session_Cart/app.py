from flask import Flask, render_template, session, request
from flask import redirect, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

products = [
    {"id": "item1", "name": "apple", "price": 3000},
    {"id": "item2", "name": "peach", "price": 8000},
    {"id": "item3", "name": "orange", "price": 5000},
    {"id": "item4", "name": "watermelon", "price": 20000},
    {"id": "item5", "name": "mango", "price": 10000},
    {"id": "item6", "name": "mandarine", "price": 6000},
    {"id": "item7", "name": "tomato", "price": 4500},
    {"id": "item8", "name": "pear", "price": 15000},
]

@app.route('/')
def home():
    return render_template('product.html', list = products)

@app.route('/add-cart/<id>')
def add_cart_list(id):
    isNew = False
    if not session:
        session['carts'] = [{'id': id, 'count': 1}]
    else:
        carts = session['carts']
        for item in carts:
            if (item['id'] == id):
                item['count'] = item['count'] + 1
                isNew = True
        if isNew == False:
            carts.append({'id': id, 'count': 1})
        session['carts'] = carts
    return redirect(url_for('home'))

@app.route('/cart')
def cart_list():
    carts = session.get('carts', [])

    cart_items = {}
    total_price = 0

    for cart in carts:
        id = cart['id']
        count = cart['count']
        item = next((p for p in products if p['id'] == id), None)
    
        if item is None:
            continue
        cart_items[id] = {
            'name': item['name'],
            'count': count,
            'price': item['price'],
            'subtotal': item['price'] * count
        }
        total_price += item['price'] * count

    return render_template(
        'cart.html',
        cart_list=cart_items,
        total_price=total_price
    )
if __name__ == '__main__':
    app.run(debug=True)