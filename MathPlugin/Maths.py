from flask import Flask, send_from_directory, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return "Hello, World!"


@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('input')
    b = request.args.get('input2')
    return str(float(a) + float(b))


@app.route('/subtract', methods=['GET'])
def subtract():
    a = request.args.get('input')
    b = request.args.get('input2')
    return str(float(a) - float(b))

@app.route('/multiply', methods=['GET'])
def multiply():
    a = request.args.get('input')
    b = request.args.get('input2')
    return str(float(a) * float(b))

@app.route('/divide', methods=['GET'])
def divide():
    a = request.args.get('input')
    b = request.args.get('input2')
    return str(float(a) / float(b))


@app.route('/squareroot', methods=['GET'])
def squareroot():
    a = request.args.get('input')
    return str(float(a) ** 0.5)


@app.route('/.well-known/ai-plugin.json', methods=['GET'])
def serve_ai_plugin():
    return send_from_directory('.', 'ai-plugin.json', mimetype='application/json')

# Create a route named /.well-known/openapi.yaml to access the openapi.yaml file
@app.route('/.well-known/openapi.yaml', methods=['GET'])
def serve_openapi():
    return send_from_directory('.', 'openapi.yaml', mimetype='text/yaml')

# Create a route so that when i type "http://localhost:5000/logo.png" I can see my logo.png image
@app.route('/logo.png', methods=['GET'])
def serve_logo():
    return send_from_directory('.', 'logo.png', mimetype='image/png')

if __name__ == '__main__':
  app.run(debug=True, port=5001)









