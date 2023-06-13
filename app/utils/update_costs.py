import datetime
import time
import asyncio
import requests

from app.session import get_db
from app.models import Crypto


class UpdatePrices:
    def __init__(self):
        self.db = get_db
        self.base_url = "https://www.deribit.com/api/v2/public/get_index_price?index_name="
        self.btc = "btc_usd"
        self.eth = "eth_usd"

        self.sleeptime = 1 * 60  # Update every 1 minute

    async def update(self):
        while True:
            await asyncio.sleep(self.sleeptime)
            db = next(self.db())  # Open DB

            btc = Crypto(
                ticker=self.btc[:3],
                value=self.getPrices(url=self.base_url + self.btc),
                timestamp=time.mktime(datetime.datetime.now().timetuple())
            )
            eth = Crypto(
                ticker=self.eth[:3],
                value=self.getPrices(url=self.base_url + self.eth),
                timestamp=time.mktime(datetime.datetime.now().timetuple())
            )
            db.add(btc)
            db.add(eth)
            db.commit()
            db.refresh(btc)
            db.refresh(eth)

            db.close()  # Close DB

    def getPrices(self, url):
        return requests.get(url=url).json()['result']['index_price']
