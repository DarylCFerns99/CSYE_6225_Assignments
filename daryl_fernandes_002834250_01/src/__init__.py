from flask import Flask
import os
from src.config.config import Config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

# loading environment variables
load_dotenv()
# declaring flask application
app = Flask(__name__)
# calling the dev configuration
config = Config().dev_config
# config = Config().production_config
# making our application to use dev env
app.env = config.ENV

# Configure Flask logging
app.logger.setLevel(logging.INFO)  # Set log level to INFO
logger_path = "./logs"
if not os.path.exists(logger_path):
    os.makedirs(logger_path)
handler = logging.FileHandler(logger_path + "/logfile.log")  # Log to a file
app.logger.addHandler(handler)

# Path for our local mysql database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI_DEV")
# To specify to track modifications of objects and emit signals
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
# sql alchemy instance
db = SQLAlchemy(app)
# Flask Migrate instance to handle migrations
migrate = Migrate(app, db)
# import models to let the migrate tool know
from src.models.test_model import Test

# import api blueprint to register it with app
from src.routes import api
app.register_blueprint(api, url_prefix = "/")