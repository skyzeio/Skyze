# Deploying Skyze

## AWS

### Environment Variables

`# Rollbar
ROLLBAR_ACCESS_TOKEN="xxx"
ENVIRONMENT="AWS_1"
REVISION="Bitfinex_scheduled_2018_01_07"
LOCAL_USERNAME="not_set"

# Virtual Env Wrapper (not sure if needed for Ubuntu)
export WORKON_HOME=~/Dropbox/Aptana_Workspace/Virtual_Environments
source /usr/local/bin/virtualenvwrapper.sh

# Twitter
export TWITTER_CONSUMER_KEY="xxx"
export TWITTER_CONSUMER_SECRET="xxx"
export TWITTER_ACCESS_TOKEN="xxx"
export TWITTER_TOKEN_SECRET="xxx"

# Useful Aliasa Mac
alias cdaws='cd /Users/michaelnew/Dropbox/Trading/Skyze\ Trading/AWS\ Server'
alias logonaws='ssh -i MikeKeyPair.pem ubuntu@ec2-52-206-73-25.compute-1.amazonaws.com'

# Useful Aliasa Ubuntu

# Useful Aliasa Both
alias cdskyze='cd ~/Dropbox/Aptana_Workspace/Skyze'
alias prp='pipenv run python3'
alias gpushodm='git push origin develop master'`

set them by:

1. `sudo vim /etc/environment`
2. set variables
3. `source /etc/environment`

### Notify ROLLBAR

`curl https://api.rollbar.com/api/1/deploy/ \
  -F access_token=$ROLLBAR_ACCESS_TOKEN \
  -F environment=$ENVIRONMENT \
  -F revision=$REVISION \
  -F local_username=$LOCAL_USERNAME`
