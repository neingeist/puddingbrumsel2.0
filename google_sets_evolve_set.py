#!/usr/bin/env python
# vim: set fileencoding=utf-8:
import random
from google_sets import google_sets
import enchant
import time

wordset = ["wirsing", "rotkohl"]

gs = google_sets()
d = enchant.Dict("de_DE")

def get_random_word():
  return random.choice(wordset)

def get_new_words(w1, w2):
  return gs.get_new_words(w1, w2, lambda w: d.check(w.capitalize()))

if __name__ == "__main__":
  while True:
    for word in get_new_words(get_random_word(), get_random_word()):
      if word not in wordset:
        print word
        wordset.append(word)
    time.sleep(10)
