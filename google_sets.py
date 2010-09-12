#!/usr/bin/env python
# vim: set fileencoding=utf-8:
import re
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

class google_sets:

  def get_new_words(self, word1, word2):
    url = 'http://labs.google.com/sets'
    values = { 'q1' : word1, 'q2' : word2 }
    newwords = []

    data = urllib.urlencode(values)
    req = urllib2.Request(url + "?" + data)
    response = urllib2.urlopen(req).read()

    soup = BeautifulSoup(response)
    # recht schoener html code so, bei google sets
    for r in soup.html.body.findAll("font", size=-1, face="Arial, sans-serif"):
      word = r.a.contents[0]
      if re.compile("^http://www.google.com/search\?hl=en&q=").match(r.a["href"]):
        if re.compile("^[a-zäöüß]+$").match(word):
          newwords.append(word)

    return newwords

if __name__ == "__main__":
  g = google_sets()
  print g.get_new_words("rosenkohl", "wirsing")
