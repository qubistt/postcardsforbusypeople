from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dash')
def dash():
    return render_template('dash.html')

@app.route('/create')
def create():
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)