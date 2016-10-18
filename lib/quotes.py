#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint

def add(text, author):
  open("quotes/quotes.txt", 'a').write(text + "\n")
  open("quotes/authors.txt", 'a').write(author + "\n")

def show(text, author):
  if text == 'last':
    last = open("quotes/quotes.txt").read().split("\n")[-2:-1][0]
    lastauthor = open("quotes/authors.txt").read().split("\n")[-2:-1][0]
    return " " + last + " | added by " + lastauthor
  else:
    allquotes = open("quotes/quotes.txt").read()
    allauthors = open("quotes/authors.txt").read()
    quotes = allquotes.split("\n")[:-1]
    authors = allauthors.split("\n")
    try:
      quoteid = int(text)
      if 0 <= quoteid < len(quotes):
        return " " + quotes[quoteid] + " | added by "+ authors[quoteid]
      else:
        return "Quote does not exist"
    except ValueError:
      return "Quote does not exist"

def random(text, author):
  allquotes = open("quotes/quotes.txt").read()
  allauthors = open("quotes/authors.txt").read()
  quotes = allquotes.split("\n")
  authors = allauthors.split("\n")
  qid = randint(0,len(quotes)-2)
  return " " + str(qid) + " : "+ quotes[qid] + " | added by "+authors[qid]

def search(text, author):
  allquotes = open("quotes/quotes.txt").read()
  quotes = allquotes.split("\n")
  ids = ""
  i = 0
  for quote in quotes:
    if text.lower() in quote.lower():
      ids = ids + " " + str(i)
    i = i + 1

  return ids

def qfrom(text, author):
  allquotes = open("quotes/authors.txt").read()
  quotes = allquotes.split("\n")
  ids = ""
  i = 0
  for quote in quotes:
    if text in quote:
      ids = ids + " " + str(i)
    i = i + 1

  return ids

import threading
from time import sleep

def randomQuote(bot):
  bot.msg("#BFF", random('a','b'))
  sleep(3600)
  randomQuote(bot)


def startRandomQt(bot):
  t = threading.Thread(target=randomQuote, args=(bot,))
  t.start()
