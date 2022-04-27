from app import app, db  # noqa

from app.models import User, Coin


# use `flask shell` to pre-import these in the shell context
# Usage: `db`, `User`, `Coin`
@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Coin": Coin}
