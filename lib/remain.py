#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime

def get(pseudo, author, folder):
  if pseudo == '':
    pseudo = author
  time = open(folder + "/" + pseudo).read().split(" ")
  h = int(time[0])
  m = int(time[1])
  now = datetime.datetime.now()
  rh = h-now.hour
  rm = m-now.minute
  if rm < 0:
    rm = 60 + rm
    rh = rh - 1
  rh = str(rh)
  rm = str(rm)
  if len(rh) == 1:
    rh = "0"+rh
  if len(rm) == 1:
    rm = "0"+rm
  return "Remaining for "+ pseudo + ": "+ rh + ":" + rm


def setR(hours, minutes, author, folder):
  try:
    hours = int(hours)
    minutes = int(minutes)
    if 0 <= hours < 24:
      if 0 <= minutes < 60:
        open(folder + "/" + author, 'w').write(str(hours) + " " + str(minutes))
        return "Set " + str(hours) +":"+ str(minutes) + " for " + author
    else:
      return "Invalid time"
  except ValueError:
    return "Invalid time"

