"""Created on 30 / 12 / 2017 @author: michaelnew"""


# Standard Libraries

# Skyze libraries - Required
from Skyze_Standard_Library.Unit_Test.UnitTestSkyzeAbstract import *

# Skyze libraries - Test Case Specific
from Skyze_Standard_Library.TradingPair import *
from Skyze_Standard_Library.TradingPairIterator import *


class TradingPairIterator_test(UnitTestSkyzeAbstract):
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

  def disable_test_init_string_constructor(self):
    print("yup test_list_markets")

    class_tested = "TradingPair"
    test_columns = ["zzz"]

    # Test Data
    separator = "_"
    test_data = \
        ['BTC_AMP', 'BTC_ARDR', 'BTC_BCH', 'BTC_BCN', 'BTC_BCY',
         'BTC_BELA', 'BTC_BLK', 'BTC_BTCD', 'BTC_BTM', 'BTC_BTS', 'BTC_BURST',
         'BTC_CLAM', 'BTC_CVC', 'BTC_DASH', 'BTC_DCR', 'BTC_DGB', 'BTC_DOGE',
         'BTC_EMC2', 'BTC_ETC', 'BTC_ETH', 'BTC_EXP', 'BTC_FCT', 'BTC_FLDC',
         'BTC_FLO', 'BTC_GAME', 'BTC_GAS', 'BTC_GNO', 'BTC_GNT', 'BTC_GRC',
         'BTC_HUC', 'BTC_LBC', 'BTC_LSK', 'BTC_LTC', 'BTC_MAID', 'BTC_NAV',
         'BTC_NEOS', 'BTC_NMC', 'BTC_NXC', 'BTC_NXT', 'BTC_OMG', 'BTC_OMNI',
         'BTC_PASC', 'BTC_PINK', 'BTC_POT', 'BTC_PPC', 'BTC_RADS', 'BTC_REP',
         'BTC_RIC', 'BTC_SBD', 'BTC_SC', 'BTC_STEEM', 'BTC_STORJ', 'BTC_STR',
         'BTC_STRAT', 'BTC_SYS', 'BTC_VIA', 'BTC_VRC', 'BTC_VTC', 'BTC_XBC',
         'BTC_XCP', 'BTC_XEM', 'BTC_XMR', 'BTC_XPM', 'BTC_XRP', 'BTC_XVC',
         'BTC_ZEC', 'BTC_ZRX', 'ETH_BCH', 'ETH_CVC', 'ETH_ETC', 'ETH_GAS',
         'ETH_GNO', 'ETH_GNT', 'ETH_LSK', 'ETH_OMG', 'ETH_REP', 'ETH_STEEM',
         'ETH_ZEC', 'ETH_ZRX', 'USDT_BCH', 'USDT_BTC', 'USDT_DASH', 'USDT_ETC',
         'USDT_ETH', 'USDT_LTC', 'USDT_NXT', 'USDT_REP', 'USDT_STR', 'USDT_XMR',
         'USDT_XRP', 'USDT_ZEC', 'XMR_BCN', 'XMR_BLK', 'XMR_BTCD', 'XMR_DASH',
         'XMR_LTC', 'XMR_MAID', 'XMR_NXT', 'XMR_ZEC']

    target_results = ['BTC', 'AMP', 'BTC', 'ARDR', 'BTC', 'BCH', 'BTC', 'BCN', 'BTC', 'BCY',
                      'BTC', 'BELA', 'BTC', 'BLK', 'BTC', 'BTCD', 'BTC', 'BTM', 'BTC', 'BTS', 'BTC', 'BURST',
                      'BTC', 'CLAM', 'BTC', 'CVC', 'BTC', 'DASH', 'BTC', 'DCR', 'BTC', 'DGB', 'BTC', 'DOGE',
                      'BTC', 'EMC2', 'BTC', 'ETC', 'BTC', 'ETH', 'BTC', 'EXP', 'BTC', 'FCT', 'BTC', 'FLDC',
                      'BTC', 'FLO', 'BTC', 'GAME', 'BTC', 'GAS', 'BTC', 'GNO', 'BTC', 'GNT', 'BTC', 'GRC',
                      'BTC', 'HUC', 'BTC', 'LBC', 'BTC', 'LSK', 'BTC', 'LTC', 'BTC', 'MAID', 'BTC', 'NAV',
                      'BTC', 'NEOS', 'BTC', 'NMC', 'BTC', 'NXC', 'BTC', 'NXT', 'BTC', 'OMG', 'BTC', 'OMNI',
                      'BTC', 'PASC', 'BTC', 'PINK', 'BTC', 'POT', 'BTC', 'PPC', 'BTC', 'RADS', 'BTC', 'REP',
                      'BTC', 'RIC', 'BTC', 'SBD', 'BTC', 'SC', 'BTC', 'STEEM', 'BTC', 'STORJ', 'BTC', 'STR',
                      'BTC', 'STRAT', 'BTC', 'SYS', 'BTC', 'VIA', 'BTC', 'VRC', 'BTC', 'VTC', 'BTC', 'XBC',
                      'BTC', 'XCP', 'BTC', 'XEM', 'BTC', 'XMR', 'BTC', 'XPM', 'BTC', 'XRP', 'BTC', 'XVC',
                      'BTC', 'ZEC', 'BTC', 'ZRX', 'ETH', 'BCH', 'ETH', 'CVC', 'ETH', 'ETC', 'ETH', 'GAS',
                      'ETH', 'GNO', 'ETH', 'GNT', 'ETH', 'LSK', 'ETH', 'OMG', 'ETH', 'REP', 'ETH', 'STEEM',
                      'ETH', 'ZEC', 'ETH', 'ZRX', 'USDT', 'BCH', 'USDT', 'BTC', 'USDT', 'DASH', 'USDT', 'ETC',
                      'USDT', 'ETH', 'USDT', 'LTC', 'USDT', 'NXT', 'USDT', 'REP', 'USDT', 'STR', 'USDT', 'XMR',
                      'USDT', 'XRP', 'USDT', 'ZEC', 'XMR', 'BCN', 'XMR', 'BLK', 'XMR', 'BTCD', 'XMR', 'DASH',
                      'XMR', 'LTC', 'XMR', 'MAID', 'XMR', 'NXT', 'XMR', 'ZEC']

  def test_findStrings(self):

    class_tested = "TradingPairIterator"
    function_tested = "findStrings"
    test_columns = ["zzz"]

    # Test Data
    test_data_separator = "_"
    test_data_pair_strings2 = \
        ['BTC_AMP', 'BTC_ARDR', 'BTC_BCH', 'BTC_BCN', 'BTC_BCY',
         'BTC_BELA', 'BTC_BLK', 'BTC_BTCD', 'BTC_BTM', 'BTC_BTS', 'BTC_BURST',
         'BTC_CLAM', 'BTC_CVC', 'BTC_DASH', 'BTC_DCR', 'BTC_DGB', 'BTC_DOGE',
         'BTC_EMC2', 'BTC_ETC', 'BTC_ETH', 'BTC_EXP', 'BTC_FCT', 'BTC_FLDC',
         'BTC_FLO', 'BTC_GAME', 'BTC_GAS', 'BTC_GNO', 'BTC_GNT', 'BTC_GRC',
         'BTC_HUC', 'BTC_LBC', 'BTC_LSK', 'BTC_LTC', 'BTC_MAID', 'BTC_NAV',
         'BTC_NEOS', 'BTC_NMC', 'BTC_NXC', 'BTC_NXT', 'BTC_OMG', 'BTC_OMNI',
         'BTC_PASC', 'BTC_PINK', 'BTC_POT', 'BTC_PPC', 'BTC_RADS', 'BTC_REP',
         'BTC_RIC', 'BTC_SBD', 'BTC_SC', 'BTC_STEEM', 'BTC_STORJ', 'BTC_STR',
         'BTC_STRAT', 'BTC_SYS', 'BTC_VIA', 'BTC_VRC', 'BTC_VTC', 'BTC_XBC',
         'BTC_XCP', 'BTC_XEM', 'BTC_XMR', 'BTC_XPM', 'BTC_XRP', 'BTC_XVC',
         'BTC_ZEC', 'BTC_ZRX', 'ETH_BCH', 'ETH_CVC', 'ETH_ETC', 'ETH_GAS',
         'ETH_GNO', 'ETH_GNT', 'ETH_LSK', 'ETH_OMG', 'ETH_REP', 'ETH_STEEM',
         'ETH_ZEC', 'ETH_ZRX', 'USDT_BCH', 'USDT_BTC', 'USDT_DASH', 'USDT_ETC',
         'USDT_ETH', 'USDT_LTC', 'USDT_NXT', 'USDT_REP', 'USDT_STR', 'USDT_XMR',
         'USDT_XRP', 'USDT_ZEC', 'XMR_BCN', 'XMR_BLK', 'XMR_BTCD', 'XMR_DASH',
         'XMR_LTC', 'XMR_MAID', 'XMR_NXT', 'XMR_ZEC']
    test_data_pair_strings = \
        ['BTC_ZEC', 'BTC_ZRX', 'ETH_BCH', 'ETH_ZEC', 'ETH_ZRX', 'USDT_BCH']

    test_data_search_pair_strings = \
        ["BTC_ZRX", "ZRX_ETH", "ZRX_BLK", "BCN_ZRX"]
    target_results_pair_strings = "BTC_ZRX, ETH_ZRX, None, None"

    # Output Headings
    self.printTestHeader(self._package_name, class_tested,
                         "internal", "internal", test_columns)

    # Output test data
    print("\n\n======= Test Data =================================== ")
    # construct the pairs
    test_pairs = []
    for pair in test_data_pair_strings:
      test_pairs.append(TradingPair.init_string(pair, "_"))

    test_pairs_iterator = TradingPairIterator(test_pairs)

    print("Count Pair Universe Strings: " + str(len(test_data_pair_strings)))
    print(test_data_pair_strings)
    print("Count Pair Universe: " + str(test_pairs_iterator.length()))
    print(str(test_pairs_iterator.toString()) + "\n\n")

    test_data_search_pairs = []
    for pair in test_data_search_pair_strings:
      test_data_search_pairs.append(TradingPair.init_string(pair, "_"))

    test_search_iterator = TradingPairIterator(test_data_search_pairs)

    print("Count Searches String: " + str(len(test_data_search_pair_strings)))
    print(str(test_data_search_pair_strings) + "\n\n")
    print("Count Searches: " + str(test_search_iterator.length()))
    print(str(test_search_iterator.toString()) + "\n\n")

    # Output target_file
    print("\n\n======= Target Results =================================== ")
    print("Count Target Results Pairs: 2")
    print(str(target_results_pair_strings) + "\n\n")

    # Calcualte

    test_calcs = []
    for pair in test_data_search_pairs:
      test_calcs.append(test_pairs_iterator.findStrings(
          pair.getBase(), pair.getQuote(), test_data_separator))

    test_calcs_iterator = TradingPairIterator(test_calcs)
    test_calcs_pairs_strings = test_calcs_iterator.toString()

    # Output target_file
    print("\n\n======= Test Calculations =================================== ")
    print("Test Calc Pairs: " + str(test_calcs_iterator.length()))
    print(str(test_calcs_pairs_strings))

    # Assert list of pairs the same
    print("\n\n======= Test Assertions =================================== ")
    print("Test Calcs: ", end='')
    assert(test_calcs_pairs_strings == target_results_pair_strings)
    print("Passed ++++")
    print("All Passed ++++")


if __name__ == '__main__':
  unittest.main()
