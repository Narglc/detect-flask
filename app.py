from flask import Flask, request, jsonify

# https://pypi.org/project/langdetect/
from langdetect import detect   

from setting import logger

app = Flask(__name__)

# 开启DEBUG模式
app.config['DEBUG'] = True

@app.route('/detect-language', methods=['POST'])
def detect_language():
    if 'text' not in request.json:
        logger.error(f"oriText is empty")
        return jsonify({'error': 'Text field is missing in the request body'}), 400
    
    text = request.json['text']
    
    try:
        language = detect(text)
        logger.info(f"oriText:{text},lang:{language}\n")
        return jsonify({'language': language}), 200
    except Exception as e:
        logger.error(f"detect fail, err:{str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)