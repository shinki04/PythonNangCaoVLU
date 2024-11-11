from flask import  Flask , render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__) 
bootstrap = Bootstrap(app)

@app.route('/<name>')
def b15(name = None):
    return render_template("B15.html", name = name)

if __name__ == "__main__":
    app.run(debug=True)
