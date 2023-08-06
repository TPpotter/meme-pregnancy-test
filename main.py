from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    if request.method == 'GET':
        return render_template('main.html')


app.run(host='localhost', port=8000, debug=True)
