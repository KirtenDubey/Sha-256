from flask import Flask, request, jsonify, render_template
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hash', methods=['POST'])
def generate_hash():
    data = request.get_json()
    text = data.get("text", "")
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    return jsonify({"hash": sha256_hash})

if __name__ == '__main__':
    app.run(debug=True)
