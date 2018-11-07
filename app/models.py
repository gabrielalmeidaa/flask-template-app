from app import db

class ExempleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(30))
    hour = db.Column(db.String(30))

    def __init__(self, date, hour, csv_content):
        self.date = date
        self.hour = hour

    def __repr__(self):
        return '<ExempleModel %r>' % self.id

db.create_all()
