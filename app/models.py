from app import db

# class for each database entity


class User(db.Model):
    username = db.Column(db.String(32), primary_key=True)
    email = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<User:{self.username}>"


# check/desgn DB schema & add other tables for coin info
