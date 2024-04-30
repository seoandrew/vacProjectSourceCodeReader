from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

server = Flask(__name__)
CORS(server)

@server.route('/')
def index():
    return render_template("VACProject1.html")

@server.route('/grab-url', methods=['GET'])
def grab_url():
    url = request.args.get('url')
    try:
        response = requests.get(url)
        decoded = response.content.decode('utf-8', errors='replace')
        return decoded
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    server.run(debug=True)
