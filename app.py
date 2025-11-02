from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Flask Text Analyzer API — Send a POST request to /analyze with your text!"

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Please send JSON with a 'text' field"}), 400

    text = data['text']
    analysis = {
        "original_text": text,
        "word_count": len(text.split()),
        "character_count": len(text),
        "is_palindrome": text.lower().replace(" ", "") == text[::-1].lower().replace(" ", "")
    }
    return jsonify(analysis)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
