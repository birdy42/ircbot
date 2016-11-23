#!/usr/bin/python
# -*- coding: utf8 -*-
import sys
import socket
import string
import multiprocessing

import time
from lib import bullshit
from lib import getimg
from lib import leet
from lib import quotes
from lib import roulette
from lib import rule
from lib import botserv
from lib import utils

#----------CONFIG---------------------------------------------------------
HOST='irc.root-me.org'
PORT=6667
NICK='BirdyBot'
IDENT='BirdyBot'
REALNAME='BirdyBot'
CHANNELINIT='#BFF'
#-------------------------------------------------------------------------

def nm_to_n(nickmask):
  return nickmask.split("!")[0][1:]

class MyBot():
  s = ''
  admin = 'birdy4'
  isVote = 0
  isLeet = 0
  # Starting, Running, Players, currentPlayer, lastText, loser
  rouletteState = [0,0,[],0, '', ''] 
  voteTopic = ""
  topicYes = 0
  topicNo = 0
  
  def __init__(self):
    self.s = self.connect()
    quotes.startRandomQt(self)
    self.botserv()

  def connect(self):
    s=socket.socket( )
    s.connect((HOST, PORT))
    s.send('NICK '+NICK+'\n\r')
    s.send('USER '+IDENT+' '+HOST+' hackerzvoice '+REALNAME+'\n\r') 
    while 1:
      line=s.recv(4096)
      print line
      if 'Welcome' in line:
        s.send('JOIN '+CHANNELINIT+'\n\r')
        s.send('PRIVMSG NickServ identify david\n\r')
        return s

  def send(self, msg):
    self.s.send(msg)
  
  def msg(self, target, message):
    self.send('PRIVMSG ' + target + ' ' + message + '\n\r')

  def botserv(self):
    print "starting botserv..."
    s = self.s
    try:

      while 1:
        rBuffer = ''
        c = 100000
        while c != "\n":
          c = s.recv(1)
          rBuffer += c
  
        line = rBuffer[:-1] # Remove \n
        if line != "":
          self.log(line)

        line=line.rstrip() # Remove \r
        line=line.split(" ")

        if(line[0]=='PING'):
          s.send('PONG '+line[1]+'\n\r')
        else:
          if 'PRIVMSG' in line:
            self.parsemsg(nm_to_n(line[0]), line[2], line[3:])
    except socket.timeout:
      s.close()
      exit(0)

  def parsemsg(self, author, replyto, msg):
    message = " ".join(msg)[1:]
    self.log(message)
    self = botserv.serv(self, author, replyto, message)

  def log(self, msg):
    fs = open("data.log", 'a')
    fs.write(msg+"\n")
    fs.close()

# ---------"MAIN"-----------
def worker(bot):
  bot.botserv()

def reader(s):
  data = input("Send data:")
  s.send('PRIVMSG '+CHANNELINIT+' '+data)
  reader(s)

if __name__ == "__main__":
  print "Starting bot..."
  bot = MyBot()


