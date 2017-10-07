# Google Cloud App Engine

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Google Cloud App Engine](#google-cloud-app-engine)
	- [install](#install)
	- [Deploy](#deploy)
	- [View app status](#view-app-status)
	- [Update from SkyZe github](#update-from-skyze-github)

<!-- /TOC -->

## install
1. Use dashboard to set up app Engine
2. Start cloud shell
3. Clone fro git `git clone [repo]`
    `git clone https://github.com/SkyzeTrading/Skyze`
4. Test it runs: `dev_appserver.py $PWD`

## Deploy
? CD to directory?
1. Deploy: `gcloud app deploy app.yaml --project skyze-market-data-updater`
2. Defaul URL: http://skyze-market-data-updater.appspot.com/
    which is `http://[YOUR_PROJECT_ID].appspot.com`
3. stream logs from the command line by running: `gcloud app logs tail -s default`
4. To view your application in the web browser run:
  `gcloud app browse`

## View app status
1. go to the App Engine dashboard.
2. Open the menu on the left side of the console.
3. Select the App Engine section.

## Update from SkyZe github
1. Start cloud Shell
2. CD to project directory
3. Pull from GH 'git pull https://github.com/SkyzeTrading/Skyze'
