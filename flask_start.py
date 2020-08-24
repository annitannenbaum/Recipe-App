from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "cV8LFkFYTB"

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")

@app.route('/recipes')
def recipes():
    return render_template('recipes.html', title="Recipes")

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm() # Create an instance of the Registration Form
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'Success!')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


# If File is run directly, the app runs in debug mode

if __name__ == "__main__":
    app.run(debug=True)
