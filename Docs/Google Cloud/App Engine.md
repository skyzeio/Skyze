# Google Cloud App Engine

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Google Cloud App Engine](#google-cloud-app-engine)
	- [Installing Skyze Services](#installing-skyze-services)
		- [install](#install)
		- [Deploy](#deploy)
		- [View app status](#view-app-status)
		- [Update from SkyZe github](#update-from-skyze-github)
	- [Install Cloud Services SDK](#install-cloud-services-sdk)
		- [**./install.sh**](#installsh)
		- [gcloud init --skip-diagnostics](#gcloud-init-skip-diagnostics)

<!-- /TOC -->

## Declaring and managing dependencies

Dependencies for python applications are declared in a standard `requirements.txt` file. For example:

`Flask==0.10.1
python-memcached==1.54`


## Files required
**Git for tutorial** https://github.com/ChrisParsonsDev/googleclouddemos/tree/master/helloworld-python
**YouTube Tutorial** https://www.youtube.com/watch?v=o8XxAWZwnOg
1. `app.yaml`
2. `requirements.txt`
3. `main.py`


## Installing Skyze Services

### install
1. Use dashboard to set up app Engine
2. Start cloud shell
3. Clone fro git `git clone [repo]`
    `git clone https://github.com/SkyzeTrading/Skyze`
4. Test it runs: `dev_appserver.py $PWD`

### Deploy
? CD to directory?
1. Deploy: `gcloud app deploy app.yaml --project skyze-market-data-updater`
2. Defaul URL: http://skyze-market-data-updater.appspot.com/
    which is `http://[YOUR_PROJECT_ID].appspot.com`
3. stream logs from the command line by running: `gcloud app logs tail -s default`
4. To view your application in the web browser run:
  `gcloud app browse`

### View app status
1. go to the App Engine dashboard.
2. Open the menu on the left side of the console.
3. Select the App Engine section.

### Update from SkyZe github
1. Start cloud Shell
2. CD to project directory
3. Pull from GH 'git pull https://github.com/SkyzeTrading/Skyze'

## Install Cloud Services SDK

### **./install.sh**
Welcome to the Google Cloud SDK!

To help improve the quality of this product, we collect anonymized usage data
and anonymized stacktraces when crashes are encountered; additional information
is available at <https://cloud.google.com/sdk/usage-statistics>. You may choose
to opt out of this collection now (by choosing 'N' at the below prompt), or at
any time in the future by running the following command:

   gcloud config set disable_usage_reporting true

Do you want to help improve the Google Cloud SDK (Y/n)?  n


Your current Cloud SDK version is: 174.0.0
The latest available version is: 174.0.0

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                  Components                                                 │
├───────────────┬──────────────────────────────────────────────────────┬──────────────────────────┬───────────┤
│     Status    │                         Name                         │            ID            │    Size   │
├───────────────┼──────────────────────────────────────────────────────┼──────────────────────────┼───────────┤
│ Not Installed │ App Engine Go Extensions                             │ app-engine-go            │  97.7 MiB │
│ Not Installed │ Cloud Bigtable Command Line Tool                     │ cbt                      │   4.0 MiB │
│ Not Installed │ Cloud Bigtable Emulator                              │ bigtable                 │   3.5 MiB │
│ Not Installed │ Cloud Datalab Command Line Tool                      │ datalab                  │   < 1 MiB │
│ Not Installed │ Cloud Datastore Emulator                             │ cloud-datastore-emulator │  15.4 MiB │
│ Not Installed │ Cloud Datastore Emulator (Legacy)                    │ gcd-emulator             │  38.1 MiB │
│ Not Installed │ Cloud Pub/Sub Emulator                               │ pubsub-emulator          │  33.2 MiB │
│ Not Installed │ Emulator Reverse Proxy                               │ emulator-reverse-proxy   │  14.5 MiB │
│ Not Installed │ Google Container Local Builder                       │ container-builder-local  │   3.7 MiB │
│ Not Installed │ Google Container Registry's Docker credential helper │ docker-credential-gcr    │   2.2 MiB │
│ Not Installed │ gcloud Alpha Commands                                │ alpha                    │   < 1 MiB │
│ Not Installed │ gcloud Beta Commands                                 │ beta                     │   < 1 MiB │
│ Not Installed │ gcloud app Java Extensions                           │ app-engine-java          │ 116.9 MiB │
│ Not Installed │ gcloud app PHP Extensions                            │ app-engine-php           │  21.9 MiB │
│ Not Installed │ gcloud app Python Extensions                         │ app-engine-python        │   6.2 MiB │
│ Not Installed │ kubectl                                              │ kubectl                  │  15.9 MiB │
│ Installed     │ BigQuery Command Line Tool                           │ bq                       │   < 1 MiB │
│ Installed     │ Cloud SDK Core Libraries                             │ core                     │   6.8 MiB │
│ Installed     │ Cloud Storage Command Line Tool                      │ gsutil                   │   3.0 MiB │
└───────────────┴──────────────────────────────────────────────────────┴──────────────────────────┴───────────┘
To install or remove components at your current SDK version [174.0.0], run:
 $ gcloud components install COMPONENT_ID
 $ gcloud components remove COMPONENT_ID

To update your SDK installation to the latest version [174.0.0], run:
 $ gcloud components update

==> Source [/Users/michaelnew/Dropbox/Aptana_Workspace/Skyze/google-cloud-sdk/completion.bash.inc] in your profile to enable shell command completion for gcloud.
==> Source [/Users/michaelnew/Dropbox/Aptana_Workspace/Skyze/google-cloud-sdk/path.bash.inc] in your profile to add the Google Cloud SDK command line tools to your $PATH.

For more information on how to get started, please visit:
 https://cloud.google.com/sdk/docs/quickstarts

### gcloud init --skip-diagnostics

## Storage
from: https://console.cloud.google.com/appengine/settings?project=skyze-market-data-updater&authuser=1&serviceId=default&versionId=20171007t093717
Default Cloud Storage Bucket

Up to 5GB of Cloud Storage may be used with App Engine applications without enabling billing. Learn more
