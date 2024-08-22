# from flask import Flask
#
# app = Flask(__name__)
#
# from view0.page import page
# from view0.user import user
#
# @app.route('/ ')
# def hello_world():
#     # put application's code here
#     return 'fuken'
#
# if __name__ == ' __main__':
#     app.register_blueprint(page.pb, static_folder='static', template_folder='templates')
#     app.register_blueprint(user.ub, static_folder='static', template_folder='templates')
#     app.run()

from flask import Flask
from view0.page import page
from view0.user import user

app = Flask(__name__)
app.secret_key='this is secret key'
@app.route('/')
def hello_world():
    return 'fuken'

if __name__ == '__main__':
    app.register_blueprint(page.pb, static_folder='static', template_folder='templates')
    app.register_blueprint(user.ub, static_folder='static', template_folder='templates')
    app.run(port="8088",debug=True)