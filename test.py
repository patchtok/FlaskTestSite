import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1 style=\" color:red ; \">Hello World</h1><br>" \
           "<a href=\"about\">Link</a>"


@app.route('/about')
def about_me():
    return "I was born in England"

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)
print("hello")