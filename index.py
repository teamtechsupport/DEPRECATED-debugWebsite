from flask import Flask, request, render_template
app = Flask(__name__)
import annealing_decryption
import re
import string

key = string.ascii_uppercase
ciphertype = "substitution"

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
	userinput = text.upper()
	regex = re.compile('[^A-Z]')
	print(regex.sub('', userinput), "HE")
	return (annealing_decryption.anneal(regex.sub('', userinput), key, ciphertype, "swap", ""))