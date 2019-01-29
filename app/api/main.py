from flask import jsonify, request
from md5_light import app
from app.api import bp
from app.models import MD5_files
from uuid import uuid4
from app import db
import hashlib
from urllib.request import urlopen
from threading import Thread
from app.email import send_email


def file_from_net_async(id, url, email):
	hash_md5 = hashlib.md5()
	try:
		req = urlopen(url)
		for chunk in iter(lambda: req.read(4096), b""):
			hash_md5.update(chunk)
		md5 = hash_md5.hexdigest()
		status = 'done' if md5 else 'fail'
	except: 
		status = 'fail'
	# Записываем в БД
	with app.app_context():
		note = db.session.query(MD5_files).filter_by(id=id).first()
		note.status = status
		note.md5 = md5 if status != 'fail' else None
		db.session.commit()
	# Отправляем письмо
	print(email)
	if email:
		text_body = 'id: {}. url: {}, md5: {}'.format(id, url, md5)
		send_email('Md5_light', 'API', email, text_body, app)


@bp.route('/submit', methods=['POST'])
def submit():
	id = str(uuid4())
	if 'email' in request.form.keys():
		email = email = request.form['email']
	else:
		email = False
	url = request.form['url']
	status = 'running'
	# Записываем в БД
	md5_file = MD5_files(id=id, url=url, status='running')
	db.session.add(md5_file)
	db.session.commit()
	# Отправляем выполняться
	Thread(target=file_from_net_async, args=(id, url, email)).start()

	return jsonify({'id': id})


@bp.route('/check', methods=['GET'])
def check():
	id = request.args['id']
	response = MD5_files.query.filter_by(id=id).first().to_dict()
	if response['status'] == 'running':
		return jsonify({'status': 'running'})
	else:
		return jsonify(response)
