from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def roleSelect():
    return render_template('index.html')
@app.route('/educator')
def educatorLogin():
    return render_template('educatorLogin.html')

if __name__ == '__main__':
    app.run(debug=True)