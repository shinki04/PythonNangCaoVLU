'''
Lỗi
'''

from flask import Flask, render_template
app = Flask(__name__, static_folder='C:\\Users\\Lenovo\\Desktop\\Myspace\\Coder\\Python\\PythonNangCao\\Chuong6\\application\\static')

@app.route('/')
def index():
    return render_template("abc.html")


if __name__ == "__main__":
    app.run()
