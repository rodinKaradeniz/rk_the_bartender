from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # return render_template("home.html")
    return 'Welcome!'

@app.route('/user/<name>')
def user(name):
    # the curly braces {} hold a variable; when below runs,
    # the value will replace the braces and the variable name
    personal = f'<h1>Hello, {name}!</h1>'

    instruc = '<p>Change the name in the <em>browser address bar</em> \
        and reload the page.</p>'

    return personal + instruc

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='127.0.0.1', port=4999, debug=True)