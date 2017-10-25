"""Supertrend - EMA Crossover trading Strategy

http://www.freebsensetips.com/blog/detail/8/Supertrend


Supertrend(11,2) with 8 EMA & 15 EMA Crossover

Buy

Buy when 8 EMA crosses 15 EMA from below upwards and Supertrend indicator has
alreday provided a buy indication in the last two candles. If supertrend
indicator provides buy signal soon after the bullish EMA crossover.

Sell

Sell when 8 EMA crosses 15 EMA from over downwards and Supertrend indicator
provides given a sell indication in the last two candles. If supertrend
indicator provides sell signal soon after the bearish EMA crossover.

Stoploss and Trails

Stoploss to be positioned at the lower or upper peak of the Supertrend signal.
Trailing is performed along with Supertrend indicator graph.

Profit/Loss and exit booking

Any reverse signal by EMA crossover or Supertrend indicator can be an exit.
No profit booking guideline is defined, and positions to keep so long as we
don’t get yourself a exit transmission or get halted out."""
# TO DO
