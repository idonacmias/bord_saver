from flask import Flask

app = Flask(__file__)

@app.raute('/')
def __init__():
	return '__init__'


if __name__ == '__main__':
	app.run()