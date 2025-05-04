from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

if __name__ == '__main__':
    app.run(debug=False)  # Tắt debug mode khi deploy
