from flask import Flask, request
from sklearn.externals import joblib

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
	if request.method == 'POST':
		file = request.files['file']
		if file:
			loaded_model = joblib.load('finalized_model.sav')
			result = loaded_model.predict(predict)

			return jsonify(results={'width': width, 'height': height})
	return'''
		<h1>Upload new File</h1>
		<form action="" method=post enctype=multipart/form-data>
		<p><input type=file name=file>
		<input type=submit value=Upload>
		</form>
	'''

if __name__ == "__main__":
	app.run()