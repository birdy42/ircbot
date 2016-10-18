#!/usr/bin/python
# -*- coding: utf-8 -*-
def leet(phrase):
  list_leet = {
    "a":"/-\\",
    "b":"|3",
    "c":"(",
    "d":"|)",
    "e":"3",
    "f":"|=",
    "g":"6",
    "h":"|-|",
    "i":"!",
    "j":"_)",
    "k":"|<",
    "l":"|_",
    "m":"|\\/|",
    "n":"|\\|",
    "o":"()",
    "p":"|>",
    "q":"()_",
    "r":"|2",
    "s":"5",
    "t":"7",
    "u":"|_|",
    "v":"\\/",
    "w":"\\/\\/",
    "x":"><",
    "y":"`/",
    "z":"7_"
  }
  line = ""
  for i in phrase:
    if i.lower() in list_leet:
      line += list_leet[i.lower()]
    else:
      line += i
  return line
