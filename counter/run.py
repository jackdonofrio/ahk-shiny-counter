import json

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    count = get_count()
    return render_template('index.html', count=count)

@app.route('/count')
def get_count_dict():
    return json.load(open('count.json'))

def get_count():
    return get_count_dict()['count']

@app.route('/add')
def add():
    new = {'count' : get_count() + 1}
    json.dump(new, open('count.json','w'))
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=False)