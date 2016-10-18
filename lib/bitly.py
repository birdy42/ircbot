#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import urllib2
import urllib
from bs4 import BeautifulSoup

def get(text):
  # text = url
  ### Create opener with Google-friendly user agent
  bitlyopener = urllib2.build_opener()
  bitlyopener.addheaders = [('User-agent', 'Mozilla/5.0')]
  token = open("getimg/bitlytoken").read().split("\n")[0]
  url = "https://api-ssl.bitly.com/v3/user/link_save?longUrl="+ urllib.quote_plus(text) +"&access_token="+token
  bitlypage = bitlyopener.open(url)
  jsonobj = json.loads(bitlypage.read())
  link = jsonobj["data"]["link_save"]["link"]
  print link
  return link
