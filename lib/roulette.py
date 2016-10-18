#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint

#!roulette
def roulette(State, author):
  Starting, Running, Players, currentPlayer, lastText, loser = State
  loser = ''
  lastText = ''
  if Running or Starting:
    lastText = "Wait for the roulette game to stop."
    return Starting, Running, Players, currentPlayer, lastText, loser
  else:
    lastText = author + " is starting a roulette... !join to join"
    Starting = 1
    Players = [author]
  return Starting, Running, Players, currentPlayer, lastText, loser

#!join
def join(State, author):
  Starting, Running, Players, currentPlayer, lastText, loser = State
  lastText = ''
  if Starting:
    if author not in Players:
      Players.append(author)
    if len(Players) >= 2:
      lastText = "You can now use !start"
  return Starting, Running, Players, currentPlayer, lastText, loser

#!start
def start(State, author):
  Starting, Running, Players, currentPlayer, lastText, loser = State
  lastText = ''
  if len(Players) >= 2 and (author == Players[0]):
    Starting = 0
    Running = 1
    currentPlayer = randint(0,len(Players)-1)
    lastText = "Next player is: "+ Players[currentPlayer] +" !pull to pull trigger"
  return Starting, Running, Players, currentPlayer, lastText, loser


#!pull
def pull(State, author):
  Starting, Running, Players, currentPlayer, lastText, loser = State
  lastText = ''
  if Running:
    if author == Players[currentPlayer]:
      if randint(0,6) == 4:
        loser = author
        allrolls = open("roulette/roulette.txt").read()
        rolls = allrolls.split("\n")[:-1]
        newrolls = ""
        for roll in rolls:
          auth = roll.split(" ")
          if author == auth[0]:
            newrolls = newrolls + auth[0] + " " + str(int(auth[1])+1) +" " + str(int(auth[2])+1) + "\n"
            lastText = "PAN " + Players[currentPlayer] + " dies. " + str(int(auth[1])+1) +" death in " + str(int(auth[2])+1) +" participations"
          elif auth[0] in Players:
            newrolls = newrolls + auth[0] + " " + auth[1] + " " + str(int(auth[2])+1) + "\n"
          else:
            newrolls = newrolls + auth[0] + " " + auth[1] + " " + auth[2] + "\n"

        open("roulette/roulette.txt", 'w').write(newrolls)
        Players = []
        Running = 0
      else:
        currentPlayer = (currentPlayer + 1) % (len(Players))
        lastText = "Next player is: "+ Players[currentPlayer] +" !pull to pull trigger"
  return Starting, Running, Players, currentPlayer, lastText, loser

def stats():
  allrolls = open("roulette/roulette.txt").read()
  rolls = allrolls.split("\n")[:-1]
  stats = ""
  for roll in rolls:
    auth = roll.split(" ")
    stats = stats + " " +auth[0]+ " "+auth[1]+"/"+auth[2]
  return stats

def kill(State, text, author):
  Starting, Running, Players, currentPlayer, lastText = State
  lastText = ''
  if len(Players) > 2:
    if author in Players:
      if text in Players:
        Players.remove(text)
        currentPlayer = (currentPlayer) % (len(Players))
        lastText = text + " was removed from roulette game. Next player is: "+ Players[currentPlayer]
  return Starting, Running, Players, currentPlayer, lastText, loser
