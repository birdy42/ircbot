import urllib2
import re
from random import randint

def getBeer():
  url = "http://beeroverip.org/random/"
  opener = urllib2.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0')]
  page = opener.open(url)
  p = re.compile(ur'<em>(.*)<\/em>')
  beer = re.search(p, page.read()).group(1)
  return beer

def getDevScuse():
  url = "http://developerexcuses.com/"
  opener = urllib2.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0')]
  page = opener.open(url)
  p = re.compile(ur'\#333\;\">(.*)<\/a')
  scuse = re.search(p, page.read()).group(1)
  return scuse

def getBitoduc():
  dico = open("bitoduc/dico.words", 'r').read()[:-1].split("\n")
  return dico[randint(0,len(dico))]
