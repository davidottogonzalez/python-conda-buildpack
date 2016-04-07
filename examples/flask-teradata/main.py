from flask import Flask
import json, os

#just a demo use of the library in the code
import teradata

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello Teradata!'

@app.route('/query')
def query():
	udaExec = teradata.UdaExec (appName="HelloTeradata", version="1.0", logConsole=True)
	session = udaExec.connect(method="odbc", system="tdprod", username="xxx", password="xxx");
	rows = [ row for row in session.execute("SELECT GetQueryBand()") ]
	print rows
	# return some json here
	return rows

port = os.getenv('PORT')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
