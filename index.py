from flask import Flask, request, render_template
app = Flask(__name__)
import annealing_decryption
import re
import string
import json

key = string.ascii_uppercase
ciphertype = "substitution"

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    selected = []
    if request.form.get('substition'):
        selected.append("substition")
    if request.form.get('vigenere'):
        selected.append("vigenere")
    if request.form.get('columntrans'):
        selected.append('columntrans')
    print(json.dumps(selected))
    text = request.form['text']
    userinput = text.upper()
    regex = re.compile('[^A-Z]')
    print(regex.sub('', userinput), "HE")
    decoded = annealing_decryption.anneal(regex.sub('', userinput), key, ciphertype, "swap", "")
    return render_template("result.html", data = decoded)
