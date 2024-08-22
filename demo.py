from flask import Flask, Blueprint


app = Flask(__name__,static_folder=None)

@app.route('/')
def hello_world():
    return 'fuken'

pb = Blueprint('page', __name__, url_prefix='/', template_folder='templates')
@pb.route('/page')
def home():
    return '我是符肯'
if __name__ == '__main__':

    app.register_blueprint(pb, static_folder='static', template_folder='templates')
    # app.register_blueprint(user.ub, static_folder='static', template_folder='templates')
    app.run(debug=True)