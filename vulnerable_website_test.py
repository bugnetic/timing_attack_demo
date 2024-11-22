import os
from flask import Flask, request, jsonify, render_template, abort
import time
app = Flask(__name__)

SECRET = os.getenv("SECRET_KEY")

def compare(user_input, secret):
    for x, y in zip(user_input, secret):
        if x != y:
            return False
        time.sleep(0.02) 
    return len(user_input) == len(secret)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/check', methods=['POST'])
def check_secret():
    message = ""
    if request.method == 'POST':
        user_input = request.form.get("secret", "")
        if not user_input:
            message = "Please enter a secret."
        elif compare(user_input, SECRET):
            message = "Success! You guessed the secret correctly."
        else:
            message = "Failure! Your guess was incorrect."
    
    return render_template("index.html", message=message)

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": str(error)}), 401

if __name__ == "__main__":
    app.run()


