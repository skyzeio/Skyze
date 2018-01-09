# Skyze Notifier Manual

## Twitter
uses the `tweepy` library to send a Tweet.
See simple tutorial
      http://nodotcom.org/python-twitter-tutorial.html

### Twitter apps
App is set up at Twitter apps link: https://apps.twitter.com/
Contains all the access codes which are acessed as environment variables as below
    `"consumer_key": os.environ['TWITTER_CONSUMER_KEY'],
    "consumer_secret": os.environ['TWITTER_CONSUMER_SECRET'],
    "access_token": os.environ['TWITTER_ACCESS_TOKEN'],
    "access_token_secret": os.environ['TWITTER_TOKEN_SECRET'`
