#!/usr/bin/env python
import os
import requests
from dotenv import load_dotenv
from dotenv import find_dotenv

# load environment variables
load_dotenv(find_dotenv())
pushover_token = os.environ.get("PUSHOVER_TOKEN")
pushover_user = os.environ.get("PUSHOVER_USER")
pushover_title = os.environ.get("PUSHOVER_TITLE")

# message for sit ios app
sit_message = "Take 5. It's time to meditate with sit."

# data to send to pushover
payload = {
  "token": pushover_token,
  "user": pushover_user,
  "title": pushover_title,
  "message": sit_message
}

# send post request to pushover
def pushover_post():
  try:
    r = requests.post('https://api.pushover.net:443/1/messages.json', data=payload)
  except requests.exceptions.RequestException as e:
    print e
    sys.exit(1)
  else:
    print(sit_message)

pushover_post()

