import shapeshift
import gdax_functions
market_info = shapeshift.get_market_info("BTC","ETH")
print(market_info)

BTC_USD = gdax_functions.BTC_USD()["price"]
ETH_USD = gdax_functions.ETH_USD()["price"]

print("btc to usd ",BTC_USD)
print("eth to usd", ETH_USD)
print("btc/eth usd amounts",float(BTC_USD)/float(ETH_USD))



print("market info btc to eth rate")
print(market_info["rate"])

