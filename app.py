from flask import Flask, jsonify
from flask_cors import CORS
import random
import json

app = Flask(__name__)
CORS(app) 

with open('quotes.json', 'r', encoding='utf-8') as f:
    quotes = json.load(f)

@app.route('/api/quote', methods=['GET'])
def get_random_quote():
    """Retorna uma citação aleatória da lista."""
    random_quote = random.choice(quotes)
    return jsonify(random_quote)

if __name__ == '__main__':
    app.run(debug=True, port=5000)