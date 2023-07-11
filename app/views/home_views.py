from flask import Blueprint, render_template

home_views = Blueprint('home', __name__)

@home_views.route("/")
@home_views.route("/home/")
def home():
    return render_template('home.html')

@home_views.route("/contact/")
def contact():
    return render_template('contact.html')

@home_views.route("/saludo/<name>/")
def saludo(name):
    user = 'admin'
    return render_template('saludo.html', 
                           name=name, 
                           user=user)

@home_views.route("/drinks/")
def drinks():
    drinks = ["agua", "jugo", "tequila", "pulque", "azulito", "chela"]
    return render_template('drinks.html', drinks=drinks)
