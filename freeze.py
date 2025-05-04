from flask_frozen import Freezer
from app import app

app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

# Thêm URL generator cho route project
@freezer.register_generator
def project_url_generator():
    yield '/project'

if __name__ == '__main__':
    freezer.freeze()
