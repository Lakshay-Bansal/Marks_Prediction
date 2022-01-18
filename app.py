from flask import Flask, render_template, request, redirect

import joblib


# __name__ == __main__
app = Flask(__name__)

#Loading the trained ML model on dataset
reg_model = joblib.load("model.pk1")

@app.route('/')
def hello():
	return render_template("index.html")
	# return "Your are at the home page."

@app.route('/', methods= ['POST'])
def marks():
	if request.method == 'POST':
		hours = request.form['hours']
		# hours = float(request.form['hours'])

		## We are providing hours in [[]] beacuse predict take 2D array
		pred_marks = reg_model.predict([[float(hours)]])
	return render_template("index.html", your_marks = pred_marks[0][0])

if __name__ == '__main__':
	app.debug = True	# Now we not need to referesh the server everytime for the changes created in the file
	app.run()