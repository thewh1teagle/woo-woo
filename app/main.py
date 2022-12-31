from flask import Flask, render_template, request, redirect, url_for, jsonify
from ai import predict, DOG, CAT
app = Flask(__name__, template_folder="templates")

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def submit():
    files = request.files
    file = files.get('file')
    stream = file.stream
    print(file)
    result = predict(stream.read())
    return jsonify({"result": 'cat' if result == CAT else 'dog'})

@app.route('/cat')
def cat():
    return render_template('cat.html')

@app.route('/dog')
def dog():
    return render_template('dog.html')

app.run(host="0.0.0.0", port=8000, debug=True)