from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


user_coins = db.Table(
    "user_coins",
    db.Column(
        "user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True
    ),
    db.Column(
        "coin_id", db.Integer, db.ForeignKey("coin.id"), primary_key=True
    ),
)


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    coins = db.relationship(
        "Coin", secondary=user_coins, back_populates="users"
    )

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Coin(db.Model):
    __tablename__ = "coin"
    id = db.Column(db.Integer, primary_key=True)
    coin_name = db.Column(db.String(64), index=True, unique=True)
    ticker_name = db.Column(db.String(120))
    price_usd = db.Column(db.Numeric(18, 8))
    usd_market_cap = db.Column(db.Numeric(18, 8))
    usd_24hr_vol = db.Column(db.Numeric(18, 8))
    usd_24hr_change = db.Column(db.Numeric(18, 8))
    last_api_query_at = db.Column(db.DateTime)
    last_updated_at = db.Column(
        db.DateTime, index=True, default=datetime.utcnow
    )
    users = db.relationship(
        "User", secondary=user_coins, back_populates="coins"
    )

    def __repr__(self):
        return "<Coin {}>".format(self.body)
