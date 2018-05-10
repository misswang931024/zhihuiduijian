#encoding=utf-8
import os

DEBUG=  True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wsk931024@localhost/zhihui'
SQLALCHEMY_TRACK_MODIFICATIONS=True
SECRTE_KET=os.urandom(24)