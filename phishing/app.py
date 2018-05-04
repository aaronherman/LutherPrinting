
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
	subject = "Printer software changing for Faculty"

	#NOTE: sendgrid allows you to create and export HTML. Use that to generate HTML for the content?
	# Call function which generates that part? 
	content = Content("text/html", """<p>Hello <Humanities Division>,</p><p>We would like to inform you of a change involved in the printing system on campus. We have switched from PaperCut to a service that will save Luther College over 15% each year and provide more functionality, PrintLuther. We have already pushed the update to your workstation -- this will not require any extra work on your Luther provided workstation. </p><p>PrintLuther allows you to print to any printer on campus by selecting the location on the [web interface](<link here>). Simply select the location from the dropdown menu on the right-hand side of the screen. </p><p>We have added a sample print job to each of your PrintLuther account, and we encourage you to try it out now and contact IT if you have any questions (x1000). You can sign into your PrintLuther account with your NorseKey [here](<link here with query parameter>).</p><p>Please feel free to contact us with any questions. We have student workers ready to help during this transition.</p><p>Sincerely,IT DepartmentExt: 1000</p>""")
	mail = Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())
	print(response)
	print('sent message')

# sendemail('hermaa02@luther.edu')

@app.route('/')
def home():

	return render_template('index.html')
	


if __name__ == '__main__':
  app.run()
