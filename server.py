from flask import Flask, render_template, jsonify
from revdict import find_words_by_query

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/query/<string:querystring>")
def query(querystring):
    words = find_words_by_query(querystring)
    return jsonify(words)


if __name__ == "__main__":
    app.run()