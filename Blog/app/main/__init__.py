#对主业务逻辑程序的初始化操作
from flask import Blueprint
main=Blueprint('main',__name__)
from . import views