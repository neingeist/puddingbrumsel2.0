#!/usr/bin/env python
# vim: set fileencoding=utf-8:
from pysqlite2 import dbapi2 as sqlite
import random
from google_sets import google_sets
import enchant

class pudding_google_sets:

  def __init__(self, sqlite_file):
    self.connection = sqlite.connect(sqlite_file)
    self.cursor = self.connection.cursor()

    self.cursor.execute("SELECT word FROM words");
    self.words = map(lambda r: r[0], self.cursor.fetchall())
    self.newwords = []

  def get_random_word(self):
    return self.words[random.randint(0, len(self.words)-1)]

  def get_random_new_words(self):
    gs = google_sets()

    self.newwords += gs.get_new_words(
      self.get_random_word(),
      self.get_random_word()
    )

  def store(self):
    d = enchant.Dict("de_DE")
    for newword in self.newwords:
      if d.check(newword.capitalize()):
        print newword
        self.cursor.execute("INSERT OR IGNORE INTO words (word) VALUES(?)", (newword,));
    self.connection.commit()
    
if __name__ == "__main__":
  g = pudding_google_sets("pudding_google_sets.sqlite")
  g.get_random_new_words(); 
  print g.newwords
  g.store()
