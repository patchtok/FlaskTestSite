import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_index():
    return render_template('index.html')


@app.route('/tips')
def tips():
    return render_template('tips.html')


@app.route('/conversions')
def conversions():
    return render_template('conversions.html')


@app.route('/video')
def video():
    return render_template('video.html')


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)
print("hello")