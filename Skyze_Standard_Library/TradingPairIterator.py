"""Created on 30/12/2017 @author: michaelnew"""


# Library Imports
# 3rd parties

# Skyze Imports
from Skyze_Standard_Library.TradingPair import *


class TradingPairIterator(object):
  '''An iterable list of TradingPairs'''

  def __init__(self, pairs):
    """Constructor"""

    # Standard member variables
    self._pairs = pairs

  def length(self):
    return len(self._pairs)

  def toString(self):
    pairs_string = ""
    for pair in self._pairs:
      if pair is None:
        pairs_string += "None, "
      else:
        pairs_string += pair.toString() + ", "

    # remove the last ", "
    return pairs_string[:-2]

  def findPair(self, target_pair):
    return [pair for pair in self._pairs if pair == target_pair]

  def partners(self, side):
    return [pair for pair in self._pairs if pair.contains(side)]

  def findStrings(self, base, quote, separator):
    '''Return the pair made up of the passed base/quote strings if it exists
       as either base/quote or quote/base'''
    target_pair = TradingPair(base, quote, separator)
    found = [pair for pair in self._pairs if pair == target_pair]

    if len(found) > 0:
      return target_pair
    else:
      reversed_target = TradingPair(quote, base, separator)
      found = [pair for pair in self._pairs if pair == reversed_target]
      if len(found) > 0:
        return reversed_target
      else:
        return None

    # found= False
    # for pair in pairs_list:
    #     #print(pair.__dict__)
    #     if pair == target_pair:
    #         found = True
    #
    # if found:
    #     print("Found")
    # else:
    #     print("False")

    return found

  def listAllInstruments(self):
    ''' Lists all the instruments from the pairs list'''
    seen = []
    for pair in self._pairs:
      base = pair.getBase()
      quote = pair.getQuote()

      if not(base in seen):
        seen.append(base)
      if not (quote in seen):
        seen.append(quote)
    return seen

  def listPairs(self, side, instrument):
    ''' Lists all the pairs that has the instrument on the specified side
        ie base or quote'''
    if side == "base":
      return [pair for pair in self._pairs if pair.getBase() == instrument]
    elif side == "quote":
      return [pair for pair in self._pairs if pair.getQuote() == instrument]
    else:
      raise "ERROR - side parameter incorrect"
