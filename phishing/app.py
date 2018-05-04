import os
import urllib.parse
import psycopg2
from flask import Flask, jsonify, render_template, redirect, url_for,g, jsonify
from flask import request
import random
import sendgrid
from sendgrid.helpers.mail import *

app = Flask(__name__)
app.debug = True
app.secret_key="supersecretkey"

def connect_db():
	print("In connect_db")
	if not 'DATABASE_URL' in os.environ:
		print("You must have DATABASE_URL in your environment variable. See documentation.")
		print("Execute 'source .env' to set up this environment variable if running locally.")
		return

	try:
		urllib.parse.uses_netloc.append("postgres")
		url = urllib.parse.urlparse(os.environ["DATABASE_URL"])

		db = psycopg2.connect(
		    database=url.path[1:],
		    user=url.username,
		    password=url.password,
		    host=url.hostname,
		    port=url.port
		)

		return db

	except Exception as ex:
		print(ex)
		print("Unable to connect to database on system.")
		return

def get_db():
	print("In get_db")
	"""Opens a new database connection if there is none yet for the
	current application context.
	"""
	if not hasattr(g, 'envelope'):
		g.envelope = connect_db()
	return g.envelope

def sendemail(email):
	sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
	from_email = Email("no-reply@printluther.com")
	to_email = Email(email)
	subject = "ENTER SUBJECT HERE"

	#NOTE: sendgrid allows you to create and export HTML. Use that to generate HTML for the content?
	content = Content("text/html", """<a href="https://pathwerks.herokuapp.com/verifyuser/"""+token+"""">Please click this link to verify your account on Pathwerks.com</a>""")
	mail = Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())

@app.route('/')
def home():

	return render_template('index.html')
	

@app.route('/login',methods=['POST'])
def login():
	print(request.form)
	return render_template('index.html')

if __name__ == '__main__':
  app.run()
