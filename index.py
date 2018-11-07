from flask import Flask, request, render_template
from flask_mail import Mail, Message
import annealing_decryption
import re
import string
import json
from column_transposition import transpos

app = Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'wbgscipherteam@gmail.com'
app.config['MAIL_PASSWORD'] = 'hahahayourdeadgaming'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail=Mail(app)

key = string.ascii_uppercase
ciphertype = "substitution"

@app.route('/')
def my_form():
    return render_template('index.html')

regex = re.compile('[^A-Z]')
@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    text = request.form['text']
    userinput = text.upper()
    selected = []
    substitutionresult = "N/A"
    columntransresult= "N/A"
    if request.form.get('substitution'):
        selected.append("substitution")
        print(regex.sub('', userinput), "HE")
        substitutionresult = annealing_decryption.anneal(regex.sub('', userinput), key, ciphertype, "swap", "")
    if request.form.get('vigenere'):
        selected.append("vigenere")
    if request.form.get('columntrans'):
        selected.append('columntrans')
        columns = request.form['columns']
        colno = 0
        if columns == "":
            colno = 0
        else:
            colno = int(columns)
        if colno > 1:
            columntransresult = transpos(regex.sub('', userinput), colno)
        else:
            for x in range(2, 21):
                columntransresult = transpos(regex.sub('', userinput), x)
    print(json.dumps(selected))
    msg = Message('Your Decoded Message from Tech Support', sender = 'wbgscipherteam@gmail.com', recipients = ['larchpraveen@gmail.com'])
    msg.html = 'Substitution Result: ' + substitutionresult + '<br><br>Column Transposition: ' + columntransresult
    mail.send(msg)
    return render_template("result.html", substitutionresult = substitutionresult, columntransresult = columntransresult)

if __name__ == '__main__':
   app.run(debug = True)
