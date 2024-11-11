from flask import Flask, render_template, session, redirect, url_for, flash
from B19 import NameForm  # Đảm bảo rằng B19.py chứa class NameForm và có trong cùng thư mục với app

app = Flask(__name__)
app.secret_key = '2af24'  # Cần thiết để sử dụng session và flash

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

if __name__ == "__main__":
    app.run(debug=True)
