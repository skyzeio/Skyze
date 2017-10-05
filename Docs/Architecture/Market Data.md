
# Skyze Market Database Architecture
Draft v0.1

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Skyze Market Database Architecture](#skyze-market-database-architecture)
	- [Data store](#data-store)
		- [csv](#csv)
		- [Artic MongoDB](#artic-mongodb)
	- [Data Sources](#data-sources)
		- [Mainstream Brokers](#mainstream-brokers)
			- [IG markets](#ig-markets)
				- [Download Package](#download-package)
				- [How to use](#how-to-use)
				- [Play labs](#play-labs)
				- [Config](#config)
		- [Crypto Exchanges](#crypto-exchanges)
			- [Poloniex](#poloniex)
			- [Cryptopia](#cryptopia)
		- [Data Aggregators](#data-aggregators)
			- [Coin Market Cap](#coin-market-cap)
			- [Quandl](#quandl)
			- [Yahoo Finance](#yahoo-finance)
			- [Google Finance](#google-finance)

<!-- /TOC -->

## Data store
### csv

### Artic MongoDB


## Data Sources
__Market Data__

### Mainstream Brokers
#### IG markets

##### Download Package
ig_trading
 https://github.com/ig-python/ig-markets-api-python-library

##### How to use
__Document directory__
https://github.com/ig-python/ig-markets-api-python-library/tree/master/docs

__REST__
https://github.com/ig-python/ig-markets-api-python-library/blob/master/docs/source/rest.rst

__STREAM__
https://github.com/ig-python/ig-markets-api-python-library/blob/master/docs/source/stream.rst

__TRADING__
Can't find this

##### Play labs
 http://labs.ig.com/

##### Config
acc_number = os.environ['IG_SERVICE_ACC_NUMBER']
password = os.environ['IG_SERVICE_PASSWORD']
api_key = os.environ['IG_SERVICE_API_KEY']
username = os.environ['IG_SERVICE_USERNAME']
acc_type = os.environ['IG_SERVICE_ACC_TYPE']


### Crypto Exchanges
#### Poloniex
Skyze class to REST API

#### Cryptopia
Skyze class to REST API

#### Bittrex
Bittrex Python Wrapper Library: 
https://github.com/ericsomdahl/python-bittrex


### Data Aggregators
#### Coin Market Cap
Web scraping historical EOD

#### Quandl
quandl downloader

#### Yahoo Finance
__ Download Package__ YStockQuote
https://pypi.python.org/pypi/ystockquote

#### Google Finance
__ Download Package__ googlefinance https://pypi.python.org/pypi/googlefinance
