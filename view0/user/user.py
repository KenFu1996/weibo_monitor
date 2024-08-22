from utils.query import query
from flask import Blueprint, render_template, request,redirect,session

ub = Blueprint('user', __name__, url_prefix='/user', template_folder='templates')

@ub.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
         return render_template("login.html")
    else:
        def filter_fn(user):
            return request.form['username'] in user and request.form['password'] in user
        users=query('select * from user ',[])
        #login_success=list(filter(filter_fn(users)))
        session['username']=request.form['username']#这一行将获取到的用户名存储到Flask的Session中，键是’username’，值是用户输入的用户名。 request.form意思是
        return redirect('/home/page')

@ub.route('/register',methods=['GET','POST'] )
def register():
    if request.method=='GET':
        return render_template("register.html") #render_template的作用在于返回一个模板
    else:
        if  request.form['password']!=request.form['checkpassword']:
            return '两次密码不符合'

        def  filter_fn(user):
            return  request.form['username'] in user
        users=query('select * from user',[])
        print(users)
        filter_list=list(filter(filter_fn,users))
        if len(filter_list):
            return '该用户已被注册'
        else:
            query('''
            insert into user(user_password,user_name) values (%s,%s)
            ''',[request.form['password'],request.form['username']])
        return  redirect('/user/login')
