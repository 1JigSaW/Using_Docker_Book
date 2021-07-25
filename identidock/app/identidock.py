from flask import Flask, Response, request
import hashlib
import requests

app = Flask(__name__)
salt = "UNIQUE_SALT"
default_name = 'Jig Saw'

@app.route('/', methods=['GET', 'POST'])
def mainpage():
	name = default_name
	if request.method == 'POST':
		name = request.form['name']
		salted_name = salt + name
		name_hash = hashlib.sha256(salted_name.encode()).hexdigest()
		header = '<html><head><title>Identidock</title></head><body>'
		body = '''<form mrthod="POST">
			Hello <input type="text" name="name" value="{}">
			<input type="submit" value="submit">
			</form>
			<p>You look like a:
			<img src="/monster/{1}"/>
			'''.format(name, name_hash)
		footer = '</body></html>'
		return header + body + footer

@app.route('/monster/<name>')
def get_identicon(name):
	r = request.get('http://dnmonster:8080/monster/' + name + '?size=80')
	image = r.content

	return Response(image, mimetype='image/png')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')