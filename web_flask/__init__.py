from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Import routes (URL handlers)
from . import routes

# Additional setup and configuration can go here
# For example, you can set configuration settings, initialize a database, or add extensions.

# Make sure to end the file with a newline

