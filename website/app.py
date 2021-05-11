from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

wifiscan = Flask(__name__)

@wifiscan.route('/')
def home():
	return redirect(url_for("index"))

@wifiscan.route('/index')
def index():
	return render_template('index.html')

@wifiscan.route('/startscan')
def startscan():
	import test2
	if test2.portscanner() == True:	
		return redirect(url_for("goodresult"))
	else:
		return redirect(url_for("badresult"))

@wifiscan.route('/goodresult')
def goodresult():
	return render_template('goodresult.html')

@wifiscan.route('/badresult')
def badresult():
	return render_template('badresult.html')

if __name__ == '__main__':
	wifiscan.run()
