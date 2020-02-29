from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():

    return '<h1>To Jest tytul <button>B</button></>'


if __name__ == "__main__":
    app.run(debug=True)
