#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint

def add(name, url):
  open("memes/memes.txt", 'a').write(name + " "  + url + "\n")

def show(text):
  allmemes = open("memes/memes.txt").read()
  memes = allmemes.split("\n")[:-1]
  for meme in memes:
    meme = meme.split(" ")
    if meme[0] == text:
      return meme[1]
  return "Meme does not exist."

def random():
  allmemes = open("memes/memes.txt").read()
  memes = allmemes.split("\n")
  mid = randint(0,len(memes)-2)
  return " " + memes[mid].split(" ")[0] + ": "+memes[mid].split(" ")[1]
