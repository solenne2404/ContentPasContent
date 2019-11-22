from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, PasswordForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Promo, FK_User_Promo
from werkzeug.urls import url_parse
from app.configChart import URL_GGSHEET, GGSHEET_GID, GGSHEET_PROMO_RANGE, GGSHEET_QUART1_RANGE, GGSHEET_QUART3_RANGE, GGSHEET_MOYENNE_RANGE, GGSHEET_ALL_RANGE


promos = Promo.query.order_by(Promo.name).all()
users = User.query.order_by(User.id).all()  


questions = ['1-Méthode pédagogique', '2-Progression', '3-Organisation matérielle', '4-Moyens pédagogiques', '5-Echanges dans le groupe', '6-Satisfaction']






@app.route('/')
@app.route('/index')
@login_required
def index():
    urimat = URL_GGSHEET.format(gid=GGSHEET_GID["global"], range=GGSHEET_ALL_RANGE["materiel"])
    uripeda = URL_GGSHEET.format(gid=GGSHEET_GID["global"], range=GGSHEET_ALL_RANGE["pedago"])
    uriech = URL_GGSHEET.format(gid=GGSHEET_GID["global"], range=GGSHEET_ALL_RANGE["echange"])
    urisat = URL_GGSHEET.format(gid=GGSHEET_GID["global"], range=GGSHEET_ALL_RANGE["satisfaction"])
    return render_template(
        'index.html', 
        title='Home', 
        Promos=promos,
        URIMAT=urimat,
        URIPEDA=uripeda,
        URIECH=uriech,
        URISAT=urisat)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template(
        'login.html', 
        title='Sign In', 
        form=form, 
        Promos=promos
        )


@app.route('/logout')
@login_required
def logout():
    logout_user()
   
    return redirect(
        url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if current_user.admin == False :
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, admin=form.admin.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Nouvel utilisateur enregistré')
        return redirect(url_for('login'))
    return render_template(
        'register.html', 
        title='Register', 
        form=form, 
        Promos=promos
        )


@app.route('/promo/<name>')
@login_required
def show_promo(name):
    thisPromo = Promo.query.filter_by(name=name).first_or_404()
    uri = URL_GGSHEET.format(gid=GGSHEET_GID["promo"], range=GGSHEET_PROMO_RANGE[name])
    return render_template(
        'promo.html',
        promo=thisPromo,
        Promos=promos,
        Questions=questions,
        URI=uri
    )


@app.route('/promo/<name>/<q>')
@login_required
def show_question(name, q):
    
    thisPromo = Promo.query.filter_by(name=name).first_or_404()
 

    urimoyenne = URL_GGSHEET.format(gid=GGSHEET_GID["promoind"], range=GGSHEET_MOYENNE_RANGE[name][q])
    uriquart1 = URL_GGSHEET.format(gid=GGSHEET_GID["promoind"], range=GGSHEET_QUART1_RANGE[name][q])
    uriquart3 = URL_GGSHEET.format(gid=GGSHEET_GID["promoind"], range=GGSHEET_QUART3_RANGE[name][q])
    if q not in questions:
        return redirect(url_for('show_promo', name=name))

    return render_template(
        'question.html',
        promo=thisPromo , 
        Promos=promos,  
        q=q,
        URIMOYENNE=urimoyenne,
        URIQUART1=uriquart1,
        URIQUART3=uriquart3
        )


@app.route('/profil', methods=['GET', 'POST'])
@login_required
def profil_edit():
    form = PasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()
        user.set_password(form.password.data)
        db.session.bulk_save_objects([user])
        db.session.commit()
        flash('Votre mot de passe a bien été modifié!')
        return redirect(url_for('index'))
    return render_template('profil.html', form=form)

@app.route('/gestionprofils')
@login_required
def rGestionProfils():
    db.session.commit()
    if current_user.admin == False :
        return redirect(url_for('index'))

    
    fk = FK_User_Promo.query.order_by(FK_User_Promo.user_id).all()  
    return render_template(
        'gestionProfil.html', 
        Promos=promos, 
        Users=users, 
        Fk=fk
        )
