#!flask/bin/python

# Starts the web development server

# Import the app 
from app import app

# Invoke its run method
app.run(debug=True)