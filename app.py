from flask import Flask
from models import db
from routes import api
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ben:ben12345@localhost/superheroes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
