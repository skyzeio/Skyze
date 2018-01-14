"""Created on 30/12/2017 @author: michaelnew"""


# Library Imports
# 3rd parties

# Skyze Imports


class TradingPair(object):
  """A pair of markets that trade with each other
  All markets involve the simultaneous purchase of one instrument and sale of
  another, but the currency pair itself can be thought of as a single unit,
  an instrument that is bought or sold. If you buy a currency pair,
  you buy the base currency and implicitly sell the quoted currency.
  The bid (buy price) represents how much of the quote currency you need t
  o get one unit of the base currency. Conversely, when you sell the
  currency pair, you sell the base currency and receive the quote currency.
  The ask (sell price) for the currency pair represents how much you will
  get in the quote currency for selling one unit of base currency.

  A widely traded currency pair is the euro against the U.S. dollar,
  or shown as EUR/USD. The quotation EUR/USD = 1.2500 means that one euro is
  exchanged for 1.2500 U.S. dollars. In this case, EUR is the base currency
  and USD is the quote currency (counter currency). This means that 1 euro
  can be exchanged for 1.25 U.S. dollars. Another way of looking at this is
  that it will cost you $125 to buy EUR 100."""

  def __init__(self, base, quote, separator="_"):
    """Constructor"""
    if len(base) < 2:
      raise "EXCEPTION:: TradingPair __init__ - base is too short: " + base

    if len(quote) < 2:
      raise "EXCEPTION:: TradingPair __init__ - quote is too short: " + quote

    if separator.isalnum():
      raise "EXCEPTION:: TradingPair __init__ - separator can not be AlphaNumeric: " + quote

    # Standard member variables
    self._base = base
    self._quote = quote
    self._separator = separator

  @classmethod
  def init_string(cls, pair_str, separator):
    '''Second constructor from pairstring and separator string'''
    separator_position = pair_str.index(separator)
    base = pair_str[:separator_position]
    quote = pair_str[-(len(pair_str) - separator_position - 1):]
    return cls(base, quote)

  def __eq__(self, other):
    '''Override equality comparisons'''
    if type(other) is type(self):
      return self.__dict__ == other.__dict__
    return False

  def contains(self, side):
    return (self._base == side) or (self._quote == side)

  def split(self):
    return self._base, self._quote

  def getBase(self):
    return self._base

  def getQuote(self):
    return self._quote

  def toString(self):
    return self._base + self._separator + self._quote
