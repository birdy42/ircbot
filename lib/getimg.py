#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import urllib2
import urllib
from bs4 import BeautifulSoup

def getImg(text):
  # text = to search
  ### Create opener with Google-friendly user agent
  opener = urllib2.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0')]
  ### Open page & generate soup
  url = "http://www.google.ch/search?tbm=isch&hl=en-CH&source=hp&biw=&bih=&q=" + text + "&btnG=Search+Images&gbv=1"
  page = opener.open(url)
  soup = BeautifulSoup(page, "lxml")
  ### Parse and find
  ### Looks like google contains URLs in <img> tags.
  for cite in soup.findAll('img'):
    img = cite['src']
    bitlyopener = urllib2.build_opener()
    bitlyopener.addheaders = [('User-agent', 'Mozilla/5.0')]
    token = open("getimg/bitlytoken").read().split("\n")[0]
    url = "https://api-ssl.bitly.com/v3/user/link_save?longUrl="+ urllib.quote_plus(img) +"&access_token="+token
    bitlypage = bitlyopener.open(url)
    jsonobj = json.loads(bitlypage.read())
    link = jsonobj["data"]["link_save"]["link"]
    print link
    return link
