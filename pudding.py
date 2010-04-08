#!/usr/bin/env python
import random
from pysqlite2 import dbapi2 as sqlite

class puddingbrumsel:

  def __init__(self, sqlite_file):
    self.connection = sqlite.connect(sqlite_file)
    self.cursor = self.connection.cursor()

    self.cursor.execute("SELECT word FROM words");
    self.words = map(lambda r: r[0], self.cursor.fetchall())

  def pudding(self):
    return "pudding"

  def neupudding(self):
    return self.words[random.randint(0, len(self.words)-1)] + "pudding"

  def brumms(self):
    if random.randint(0, 1):
      return "*brumms*"
    else:
      return "*brums*"

  def tweet(self):
    if random.randint(0, 3) == 0:
      tweet = self.neupudding()
    else:
      tweet = self.pudding()

    if len(tweet) < 120:
      tweet += self.brumms() 

    return tweet


p = puddingbrumsel("pudding-google-sets.sqlite")
print p.tweet()
