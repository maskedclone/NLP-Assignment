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
    name = StringField('Any suggestions?', validators=[DataRequired()])
    submit = SubmitField('Proceed')

@app.route('/beamsearch', methods = ['GET','POST'])
def beamsearch():
    form = MyForm()
    code = False
    name = False
    print(form.validate_on_submit())
    if form.validate_on_submit():
        name = form.name.data 
        code = predict(prompt = name, temperature=0.5)
        form.name.data = ""
    return render_template("beamsearch.html",form=form,name =name, code=code)
if __name__ == "__main__":
    app.run(debug=True)