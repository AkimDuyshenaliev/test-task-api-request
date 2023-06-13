import time
from datetime import date, datetime
from sqlalchemy import desc, and_
from sqlalchemy.orm import Session
from app.models import Crypto


def getCurrency(ticker: str, db: Session) -> list[dict]:
    '''
    Найти и вернуть все данные из базы данных по указанной валюте
    '''
    return db.query(Crypto).filter(Crypto.ticker == ticker).all()


def getLastUpdate(ticker: str, db: Session) -> float:
    '''
    Найти и вернуть последнюю запись в БД по указанной валюте
    '''
    return db.query(Crypto).filter(Crypto.ticker == ticker).order_by(Crypto.id.desc()).first()


def getCurrencyByDate(ticker: str, inputDate: date, db: Session) -> list[dict]:
    '''
    Найти и отсортировать данные по указанной валюте и дате
    '''
    inputDateMin = datetime.combine(inputDate, datetime.min.time())
    inputDateMin = time.mktime(inputDateMin.timetuple())

    inputDateMax = datetime.combine(inputDate, datetime.max.time())
    inputDateMax = time.mktime(inputDateMax.timetuple())

    return db.query(Crypto).filter(and_(
        Crypto.ticker == ticker,
        inputDateMin <= Crypto.timestamp,
        Crypto.timestamp <= inputDateMax)).all()
