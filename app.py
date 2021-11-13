# Import dependencies
from flask import Flask

# Create new app instance
app = Flask(__name__)

# Create home route
@app.route('/')
def hello_world():
    return 'Hello world'