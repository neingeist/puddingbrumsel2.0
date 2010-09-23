#!/usr/bin/env python
# vim: set fileencoding=utf-8:
import sys
sys.path.insert(0, 'libs/python-twitter')
sys.path.insert(0, 'libs/python-oauth2')

from pudding_google_sets import pudding_google_sets
from pudding import puddingbrumsel
import twitter
import time
import random
import ConfigParser
import os

if __name__ == "__main__":
 
  cp = ConfigParser.ConfigParser()
  cp.read(os.path.expanduser("~/.puddingbrumselrc"))
 
  api = twitter.Api(
    username=cp.get("twitter", "username"),
    password=cp.get("twitter", "password"),
    access_token_key=cp.get("twitter", "access_token_key"),
    access_token_secret=cp.get("twitter", "access_token_secret"),
    input_encoding="utf-8"
    )
  
  sqlite_file = "pudding_google_sets.sqlite"
  pgs = pudding_google_sets(sqlite_file)
  p = puddingbrumsel(pgs)

  while True:
    tweet = p.tweet().encode("utf-8")
    status = api.PostUpdate(tweet)
    print status.text
    
    time.sleep(random.randint(int(cp.get("puddingbrumsel", "minsleep")), 
                              int(cp.get("puddingbrumsel", "maxsleep"))))
