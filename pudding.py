#!/usr/bin/env python
# vim: set fileencoding=utf-8:
import random
from pudding_google_sets import pudding_google_sets

class puddingbrumsel:

  def __init__(self, pgs):
    self.pgs = pgs

  def pick(self, list):
    return list[random.randint(0, len(list)-1)]

  def pudding(self):
    return self.pick([
      "pudding",
      "pudding",
      self.neupudding()
    ])

  def neupudding(self):
    return pgs.get_random_word() + "pudding"

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
      "mag " + self.pudding() + " " + self.emoticon(),
      self.pudding() + " " + self.brums() + " " + self.emoticon(),
      self.adj() + " " + self.pudding() + " " + self.brums() + " " + self.emoticon(),
      "hihi. " + self.pudding() + " " + self.brums() +  " " + self.emoticon(),
      "kein " + self.pudding() + " " + self.sademoticon(),
      self.pudding() + " alle. " + self.sademoticon(),
      "wo " + self.brums() + " isser? der " + self.pudding() + "?",
    ])


if __name__ == "__main__":
  sqlite_file = "pudding_google_sets.sqlite"
  pgs = pudding_google_sets(sqlite_file)
  p = puddingbrumsel(pgs)
  print p.tweet()
