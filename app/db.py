from app import app
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Mysql Settings
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Antoniors2003/'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'projects_unilibre'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# MySQL Connection
mysql = MySQL(app)
