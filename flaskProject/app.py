from flask import Flask

app = Flask(__name__)


@app.route('/')
def startseite():
    return Startseite.html


if __name__ == '__main__':
    app.run()
