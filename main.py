from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
Bootstrap(app)


class UserNameForm(FlaskForm):
	username = StringField("username", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])
	



@app.route('/success')
def success():
	return "<h1>Welcome</h1>"


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = UserNameForm()
	if form.validate_on_submit():
		return "okare"
	return render_template("login.html", form=form)



if __name__ == "__main__":
	app.run()