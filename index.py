from flask import Flask, request, render_template
from hunspell import Hunspell
h = Hunspell()
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
	def bruteForce(message):
		letters = list(message)
		letterpos = []
		for letter in letters:
			#if letter == " ":
			#  pos = " "
			#else:
			if str.isalpha(letter):
				pos = ord(letter)-97
				letterpos.append(pos)
		a = 1
		b = 1
		apots = [1,3,5,7,9,11,15,17,19,21,23,25]
		avars = []
		for A in apots:
			for i in range(1, 26):
				if (A*i) % 26 == 1:
					avars.append(i)
		abvars = []
		for letter in letterpos:
			if letter == " ":
				currentletter = []
				for a in avars:
					b = 1
					while b<=26:
						currentletter.append(" ")
						b=b+1
			else:
				currentletter = []
				for a in avars:
					b=1
					currenta = []
					while b<=26:
						ax = letter - b
						abx = ax * a
						if abx % 26 !=0:
							abx = abx % 26
						else:
							abx = 0
						aby = chr(abx+97)
						currentletter.append(aby)
						currenta.append(aby)
						b = b + 1
			abvars.append(currentletter)
		times = 0
		while times < 311: 
			listwords = ([i[times] for i in abvars])
			wordjoined = ("".join(listwords))
			if containsEnglish(wordjoined):
                                return wordjoined
			times += 1	
	def containsEnglish(string):
		l = len(string)
		correct = 0
		for i in range(l): #for length of string
			for j in range(i+7, l+1): #for every set of letters 6 or more
				if correct > 10: #if at least 10 words are english, return yes
					return(True)
				if h.spell(string[i:j]) == True: #check if that set is a word
					correct+=1 #if yes increace english likelyhood
		return(False) #otherwise return no
	def affineShifts():
		message = text.upper()
		return bruteForce(message)
	affineShifts()
    
