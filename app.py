from flask import Flask, jsonify

import random

from sheng import sheng_words

app = Flask(__name__)

@app.route("/api/sheng")
def serve_mchongoano():
    maneno = sheng_words()
    nr_of_manenoz = len(maneno)
    selected_maneno = maneno[random.randint(0, nr_of_manenoz - 1)]
    return jsonify(selected_maneno)

if __name__ == "__main__":
    app.run(debug=True)
