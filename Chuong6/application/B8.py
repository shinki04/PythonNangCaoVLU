from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route("/")
def index():
    # return '<h1> Bad Request </h1>',400
    response = make_response('<h1>This document carries a cookie!</h1>') 
    response.set_cookie('answer','42')
    return response
    


if __name__ == "__main__":
    app.run()
