from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from app.models import Server, Law, LawCategory, User
from app import db

class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == 'admin'
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

def init_admin(app):
    admin = Admin(app, name='GTA RP Laws Admin', template_mode='bootstrap4')
    admin.add_view(AdminModelView(Server, db.session))
    admin.add_view(AdminModelView(LawCategory, db.session))
    admin.add_view(AdminModelView(Law, db.session))
    admin.add_view(AdminModelView(User, db.session))