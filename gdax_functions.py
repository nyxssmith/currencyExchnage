import gdax

public_client = gdax.PublicClient()


def ETH_USD():
    ETH_USD_ticker = public_client.get_product_ticker(product_id='ETH-USD')
    # print("ETH-ticker",ETH_USD_ticker)
    return ETH_USD_ticker


def BTC_USD():
    BTC_USD_ticker = public_client.get_product_ticker(product_id='BTC-USD')
    # print("BTC-ticker",BTC_USD_ticker)
    return BTC_USD_ticker
