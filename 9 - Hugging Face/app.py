from flask import Flask, render_template, request
import torch
from transformers import AutoTokenizer
from transformers import pipeline




app = Flask(__name__)

pipe = pipeline("text-generation", max_length=50, pad_token_id=0, eos_token_id=0, model="briands/wikitext-lab-accelerate")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/suggestions')
def generate_suggestions():
    prompt = request.args.get('code', '')
    print(prompt)

    # real-----

    gen = pipe(prompt, max_length=128,do_sample=False)[0]["generated_text"]
    suggestion = gen.replace('\n', '<br>')
    suggestion_html= [f'<li class="list-group-item">{suggestion}</li>']
    return {'suggestions': suggestion_html}


if __name__ == '__main__':
    app.run(debug=True)
