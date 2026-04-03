from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Flask Works!'})

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'framework': 'flask'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))