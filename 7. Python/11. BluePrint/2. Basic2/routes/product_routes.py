from flask import Blueprint, render_template

product_blueprint = Blueprint('product', __name__)

@product_blueprint.route('/')
def product_page():
    return render_template('product.html')

@product_blueprint.route('/detail')
def detail_page():
    return render_template('product_detail.html')