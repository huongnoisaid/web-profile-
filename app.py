from flask import Flask, render_template
from flask.cli import ScriptInfo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

def handler(event, context):
    return ScriptInfo().load_app().wsgi_app(event, context)
