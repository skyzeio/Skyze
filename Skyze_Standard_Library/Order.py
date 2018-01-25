class Order(object):
  '''Order Class'''
  average = None
  datetime = None
  fee = None
  filled = None
  id = None
  info = {'avg_execution_price': None,
          'cid': None,
          'cid_date': None,
          'exchange': None,
          'executed_amount': None,
          'gid': None,
          'id': None,
          'is_cancelled': None,
          'is_hidden': None,
          'is_live': None,
          'oco_order': None,
          'order_id': None,
          'original_amount': None,
          'price': None,
          'remaining_amount': None,
          'side': None,
          'src': None,
          'symbol': None,
          'timestamp': None,
          'type': None,
          'was_forced': None}
  price = None
  remaining = None
  side = None
  status = None
  symbol = None
  timestamp = None
  type = None
  mike = None

  def __init__(self, dictionary):
    self.__dict__.update(dictionary)
    # Coerce the types
    if self.average is not None:
      self.average = float(self.average)
    else:
      self.average = 0

    if self.fee is not None:
      self.fee = float(self.fee)
    else:
      self.fee = 0

    if self.filled is not None:
      self.filled = float(self.filled)
    else:
      self.filled = 0

    if self.price is not None:
      self.price = float(self.price)
    else:
      self.price = 0

    if self.remaining is not None:
      self.remaining = float(self.remaining)
    else:
      self.remaining = 0

  def getAverage(self):
    '''Getter'''
    return self.average

  def getDatetime(self):
    '''Getter'''
    return self.datetime

  def getFee(self):
    '''Getter'''
    return self.fee

  def getFilled(self):
    '''Getter'''
    return self.filled

  def getId(self):
    '''Getter'''
    return self.id

  def getInfo(self):
    '''Getter'''
    return self.info

  def getPrice(self):
    '''Getter'''
    return self.price

  def getRemaining(self):
    '''Getter'''
    return self.remaining

  def getSide(self):
    '''Getter'''
    return self.side

  def getStatus(self):
    '''Getter'''
    return self.status

  def getSymbol(self):
    '''Getter'''
    return self.symbol

  def getTimestamp(self):
    '''Getter'''
    return self.timestamp

  def getType(self):
    '''Getter'''
    return self.type

  def toString(self):
    '''To String'''
    return str(self.__dict__)
