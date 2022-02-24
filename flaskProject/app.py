from flask import Flask

app = Flask(__name__)


@app.route('/')
def helloWorld():
    return "Startseite.html"


if __name__ == '__main__':
    app.run()
