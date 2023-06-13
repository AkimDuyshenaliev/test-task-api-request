from app.utils.update_costs import UpdatePrices


def test_btc():
    element = UpdatePrices()
    result = element.getPrices(url=element.base_url + element.btc)
    assert type(result) == float


def test_eth():
    element = UpdatePrices()
    result = element.getPrices(url=element.base_url + element.eth)
    assert type(result) == float