import csv
from flask import Flask, render_template, send_from_directory, request, redirect
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<path:subpath>')
def show_subpath(subpath):
    return render_template(subpath)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		name = data['name']
		email = data['email']
		phone = data['phone']
		message = data['message']
		file = database.write(f'\n{name},{email},{phone},{message}')

def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as database2:
		name = data['name']
		email = data['email']
		phone = data['phone']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,email,phone,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try:
	    	data = request.form.to_dict()
	    	write_to_csv(data)
	    	return redirect('/thankyou.html')
	    except:
	    	return 'Did not save to database'
    return 'something went wrong'