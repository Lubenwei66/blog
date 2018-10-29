#与当前项目相关的模型文件，即所有的实体类在此编写
from . import db
class Category(db.Model):
    __tablename__='category'
    id=db.Column(db.Integer,primary_key=True)
    cate_name=db.Column(db.String(50),nullable=False)
    topics=db.relationship('Topic',backref='category',lazy='dynamic')
class BlogType(db.Model):
    __tablename__='blogtype'
    id=db.Column(db.Integer,primary_key=True)
    type_name=db.Column(db.String(20),nullable=False)
    topics=db.relationship('Topic',backref='blogType',lazy='dynamic')
class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    loginname=db.Column(db.String(50),nullable=False)
    uname=db.Column(db.String(30),nullable=False)
    email=db.Column(db.String(200),nullable=False)
    url=db.Column(db.String(200))
    upwd=db.Column(db.String(30),nullable=False)
    is_author=db.Column(db.SmallInteger,default=0)
    topic=db.relationship('Topic',backref='user',lazy='dynamic')
    replies = db.relationship('Reply', backref='user', lazy='dynamic')
    voke_topics = db.relationship(
        'Topic',
        secondary='voke',
        backref=db.backref('voke_users', lazy='dynamic'),
        lazy='dynamic'
    )
class Topic(db.Model):
    __tablename='topic'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    pub_date=db.Column(db.DateTime,nullable=False)
    read_num=db.Column(db.Integer)
    content=db.Column(db.Text,nullable=False)
    images=db.Column(db.Text,nullable=False)
    blogtype_id=db.Column(db.Integer,db.ForeignKey('blogtype.id'))
    category_id=db.Column(db.Integer,db.ForeignKey('category.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    replies=db.relationship('Reply',backref='topic',lazy='dynamic')
class Reply(db.Model):
    __tablename__='reply'
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    topic_id=db.Column(db.Integer,db.ForeignKey('topic.id'))
    content=db.Column(db.Text,nullable=False)
    reply_time=db.Column(db.DateTime)

Voke=db.Table('voke',db.Column('id',db.Integer,primary_key=True),db.Column('user_id',db.Integer,db.ForeignKey('user.id')),db.Column('topic_id',db.Integer,db.ForeignKey('topic.id')))


