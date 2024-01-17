from flask import Flask, send_from_directory, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return "Hello, World!"

def get_exchange_rate(from_currency, to_currency, amount, date=None):
  url = f"https://api.apilayer.com/exchangerates_data/convert?from={from_currency}&to={to_currency}&amount={amount}"

  headers = {"apikey": "YOUR_API_KEY"}

  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    result = response.json()
    return result["result"]
  else:
    raise Exception(f"Error: {response.status_code}, {response.text}")


@app.route('/convert', methods=['GET'])
def convert_currency():
  from_currency = request.args.get('from')
  to_currency = request.args.get('to')
  amount = request.args.get('amount')
  date = request.args.get('date', None)

  try:
    converted_amount = get_exchange_rate(from_currency, to_currency, amount,
                                         date)
    return jsonify({
      "from": from_currency,
      "to": to_currency,
      "amount": amount,
      "converted_amount": converted_amount
    })
  except Exception as e:
    return jsonify({"error": str(e)}), 400

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
  app.run(debug=True, port=5050)









