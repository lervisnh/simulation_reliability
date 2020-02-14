import db
from db.models import User

db.init_db()
session = db.make_session()

user = session.query(User).filter(User.name == '0000').first()

if user is None:
    user = User(name='0000', password='1234', is_admin=True)
    session.add(user)
    session.commit()

else:
    print('user exists, change another username')
