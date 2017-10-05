"""Simple test of pymongo to Skyze AWS Mongo Atlas Sandpit Cloud Cluster"""
import pymongo
from pymongo import MongoClient

# Get the password
mongo_password = "Bruceskyze1!"

# Create a Mongo client to work with the mongod Instance
client = pymongo.MongoClient(
    "mongodb://kay:" + mongo_password
    + "@mycluster0-shard-00-00-wpeiv.mongodb.net:27017,mycluster0-shard-00-01-wpeiv.mongodb.net:27017,mycluster0-shard-00-02-wpeiv.mongodb.net:27017/admin?ssl=true&replicaSet=Mycluster0-shard-0&authSource=admin")
print("\nClient: ")
print(client)

# Confirm connection with existing DB
db_admin = client.admin
print("\n\nDatabase Admin: ")
print(db_admin)

# Get the database
# Note: MongoDB creates databases and collections automatically for you if they don't exist already.
db_market_db = client.skyze_market_database
# or (using dictionary style access) db = client['test-database']
print("\n\nDatabase Market DB: ")
print(db_market_db)

# Getting a Collection
# A collection is a group of documents stored in MongoDB, and can be thought of as roughly the equivalent of a table in a relational database.
cln_poloniex_btc_usdt = db_market_db.poloniex_btc_usdt
# or (using dictionary style access) collection = db['test-collection']
print("\n\nCollection poloniex_btc_usdt: ")
print(cln_poloniex_btc_usdt)


print("\n\n")
