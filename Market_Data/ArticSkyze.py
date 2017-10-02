from arctic import Arctic
import quandl
from trading_ig import IGService
from trading_ig.config import config
import os

# Connect to Local MONGODB
store = Arctic('localhost')

# Create the library - defaults to VersionStore
store.initialize_library('NASDAQ')

# Access the library
library = store['NASDAQ']

# Get some data from IG

# Get environment variables for IG
acc_number = os.environ['IG_SERVICE_ACC_NUMBER']
password = os.environ['IG_SERVICE_PASSWORD']
api_key = os.environ['IG_SERVICE_API_KEY']
username = os.environ['IG_SERVICE_USERNAME']
acc_type = os.environ['IG_SERVICE_ACC_TYPE']


# Create IG Session
ig_service = IGService(username, password, api_key, acc_type)
ig_service.create_session()

# Get account info
account_info = ig_service.switch_account(acc_number, False)  # not necessary
print(account_info)

# get position info
open_positions = ig_service.fetch_open_positions()
print("open_positions:\n%s" % open_positions)
print()

epic = 'CS.D.EURUSD.MINI.IP'
resolution = 'D'
num_points = 10
response = ig_service.fetch_historical_prices_by_epic_and_num_points(
    epic, resolution, num_points)
df_ask = response['prices']['ask']
print("ask prices:\n%s" % df_ask)




# Store the data in the library
library.write('AAPL', aapl, metadata={'source': 'Quandl'})

# Reading the data
item = library.read('AAPL')
aapl = item.data
metadata = item.metadata


# Load some data - maybe from Quandl
#aapl = quandl.get("WIKI/AAPL", authtoken="your token here"))
