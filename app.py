import os
import requests
import json
from flask import Flask, render_template, request, redirect, flash, jsonify, session, url_for

app = Flask(__name__)
app.secret_key = os.environ['secret_key']

root_url = 'http://localhost:8080'
requests_ = requests.Session()


@app.route('/', methods=['GET'])
def index():

	if request.method == 'GET':
		return render_template('index.html')


@app.route('/strategies', methods=['POST'])
def strategies():
	if request.method == 'POST':
		loan_amount = float(request.form.get('loan_amount'))
		annual_interest_rate = float(request.form.get('annual_interest_rate'))
		loan_tenure = float(request.form.get('loan_tenure'))

		data = {
			'loan_amount':loan_amount,
			'annual_interest_rate': annual_interest_rate,
			'loan_tenure': loan_tenure
		}
		
		headers = {'Content-Type': 'application/json'}
		response = requests_.post(url=root_url+'/strategies', json=data, headers=headers)

		recommendations = json.loads(response.text)
		if response.status_code == 200:
			return render_template('strategies.html', recommendations=recommendations)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
