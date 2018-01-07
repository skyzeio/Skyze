# Deploying Skyze

## AWS

### Environment Variables
`ROLLBAR_ACCESS_TOKEN="8f67acbc427a4d6ba80c31516bd355da"
ENVIRONMENT="AWS_1"
REVISION="Bitfinex_scheduled_2018_01_07"
LOCAL_USERNAME="not_set"`

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
