from flask import Flask
import json, os

#just a demo use of the library in the code
import jaydebeapi
import jpype

current_dir = os.path.dirname(os.path.abspath(__file__)) 
jar = r'{base}/lib/tdgssconfig.jar:{base}/lib/terajdbc4.jar'.format(base=current_dir)
args='-Djava.class.path=%s' % jar
jvm_path = current_dir + '/lib/jdk1.8.0_77/jre/lib/amd64/server/libjvm.so'
jpype.startJVM(jvm_path, args)

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello Teradata!'

@app.route('/query')
def query():
	conn = jaydebeapi.connect('com.teradata.jdbc.TeraDriver','jdbc:teradata://tdprodla.nbcuni.ge.com/USER=206438423,PASSWORD=nbcU2015BSCS')

	cursor = conn.cursor()

	cursor.execute("select COUNT(1) from sales_detail_fact")
	rows = cursor.fetchall()

	for col1, col2 in rows:
		print str(col1)+", "+str(col2)

	return rows

	conn.close()



port = os.getenv('PORT')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
