from flask import Flask, request, render_template, flash, redirect, url_for
app = Flask(__name__)
app.secret_key = 'AXAPBswe4B'

@app.route('/')
def login():
	return render_template('login.html')

@app.route('/secure', methods=['POST'])
def secured():
	user = request.form['username']
	password = request.form['password']
	if(user == "admin" and password == "s3cur3"):
		flash("Logged in successfully")
		return render_template('secure.html')
	else:
		flash("Error while logging in with "+user)
		return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
