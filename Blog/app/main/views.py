#主业务逻辑中的视图和路由的定义
from flask import render_template,request,session,redirect
from . import main
from ..models import *
from .. import *
import datetime
import os
@main.route('/')
def main_index():
    categories=Category.query.all()
    topics=Topic.query.all()
    if 'uname' in session and 'uid' in session:
        user=User.query.filter_by(id=session['uid']).first()
    return render_template('index.html',params=locals())
@main.route('/login',methods=['POST','GET'])
def login_views():
    if request.method=='GET':
        return render_template('login.html')
    else:
        loginname=request.form.get('username')
        pwd=request.form.get('password')
        user=User.query.filter_by(loginname=loginname,upwd=pwd).first()
        if user:
            session['uid']=user.id
            session['uname']=user.uname
            return redirect('/')
        else:
            errMsg='用户名或密码不正确'
            return render_template('login.html',errMsg=errMsg)
@main.route('/register',methods=['POST','GET'])
def register_views():
    if request.method=='GET':
        return render_template('register.html')
    else:
        loginname=request.form.get('loginname')
        email=request.form.get('email')
        url=request.form.get('url')
        password=request.form.get('password')
        uname = request.form.get('uname')
        user=User()
        user.loginname=loginname
        user.uname=uname
        user.email=email
        user.url=url
        user.upwd=password
        db.session.add(user)
        db.session.commit()
        session['uname']=user.uname
        session['uid']=user.id
        return redirect('/')
@main.route('/release',methods=['POST','GET'])
def release_views():
    if request.method=='GET':
        if 'uid' not in session or 'uname' not in session:
            return redirect('/login')
        else:
            user=User.query.filter_by(id=session['uid']).first()
            if user.is_author !=1:
                return redirect('/')
            else:
                user = session['uname']
                blogtype = BlogType.query.all()
                categories = Category.query.all()
                return render_template('release.html', params=locals())
        blogtype = BlogType.query.all()
        categories=Category.query.all()
        return render_template('release.html',params=locals())
    else:
        topic=Topic()
        topic.title=request.form.get('author')
        topic.blogtype_id=request.form.get('list')
        topic.category_id=request.form.get('category')
        topic.user_id=request.form.get('uid')
        topic.content=request.form.get('content')
        topic.pub_date=datetime.datetime.now().strftime('%Y-%m-%d')
        if request.files:
            f=request.files['picture']
            ftime=datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
            ext=f.filename.split('.')[1]
            filename=ftime+'.'+ext
            topic.images='upload/'+filename
            basedir=os.path.dirname(os.path.dirname(__file__))
            upload_path=os.path.join(basedir,'static/upload',filename)
            f.save(upload_path)
        db.session.add(topic)
        return redirect('/')
@main.route('/list')
def list_views():
    return render_template('list.html')
@main.route('/info',methods=['POST','GET'])
def info_views():
    if request.method=='GET':
        topic_id=request.args.get('topic_id')
        topic=Topic.query.filter_by(id=topic_id).first()
        topic.read_num=int(topic.read_num)+1
        db.session.add(topic)
        prevTopic=Topic.query.filter(Topic.id<topic_id).order_by('id desc').first()
        nextTopic=Topic.query.filter(Topic.id>topic_id).first()
        if 'uid' in session and 'uname' in session:
            user=User.query.filter_by(id=session['uid']).first()
        return render_template('info.html',params=locals())

@main.route('/photo')
def photo_views():
    return render_template('photo.html')
@main.route('/logout')
def logout_views():
    if 'uid' in session and 'uname' in session:
        del session['uid']
        del session['uname']
    return redirect('/')
@main.route('/time')
def time_views():
    return render_template('time.html')
@main.route('/gbook',methods=['POST','GET'])
def gbook_views():
    if request.method=='GET':
        return render_template('gbook.html')
    else:
        msg='评论功能未开放'
        return render_template('gbook.html',msg=msg)
@main.route('/about')
def about_views():
    return render_template('about.html')