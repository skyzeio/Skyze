"""Created on 30 / 12 / 2017 @author: michaelnew"""


# Standard Libraries

# Skyze libraries - Required
from Skyze_Standard_Library.Unit_Test.UnitTestSkyzeAbstract import *

# Skyze libraries - Test Case Specific
from Skyze_Standard_Library.Order import *


class TradingPair_test(UnitTestSkyzeAbstract):
  """Test the Triangular Arbitrage Strategy Class"""

  _package_name = "Skyze_Strategies_Library"

  def _printParameters(self,
                       p_exchanges,
                       p_excluded_markets,
                       p_arb_margin):
    parameters = "\tp_exchanges:\t" + str(p_exchanges) + \
                 "\tp_excluded_markets:\t" + str(p_excluded_markets) + \
                 "\tp_arb_margin:\t" + str(p_arb_margin)
    print(parameters + "\n")

  def test_equility(self):

    class_tested = "Order"
    test_columns = []

    # Test Data
    separator = "_"
    test_data = {'amount': 10.0,
                 'average': 0.0,
                 'datetime': '2018-01-15T21:44:04.698Z',
                 'fee': None,
                 'filled': 0.0,
                 'id': '7216227905',
                 'info': {'avg_execution_price': '0.0',
                          'cid': 78243675637,
                          'cid_date': '2018-01-15',
                          'exchange': 'bitfinex',
                          'executed_amount': '0.0',
                          'gid': None,
                          'id': 7216227905,
                          'is_cancelled': False,
                          'is_hidden': False,
                          'is_live': True,
                          'oco_order': None,
                          'order_id': 7216227905,
                          'original_amount': '10.0',
                          'price': '53.572',
                          'remaining_amount': '10.0',
                          'side': 'buy',
                          'src': 'api',
                          'symbol': 'qtmusd',
                          'timestamp': '1516052643.698736796',
                          'type': 'exchange market',
                          'was_forced': False},
                 'price': 53.572,
                 'remaining': 10.0,
                 'side': 'buy',
                 'status': 'open',
                 'symbol': 'QTUM/USD',
                 'timestamp': 1516052643698,
                 'type': 'market',
                 'mike': 'mike'}

    target_results = test_data

    # Output Headings
    self.printTestHeader(self._package_name, class_tested,
                         "internal", "internal", test_columns)

    # Output test data
    print("\n\n======= Test Data =================================== ")
    print(str(test_data) + "\n\n")

    # Output target_file
    print("\n\n======= Target Reulsts =================================== ")
    print(str(target_results) + "\n\n")

    # ========= Calcualte =============================================
    order = Order(test_data)
    test_calcs = order.__dict__

    # Output target_file
    print("\n\n======= Test Reulsts =================================== ")
    print("Test Calc: " + str(test_calcs))

    # Assert list of pairs the same
    assert(test_calcs == target_results)

  def test_init(self):

    class_tested = "Order"
    function_tested = "__init__"
    test_columns = []

    # Test Data
    separator = "_"
    test_data = {'amount': 10.0,
                 'average': 0.0,
                 'datetime': '2018-01-15T21:44:04.698Z',
                 'fee': None,
                 'filled': 0.0,
                 'id': '7216227905',
                 'info': {'avg_execution_price': '0.0',
                          'cid': 78243675637,
                          'cid_date': '2018-01-15',
                          'exchange': 'bitfinex',
                          'executed_amount': '0.0',
                          'gid': None,
                          'id': 7216227905,
                          'is_cancelled': False,
                          'is_hidden': False,
                          'is_live': True,
                          'oco_order': None,
                          'order_id': 7216227905,
                          'original_amount': '10.0',
                          'price': '53.572',
                          'remaining_amount': '10.0',
                          'side': 'buy',
                          'src': 'api',
                          'symbol': 'qtmusd',
                          'timestamp': '1516052643.698736796',
                          'type': 'exchange market',
                          'was_forced': False},
                 'price': 53.572,
                 'remaining': 10.0,
                 'side': 'buy',
                 'status': 'open',
                 'symbol': 'QTUM/USD',
                 'timestamp': 1516052643698,
                 'type': 'market',
                 'mike': 'mike'}

    target_results = test_data

    # Output Headings
    self.printTestHeader(self._package_name, class_tested,
                         "internal", "internal", test_columns)
    print(f"Function Tested: {function_tested}")

    # Output test data
    print("\n\n======= Test Data =================================== ")
    print(str(test_data) + "\n\n")

    # Output target_file
    print("\n\n======= Target Reulsts =================================== ")
    print(str(target_results) + "\n\n")

    # ========= Calcualte =============================================
    order = Order(test_data)
    test_calcs = order.__dict__

    # Output target_file
    print("\n\n======= Test Reulsts Init =================================== ")
    print("Test Calc: " + str(test_calcs))

    # Assert list of pairs the same
    assert(test_calcs == target_results)

    print("\n\n======= Test Reulsts getID =================================== ")
    print(order.toString())
    print("Test Calc Type: " + str(type(order.getId())))
    print("Test Calc: " + order.getId())

    # Assert list of pairs the same
    assert(order.getId() == target_results['id'])
    assert(order.getAverage() == target_results['average'])
    assert(order.getDatetime() == target_results['datetime'])
    assert(order.getFee() == target_results['fee'])
    assert(order.getFilled() == target_results['filled'])
    assert(order.getInfo() == target_results['info'])
    assert(order.getPrice() == target_results['price'])
    assert(order.getRemaining() == target_results['remaining'])
    assert(order.getSide() == target_results['side'])
    assert(order.getStatus() == target_results['status'])
    assert(order.getSymbol() == target_results['symbol'])
    assert(order.getTimestamp() == target_results['timestamp'])
    assert(order.getType() == target_results['type'])


if __name__ == '__main__':
  unittest.main()
