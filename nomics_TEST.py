from nomics import Nomics
from get_aws_secret import get_nomics_api_key

nomics_api_key = get_nomics_api_key()
nomics = Nomics(nomics_api_key)

markets = nomics.Markets.get_markets(exchange = 'binance')
market_cap_history = nomics.Markets.get_market_cap_history(
    start="2010-01-01T00:00:00Z",
    end="2021-11-24T00:00:00Z"
)

volume_history = nomics.Volume.get_volume_history(
    start="2010-01-01T00:00:00Z",
    end="2021-11-24T00:00:00Z"
)

candles = nomics.Candles.get_candles(
    interval='1d',
    currency='BTC',
    start="2010-01-01T00:00:00Z",
    end="2021-11-24T00:00:00Z"
)
print(market_cap_history)
