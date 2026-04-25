from flask import render_template, Flask
from flask_sqlalchemy import SQLAlchemy # type: ignore

app = Flask(__name__) # 1. Create the app first!

# 2. Then set the config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://app:TNLkZk5a@localhost/eeducate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Highly recommended to save memory

# 3. Finally, initialize the database with the app
db = SQLAlchemy(app)

@app.route('/')
def roleSelect():
    return render_template('index.html')

@app.route('/educator')
def educatorLogin():
    return render_template('educatorLogin.html')

if __name__ == '__main__':
    app.run(debug=True)