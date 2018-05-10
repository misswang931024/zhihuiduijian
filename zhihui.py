#encoding:utf-8
from flask import Flask
import config
from exts import db
app = Flask(__name__)
app.config.from_object(config)
db.create_all()

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
