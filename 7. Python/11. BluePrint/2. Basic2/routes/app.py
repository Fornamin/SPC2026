from flask import Flask, render_template
from user_routes  import user_blueprint
from admin_routes import admin_blueprint
from product_routes  import product_blueprint

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static'
)

app.register_blueprint(user_blueprint, url_prefix = '/user')
app.register_blueprint(admin_blueprint, url_prefix = '/admin')
app.register_blueprint(product_blueprint, url_prefix = '/product')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)