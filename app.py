from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the root page."

@app.route('/about')
def about():
    return "This is a test application for Dice Analytics Devops training."

@app.route('/test')
def test():
    return "This is the test page."

@app.route('/post', methods=["POST"])
def post():
    return "This is a test of POST method."


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
