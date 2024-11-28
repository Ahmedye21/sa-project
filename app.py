
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, static_url_path='/')

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
