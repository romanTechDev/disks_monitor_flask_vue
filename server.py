from flask import Flask, request, render_template, flash, redirect, Markup
# from flask_login import LoginManager, login_user, login_required, UserMixin

from Scripts.authentication import authentication_user

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
@app.route('/authentication.html', methods=['POST', 'GET'])
def authentication():
    if request.method == "POST":
        try:
            if authentication_user(request.form['login_input'],request.form['password_input']):
                return redirect('workspace.html')
            else:
                flash('Неккоректные данные !', category='error')
                return render_template('authentication.html')

        except Exception:
            return render_template('authentication.html')
    else:
        return render_template('authentication.html')
