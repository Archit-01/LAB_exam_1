from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get('/add')
def add():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify(result=a + b)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
