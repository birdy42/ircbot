#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint

def add(text, author):
  open("ctfs/ctfs.txt", 'a').write(text + "\n")

def show(text, author):
  if text == 'last':
    last = open("ctfs/ctfs.txt").read().split("\n")[-2:-1][0]
    return " " + last 
  else:
    allctfs = open("ctfs/ctfs.txt").read()
    ctfs = allctfs.split("\n")[:-1]
    try:
      ctfid = int(text)
      if 0 <= ctfid < len(ctfs):
        return " " + ctfs[ctfid] 
      else:
        return "CTF does not exist"
    except ValueError:
      return "CTF does not exist"

def search(text, author):
  allctfs = open("ctfs/ctfs.txt").read()
  ctfs = allctfs.split("\n")
  ids = ""
  i = 0
  for ctf in ctfs:
    if text.lower() in ctf.lower():
      ids = ids + " " + str(i)
    i = i + 1

  return ids
