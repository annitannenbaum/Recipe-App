from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


# If File is run directly, the app runs in debug mode

if __name__ == "__main__":
    app.run(debug=True)
