from extensions.sql import db
from sqlalchemy.orm import backref
class User(db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.String(20), nullable=False)
    upassword = db.Column(db.String(60), nullable=True)
    uname = db.Column(db.String(20), nullable=True)
    idcard = db.Column(db.String(18), nullable=False)
    

class UserInfo(db.Model):
    __tablename__ = 'tb_user_info'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    headerpic = db.Column(db.String(100), nullable=True)
    usex = db.Column(db.String(2), nullable=True)
    uage = db.Column(db.Integer, nullable=True)
    uphone = db.Column(db.String(11), nullable=True)
    uemail = db.Column(db.String(20), nullable=True)
    degree = db.Column(db.String(20), nullable=True)
    school = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(30), nullable=True)
    user_id = db.Column(db.Integer,db.ForeignKey('tb_user.id'))
    info_to_user = db.relationship('User',backref=backref("user_to_info", uselist=False))# 建立ORM一对一多关系
    dept_id = db.Column(db.Integer,db.ForeignKey('tb_dept.id'))# 建立外键关系，理解为该表外键dept_id关联tb_dept表的id字段
    info_to_dept = db.relationship('Dept',backref='dept_to_info')# 建立ORM一对多关系
class Dept(db.Model):
    __tablename__ = 'tb_dept'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(20),nullable=True)
    pid = db.Column(db.Integer,nullable=False)

association_table = db.Table('tb_auth_group_access',
    db.Column('uid', db.Integer, db.ForeignKey('tb_user.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('tb_auth_group.id'))
    )#多对多中间表

class Group(db.Model):
    __tablename__ = "tb_auth_group"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(20),nullable=True)
    group_to_user = db.relationship('User',
        secondary=association_table,
        backref='user_to_group',
        lazy='dynamic'
    )

class Rule(db.Model):
    __tablename__ = 'tb_auth_rule'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(80),nullable=True)
    title = db.Column(db.String(20),nullable=False)
    icon = db.Column(db.String(20),nullable=True)
    type = db.Column(db.Integer,nullable=False)
    status = db.Column(db.Integer,nullable=False)
    condition = db.Column(db.String(100),nullable=False)
    pid = db.Column(db.Integer,nullable=False)
    level = db.Column(db.Integer,nullable=False)
    sort = db.Column(db.Integer,nullable=False)