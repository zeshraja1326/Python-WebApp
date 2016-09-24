from app import db

class Test(db.Model): #Define class (Test)

    #create rows with theirs settings
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)

    #represent Test data
    def __repr__(self):
        return '<Test %r>' % (self.id)