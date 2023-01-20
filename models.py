from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Foods(db.Model):
    __tablename__ = "foods_test"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    carb_grams = db.Column(db.Float)
    image = db.Column(db.Text)

    def __repr__(self):
        return "<Name %r>" % self.name