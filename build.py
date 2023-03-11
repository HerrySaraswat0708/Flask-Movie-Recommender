from app import app
from flask_frozen import Freezer

app.debug = False

freezer = Freezer(app)

if __name__=='__main__':
    freezer.freeze()