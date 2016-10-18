#!/usr/bin/python
# -*- coding: utf-8 -*-
from base64 import b64decode
from base64 import b64encode

def decode(text):
  return b64decode(text)

def encode(text):
  return b64encode(text)

def s2h(text):
  answer = ""
  for i in text:
    answer += i.encode("hex")
  return answer

def s2a(text):
  answer = ""
  for i in text:
    answer += str(ord(i))
  return answer

def h2s(text):
  answer = ""
  for i in range(0, len(text), 2):
    answer += str(chr(int(text[i]+text[i+1], 16)))
  return answer
