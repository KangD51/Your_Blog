from flask import Flask   #1 Flask Class imported from flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Ensure Migrate is imported
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)  #2 setting app variable to instance of Flask.From here it will look for for template,static files etc.
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'#6 for the security od the datas.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Database setup
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

# Additional setup
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Importing routes after app and extensions setup to avoid circular imports
from flaskblog import routes
