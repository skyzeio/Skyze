"""Created on 13/10/2017
   @author: michaelnew"""

# Third Party Imports
from datetime import datetime
import json
import os

# eMail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Twitter
import tweepy

# Skyze Imports
from Skyze_Notifier_Service import settings
from Skyze_Standard_Library.SkyzeServiceAbstract import *
import Skyze_Standard_Library.Colourful_Printing as cp
# Skyze Messages
from Skyze_Messaging_Service.Messages.SkyzeMessageTypes import *
from Skyze_Messaging_Service.Messages.MessageMarketDataUpdaterRunComplete \
    import MessageMarketDataUpdaterRunComplete


class SkyzeNotifierService(SkyzeServiceAbstract):
  """Skyze inter-service message logger"""

  def __init__(self, message_bus):
    """Constructor"""
    path_to_service = "Skyze_Notifier_Service"
    super().__init__(message_bus=message_bus, log_path=path_to_service)

  def __sendEmail(self, msg_subject, msg_content):
    ''' From https://coderwall.com/p/d4e_ya/using-python-to-sending-emails-via-aws'''
    log_msg = f"{self.getType()}::sendEmail::NOT IMPLIMENTED::{msg_subject}\n{msg_content}"
    self._logger.log_info(log_msg)

    # AWS Config
    # EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
    # EMAIL_HOST_USER = 'foo'
    # EMAIL_HOST_PASSWORD = 'bar'
    # EMAIL_PORT = 587
    #
    # msg = MIMEMultipart('alternative')
    # msg['Subject'] = msg_subject
    # msg['From'] = "Skyze Notifer"
    # msg['To'] = "mikenew16@gmail.com"
    #
    # html = open('index.html').read()
    #
    # mime_text = MIMEText(html, 'html')
    # msg.attach(mime_text)
    #
    # s = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    # s.starttls()
    # s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    # s.sendmail(me, you, msg_content)
    # s.quit()

  def __get_twitter_api(self, cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

  def __sendTweet(self, msg_subject, msg_content):
    ''' uses tweepy to send a Tweet'''
    log_msg = f"{self.getType()}::sendTweet::{msg_content}"
    self._logger.log_info(log_msg)
    cfg = {
        "consumer_key": os.environ['TWITTER_CONSUMER_KEY'],
        "consumer_secret": os.environ['TWITTER_CONSUMER_SECRET'],
        "access_token": os.environ['TWITTER_ACCESS_TOKEN'],
        "access_token_secret": os.environ['TWITTER_TOKEN_SECRET']
    }

    api = self.__get_twitter_api(cfg)
    max_tweet_length = 140
    tweet = f"{msg_subject} :: {msg_content}"[0:max_tweet_length - 1]
    status = api.update_status(status=tweet)
    return

  def __sendSMS(self, msg_subject, msg_content):
    log_msg = f"{self.getType()}::sendSMS::NOT IMPLIMENTED Routed to Tweet::{msg_content}"
    self._logger.log_info(log_msg)
    self.__sendTweet(msg_subject, msg_content)

  def receiveMessage(self, message_received):
    """Gets the mssage from the bus and routes internally"""
    # Parent class processing
    super().receiveMessage(message_received)
    # Route to appropriate service
    message_type = message_received.getMessageType()
    if message_type == SkyzeMessageType.NOTIFICATION:
      pass
    elif message_type == SkyzeMessageType.MARKET_DATA_UPDATER_RUN_COMPLETE:
      # TODO check user notification settings thensend apprpriately
      msg_subject = "Mkt Data Update Complete: " \
          + message_received.getMessageContent()
      msg_content = msg_subject
      self.__sendEmail(msg_subject, msg_content)
      self.__sendSMS(msg_subject, msg_content)
    else:
      self._unknownMessageTypeError(message_received)
