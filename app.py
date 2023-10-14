from flask import Flask, render_template
from generate import block, new_textarea, remove_text_area

app = Flask(__name__, static_folder='./static')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/delete/block', methods=['DELETE'])
def delete_block():
    return ''

@app.route('/add/block', methods=['POST'])
def add_block():
    return block()

@app.route('/add/textarea', methods=['POST'])
def add_textarea():
    return new_textarea()

@app.route('/remove/textarea', methods=['DELETE'])
def remove_textarea():
    return remove_text_area()