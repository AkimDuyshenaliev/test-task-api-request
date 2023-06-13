from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.session import get_db
from app.schemas import Currency
from app.utils.currencyRouterFunc import getCurrency, getLastUpdate, getCurrencyByDate

router = APIRouter(
    tags=['crypto'],
)


@router.get("/allCurrent", response_model=list[Currency], status_code=200)
def routerGetCurrency(ticker: str, db: Session = Depends(get_db)):
    return [Currency(**i.__dict__) for i in getCurrency(ticker=ticker, db=db)]


@router.get("/lastUpdate", response_model=float, status_code=200)
def routerGetLastUpdate(ticker: str, db: Session = Depends(get_db)):
    return getLastUpdate(ticker=ticker, db=db).__dict__["value"]


@router.get("/valueByDate", response_model=list[Currency], status_code=200)
def routerGetCurrencyByDate(
        ticker: str,
        inputDate: date = date.today(),
        db: Session = Depends(get_db)):
    return [Currency(**i.__dict__) for i
            in getCurrencyByDate(ticker=ticker, inputDate=inputDate, db=db)]
