from flask import Flask,render_template,url_for, flash, redirect
from forms import RegistrationForm, LoginForms

app = Flask(__name__)

app.config['SECRET_KEY'] = '38fb4122dce4e2a06aede81b9946de'

posts =[
    {
        'author': 'Oz Blumenfeld',
        'title': 'Blog post #1',
        'content': 'Greetings fellows',
        'date_posted':'July 20, 2019'
    }
]


@app.route('/')
@app.route("/home")
def hello():
    return render_template('Home.html',posts=posts,title='home page')


@app.route('/about')
def about():
    return render_template('About.html', posts=posts, title='about page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title= 'Register', form=form)


@app.route('/login')
def login():
    form = LoginForms()
    return render_template('login.html', title= 'Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)