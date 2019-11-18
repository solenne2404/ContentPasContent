from flask import render_template
from app import app

@app.route('/admin/')
@app.route('/admin/accueil')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Accueil', user=user)