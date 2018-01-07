# ROLLBAR

## Notifying of a new environment


curl https://api.rollbar.com/api/1/deploy/ \
  -F access_token=$ROLLBAR_ACCESS_TOKEN \
  -F environment=$ENVIRONMENT \
  -F revision=$REVISION \
  -F local_username=$LOCAL_USERNAME

## Env VARIABLES
ROLLBAR_ACCESS_TOKEN="8f67acbc427a4d6ba80c31516bd355da"
ENVIRONMENT="AWS_1"
REVISION="Bitfinex scheduled 2018-01-07"
LOCAL_USERNAME="not_set"
