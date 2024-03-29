from app import app, db
from app.models import User, Promo, FK_User_Promo


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Promo': Promo, 'FK_User_Promo': FK_User_Promo}