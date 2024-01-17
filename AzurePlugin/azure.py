from flask import Flask, send_from_directory, request, jsonify
import requests
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return "Hello, World!"

@app.route('/returnVMs', methods=['GET'])
def get_vms():
    logic_app_url = "https://example.com/returnVMs"
    response = requests.post(logic_app_url)
    if response.status_code == 200:
        response_text = response.text
        return response_text
    else:
        return {"status_code": response.status_code, "response": response.text}

@app.route('/ShutDownVMs', methods=['GET'])
def shutdown_vms():
    logic_app_url = "https://example.com/ShutDownVMs"
    response = requests.post(logic_app_url)
    if response.status_code == 200:
        response_text = response.text
        return response_text
    else:
        return {"status_code": response.status_code, "response": response.text}

@app.route('/.well-known/ai-plugin.json', methods=['GET'])
def serve_ai_plugin():
    return send_from_directory('.', 'ai-plugin.json', mimetype='application/json')

@app.route('/.well-known/openapi.yaml', methods=['GET'])
def serve_openapi():
    return send_from_directory('.', 'openapi.yaml', mimetype='text/yaml')

@app.route('/logo.png', methods=['GET'])
def serve_logo():
    return send_from_directory('.', 'logo.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=5055)










