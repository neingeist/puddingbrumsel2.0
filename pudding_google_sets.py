#!/usr/bin/env python
# vim: set fileencoding=utf-8:
from pysqlite2 import dbapi2 as sqlite
import random
from google_sets import google_sets

class pudding_google_sets:

  def __init__(self, sqlite_file):
    self.connection = sqlite.connect(sqlite_file)
    self.cursor = self.connection.cursor()

    self.cursor.execute("SELECT word FROM words");
    self.words = map(lambda r: r[0], self.cursor.fetchall())
    self.newwords = []

  def get_random_new_words(self):
    gs = google_sets()

    self.newwords += gs.get_new_words(
      self.words[random.randint(0, len(self.words)-1)], 
      self.words[random.randint(0, len(self.words)-1)])

  def store(self):
    for newword in self.newwords:
      print newword
      self.cursor.execute("INSERT OR IGNORE INTO words (word) VALUES(?)", (newword,));
    self.connection.commit()
    
if __name__ == "__main__":
  g = pudding_google_sets("pudding-google-sets.sqlite")
  g.get_random_new_words(); 
  print g.newwords
  #g.store()
