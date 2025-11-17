from flask import Flask, jsonify
from flask_cors import CORS
import random
import json
import unicodedata

app = Flask(__name__)
CORS(app) 

with open('quotes.json', 'r', encoding='utf-8') as f:
    quotes = json.load(f)

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

@app.route('/api/quote', methods=['GET'])
def get_random_quote():
    """Retorna uma citação aleatória da lista."""
    random_quote = random.choice(quotes)
    
    cleaned_quote = {
        'text': remove_accents(random_quote['text']),
        'author': remove_accents(random_quote['author'])
    }
    
    return jsonify(cleaned_quote)

if __name__ == '__main__':
    app.run(debug=True, port=5000)