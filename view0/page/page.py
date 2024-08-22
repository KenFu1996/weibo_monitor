# from flask import Flask, session, render_template, redirect, Blueprint, request
#
# pb = Blueprint('page', __name__, url_prefix='/page', template_folder='templates')
#
#
# @pb.route('/home')
# def home():
#     return 'I am fuken'


from flask import Blueprint

'''
之前之所以会报 404 是因为 url_prefix='/page'  @pb.route('/home') 写反了
修改过来就可以了
'''

pb = Blueprint('page', __name__, url_prefix='/home', static_folder='static', template_folder='templates')

@pb.route('/page')
def home():
    return '我是符肯'