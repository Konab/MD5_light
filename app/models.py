from app import db


class MD5_files(db.Model):
	id = db.Column(db.String(64), primary_key=True)
	md5 = db.Column(db.String(128), index=True)
	status = db.Column(db.String(64))
	url = db.Column(db.String(120), index=True)

	def __repr__(self):
		return '<id: {}, status: {}, url: {}, md5: {}>'.format(self.id, self.status, self.url, self.md5) 

	def to_dict(self, with_id=False):
		data = {
			'md5' : self.md5,
			'status' : self.status,
			'url' : self.url
		}
		if with_id: data['id'] = self.id
		return data
