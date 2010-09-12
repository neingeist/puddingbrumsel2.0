#!/usr/bin/env python
# vim: set fileencoding=utf-8:
import random
from pysqlite2 import dbapi2 as sqlite

class puddingbrumsel:

  def __init__(self, words):
    self.words = words

  def pick(self, list):
    return list[random.randint(0, len(list)-1)]

  def pudding(self):
    return self.pick([
      "pudding",
      "pudding",
      self.neupudding()
    ])

  def neupudding(self):
    return self.pick(self.words) + "pudding"

  def brums(self):
    return self.pick([
      "*brumms*", 
      "*brums*"
    ])

  def emoticon(self):
    return self.pick([
      ":D",
      ":)",
      "^^"
    ])

  def doubleemoticon(self):
    return self.pick([
      ":D :D",
      ":))",
      "^^ ^^"
    ])

  def sademoticon(self):
    return self.pick([
      ":((",
      ":-(",
      ":/"
    ])

  def adj(self):
    return self.pick([
      u"köstlicher",
      "knuspriger", 
      "knackiger",
      "lecker",
      u"süßer",
    ])

  def tweet(self):
    return self.pick([
      "<3 " + self.pudding() + " " + self.emoticon(),
      self.pudding() + " " + self.doubleemoticon(),
      self.pudding() + " " + self.brums(), 
      self.pudding() + " " + self.brums() + " " + self.emoticon(),
      self.adj() + " " + self.pudding() + " " + self.brums() + " " + self.emoticon(),
      "hihi. " + self.pudding() + " " + self.brums() +  " " + self.emoticon(),
      "kein " + self.pudding() + " " + self.sademoticon()
    ])


if __name__ == "__main__":
  sqlite_file = "pudding-google-sets.sqlite"
  cursor = sqlite.connect(sqlite_file).cursor()
  cursor.execute("SELECT word FROM words")
  words = map(lambda r: r[0], cursor.fetchall())

  p = puddingbrumsel(words)
  print p.tweet()
