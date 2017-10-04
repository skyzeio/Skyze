# <span style="color:DarkOrange">MongoDB Atlas Set Up</span>

<span style="color:limegreen">Version 1
Date: 4 October 2017 </span>

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [<span style="color:DarkOrange">MongoDB Atlas Set Up</span>](#span-stylecolordarkorangemongodb-atlas-set-upspan)
	- [<span style="color:Fuchsia">IP Whitelist</span>](#span-stylecolorfuchsiaip-whitelistspan)
	- [<span style="color:Fuchsia">Connection</span>](#span-stylecolorfuchsiaconnectionspan)
		- [<span style="color:Fuchsia">Mongo Shell</span>](#span-stylecolorfuchsiamongo-shellspan)
		- [<span style="color:Fuchsia">Skyze</span>](#span-stylecolorfuchsiaskyzespan)
		- [<span style="color:Fuchsia">MongoDB Compass</span>](#span-stylecolorfuchsiamongodb-compassspan)

<!-- /TOC -->



## <span style="color:Fuchsia">IP Whitelist</span>
Currently all ip's are whitelisted

## <span style="color:Fuchsia">Connection</span>

### <span style="color:Fuchsia">Mongo Shell</span>
** Install ** `brew install mongodb --with-openssl`

```
mongo "mongodb://skyze-1-shard-00-00-oigrk.mongodb.net:27017,skyze-1-shard-00-01-oigrk.mongodb.net:27017,skyze-1-shard-00-02-oigrk.mongodb.net:27017/test?replicaSet=Skyze-1-shard-0" --authenticationDatabase admin --ssl --username articskyze --password <PASSWORD>
```


### <span style="color:Fuchsia">MongoDB Compass</span>
** Download Compass **
https://downloads.mongodb.com/compass/mongodb-compass-1.8.2-darwin-x64.dmg



### <span style="color:Fuchsia">Skyze</span>
**Connection String:**

`mongodb://articskyze:<PASSWORD>@skyze-1-shard-00-00-oigrk.mongodb.net:27017,skyze-1-shard-00-01-oigrk.mongodb.net:27017,skyze-1-shard-00-02-oigrk.mongodb.net:27017/test?ssl=true&replicaSet=Skyze-1-shard-0&authSource=admin`

**Replace PASSWORD with the password for the articskyze user**
Replace PASSWORD with the password for the articskyze user. Please note that any special characters in your password (%, @, and :) will need to be URL encoded.

**View driver connection examples**
Failed connections can result from old versions of drivers. Check your driver version and view connection examples for your platform:
https://docs.atlas.mongodb.com/driver-connection/?_ga=2.63144043.59696586.1507086577-550625816.1504921890#python-driver-example

```client = pymongo.MongoClient("mongodb://kay:myRealPassword@mycluster0-shard-00-00-wpeiv.mongodb.net:27017,mycluster0-shard-00-01-wpeiv.mongodb.net:27017,mycluster0-shard-00-02-wpeiv.mongodb.net:27017/admin?ssl=true&replicaSet=Mycluster0-shard-0&authSource=admin")
db = client.test```

after you have run the installer from https://www.python.org to install Python 3.6, you must run the following script to install an up-to-date CA certificates bundle in order to connect to Atlas:

`open "/Applications/Python 3.6/Install Certificates.command"`

For more information on Python 3.6 installers for macOS from https://www.python.org, see https://bugs.python.org/issue29065#msg283984. Earlier versions of Python as well as Python 3.6 installed by other means are not affected.
MINIMUM DRIVER VERSION(S)
Version 3.2

To connect to an Atlas M0 (Free Tier) cluster, you must use Python 2.7.9+ and use a Python driver version that supports MongoDB 3.4. For complete documentation on compatibility between the Python driver and MongoDB, see the MongoDB compatibility matrix.
