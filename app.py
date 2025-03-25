from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/hash', methods=['POST'])
def hash_text():
    data = request.json
    text = data.get("text", "")
    hash_result = hashlib.sha256(text.encode()).hexdigest()
    return jsonify({"hash": hash_result})

if __name__ == '__main__':
    app.run(debug=True)
request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/hash', methods=['POST'])
def hash_text():
    data = request.json
    text = data.get("text", "")
    hash_result = hashlib.sha256(text.encode()).hexdigest()
    return jsonify({"hash": hash_result})

if __name__ == '__main__':
    app.run(debug=True)
