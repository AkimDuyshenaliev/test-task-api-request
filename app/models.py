from sqlalchemy import Column, Integer, String, Float
from app.session import Base


class Crypto(Base):
    __tablename__ = "crypto"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    ticker = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(Float, nullable=False)
