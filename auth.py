from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/", methods=['GET', 'POST'])
def accueil():
    
    return render_template('pages/accueil.html')

@auth.route("/apropos", methods=['GET', 'POST'])
def apropos():

    return render_template('pages/apropos.html')
