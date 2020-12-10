from doremi.database import db
from doremi.database import Column
from doremi.database import PkModel
from doremi.database import TimeStamp
from doremi.database import reference_col
from doremi.database import relationship


class User(PkModel, TimeStamp):

    __tablename__ = "user"

    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    password = Column(db.LargeBinary(128), nullable=True)
    active = Column(db.Boolean(), default=True, nullable=False)
