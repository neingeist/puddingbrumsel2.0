#!/usr/bin/env python
from pysqlite2 import dbapi2 as sqlite
import urllib
import urllib2
import random
import re
from BeautifulSoup import BeautifulSoup

class google_sets_fnord:

  def __init__(self, sqlite_file):
    self.connection = sqlite.connect(sqlite_file)
    self.cursor = self.connection.cursor()

    self.cursor.execute("SELECT word FROM words");
    self.words = map(lambda r: r[0], self.cursor.fetchall())
    self.newwords = []

  def get_new_words(self, word1, word2):
    url = 'http://labs.google.com/sets'
    values = { 'q1' : word1, 'q2' : word2 }
    
    data = urllib.urlencode(values) 
    req = urllib2.Request(url + "?" + data)
    response = urllib2.urlopen(req).read()

    soup = BeautifulSoup(response)
    # recht schoener html code so, bei google sets
    for r in soup.html.body.findAll("font", size=-1, face="Arial, sans-serif"):
      word = r.a.contents[0]
      if re.compile("^http://www.google.com/search\?hl=en&q=").match(r.a["href"]):
        self.newwords.append(word)

  def get_random_new_words(self):
    self.get_new_words(self.words[random.randint(0, len(self.words)-1)], 
                              self.words[random.randint(0, len(self.words)-1)])

  def store(self):
    for newword in self.newwords:
      print newword
      self.cursor.execute("INSERT INTO words (word) VALUES(?)", (newword,));
    self.connection.commit()
    

g = google_sets_fnord("pudding-google-sets.sqlite")
g.get_random_new_words(); 
g.store()
