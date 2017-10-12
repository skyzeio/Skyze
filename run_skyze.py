"""Created on 12/10/2017
   @author: michaelnew"""

from Skyze import *

skyze = Skyze()
skyze.run()


# Configuration data
testing = False
config = settings.from_file(
    settings.DEFAULT_CONFIG_FILENAME, testing
)
tickers = ["AAPL", "SPY"]
filename = None

# Backtest information
title = ['Moving Average Crossover Example on AAPL: 100x300']
initial_equity = 10000.0
start_date = datetime.datetime(2000, 1, 1)
end_date = datetime.datetime(2014, 1, 1)

# Use the MAC Strategy
events_queue = queue.Queue()
strategy = MovingAverageCrossStrategy(
    tickers[0], events_queue,
    short_window=100,
    long_window=300
)

# Set up the backtest
backtest = TradingSession(
    config, strategy, tickers,
    initial_equity, start_date, end_date,
    events_queue, title=title,
    benchmark=tickers[1],
)
results = backtest.start_trading(testing=testing)
return results
