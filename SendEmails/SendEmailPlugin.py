from flask import Flask, send_from_directory, request
import requests


app = Flask(__name__)


@app.route('/SendEmail', methods=['GET', 'POST'])
def send_email():
    email_content = request.args.get('input')
    email_content = email_content.replace('\\n', '\n')
    email_content = email_content.replace('\\t', '\t')
    email_content = email_content.replace('\\r', '\r')
    email_content = email_content.replace('\\"', '"')
    print("************************************S T A R T***************************************************************")
    print(email_content)
    print("**************************************E N D*************************************************************")
    # URL de la Logic App
    logic_app_url = "https://example.com/logic-app-url"

    # Datos para enviar a la Logic App
    data = {
        "email_content": email_content
    }

    # Enviar una solicitud POST a la Logic App
    response = requests.post(logic_app_url, json=data)

    return email_content


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
    app.run(debug=True, port=4000)








