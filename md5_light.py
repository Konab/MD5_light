from app import create_app, db
from app.models import MD5_files

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'MD5_files': MD5_files}
