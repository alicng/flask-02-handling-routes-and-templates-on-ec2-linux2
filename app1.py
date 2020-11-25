from flask import Flask, redirect, url_for, 


app = Flask(__name__)

@app.route('/')
def home():
    return 'This is a home page for "/" path'

@app.route('/about')
def about():
    return '<h1> This is my about page ... </h1>'

@app.route('/error')
def error():
    return '<h1> Either you encountered an error or you are not authorized... </h1>'

@app.route('/hello')
def hello():
    return '<h1> Hello from ALI </h1>'

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    authorized=False
    if authorized:
        return 'This is an admin page ....'
    else: 
        return redirect(url_for('error'))

@app.route('/<name>')
def greet(name):
    greet_format=f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Greeting Page</title>
    </head>
    <body>
        <h1>Hello, { name }!</h1>
        <h1>Welcome to my Greeting Page</h1>
    </body>
    </html>
    """
    return greet_format

@app.route('/greet-admin')
def greet_admin():
    return redirect(url_for('greet', name='Mater Admin!!!!'))

@app.route('/greet-admin')
def greet_admin():
    return redirect(url_for('greet', name='Mater Admin!!!!'))

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)