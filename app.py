from flask import Flask, request
from flask_cors import CORS
import os
import datetime
import json
import random

app = Flask(__name__)
CORS(app)  # Enable CORS on all routes

@app.route('/accept', methods=['POST'])
def accept_cookies():
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Generate a unique filename based on the timestamp and remote address
    rand_id = random.randrange(100_000)  # doesn't have to be that big due to remote addr and timestamp
    filename = f"{timestamp}_{request.remote_addr}_{rand_id}.txt"
    
    # Create a new text file to store the request information
    request_info = {
        "Timestamp": timestamp,
        "Remote Address": request.remote_addr,
        "Request Headers": dict(request.headers),
        "Cookies": request.cookies,
        "Request Data": request.data.decode('utf-8'),
        "Query Parameters": request.args.to_dict()
    }
    
    # Create a new JSON file to store the request information
    with open(filename, 'w') as file:
        json.dump(request_info, file)
    
    return json.dumps({'accepted': True}), 200


if __name__ == '__main__':
    app.run()