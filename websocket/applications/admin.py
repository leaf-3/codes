from flask import render_template,Blueprint,jsonify
from applications.modules import db,User,UserInfo,Dept,Group,Rule
admin = Blueprint('admin',__name__)
@admin.route('/')
def index():
    print('admin/index')
    return render_template('admin/index.html')

@admin.route('/admin/test')
def test():
    user = User.query.filter_by(uid='114930').first()
    print(user.user_to_info)
    return user.user_to_info.school

#注册蓝图
def init_blue_admin(app):
    app.register_blueprint(blueprint=admin)