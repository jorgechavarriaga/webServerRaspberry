from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from libraries.msgMatrix import output, outputSlow
from libraries.textToSpeech import textToSpeech
import datetime, time

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route("/")
def index():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
#   output(1, 0, 0, False, f'I Love You To The Infinity And Beyond!!! T{chr(3)}M')
#   output(1, 0, 0, False, f'T{chr(3)}M')
   return render_template("index.html")
#   return "<h1>Hola Mundo</h1>" #render_template('index.html', **templateData)

@app.route("/message", methods=["GET","POST"])
def send_message():
	name = ''
	message = ''
	language = ''
	if request.method == 'POST':
		name = request.form['name']
		message = request.form['message']
		language = request.form['language']
	print(len(name), len(language), len(message))
	if (len(name)>0) and (len(message)>0) and (len(language)>0):
		print(f"Name:{name}\nMessage:{message}\nLanguage:{language}")
		output(1, 0, 0, False, f'{message}' )
		textToSpeech(message, language)
	name = ''
	message = ''
	language = ''
	return render_template("message.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)
