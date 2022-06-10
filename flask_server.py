# -*- coding: utf-8 -*-
from flask import Flask, request, Response

# create the Flask app
app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        print(json["object"]["status"],json["object"]["metadata"])
        response = Response(status=200)
        return response
    else:
        return 'Content-Type not supported!'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=8443)
