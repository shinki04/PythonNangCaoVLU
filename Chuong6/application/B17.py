
from flask import render_template, Flask, request, redirect, url_for, session

app = Flask(__name__) 


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        session['username'] = request.form['username']

        return redirect(url_for('index'))

    return '''

        <form method = "post" >

            <p> <input type = "text" name = "username" >

            <p> <input type = "submit" value = "Login" >

        </form >
        '''
        
        
@app.route('/')
def index():
    username = session.get('username', 'Guest')
    return f"Welcome, {username}!"





# Đặt secret key để bảo mật session
app.secret_key = 'A0Zr98j/3yX R~XHH(jmN]LWX/, ?RT'


if __name__ == "__main__":
    app.run(debug=True)
