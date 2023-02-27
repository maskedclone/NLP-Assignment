from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired
import pandas as pd
from predict import predict
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
app.config['UPLOAD_FOLDER'] = 'static/files' 

@app.route('/')
def index():
    return render_template("index.html")
class MyForm(FlaskForm):
    name = StringField('Type', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/assignment6', methods = ['GET','POST'])
def autocomplete():
    form = MyForm()
    code = False
    name = False
    print(form.validate_on_submit())
    if form.validate_on_submit():
        name = form.name.data 
        code = predict(prompt = name, temperature=0.5)
        form.name.data = ""
    return render_template("assignment6.html",form=form,name =name, code=code)
if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def home():
#     return "Hello, Flask!"