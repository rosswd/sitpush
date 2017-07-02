#!/usr/bin/env python
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
r = requests.post('https://api.pushover.net:443/1/messages.json', data=payload)

# check if request was received by pushover.net
if (r.status_code == 200):
  print(sit_message)
else:
  print('request to pushover.net was not successful!')
