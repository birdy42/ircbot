#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

def getRule(text):
  try:
    ruleid = int(text)
    if 0 < ruleid:
      opener = urllib2.build_opener()
      opener.addheaders = [('User-agent', 'Mozilla/5.0')]
      ### Open page & generate soup
      url = "http://www.urbandictionary.com/define.php?term=rule" + str(text)
      page = opener.open(url)
      soup = BeautifulSoup(page, "lxml")
      for div in soup.findAll('div'):
        if div.get('class')==['meaning']:
          if div.string:
            return div.string
  except ValueError:
    return ""
