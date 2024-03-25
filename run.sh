#!/bin/bash

# Export the Flask environment variable
export FLASK_APP=app.py
export FLASK_ENV=production

# Run the Flask server
gunicorn -b :7999 app:app
