#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from random import randint
from lib import bullshit
from lib import getimg
from lib import leet
from lib import quotes
from lib import roulette
from lib import rule
from lib import remain
from lib import utils
from lib import bitly
from lib import meme
from lib import ctfs
from lib import ctftime

def serv(bot, author, replyto, message):
  try:
    if randint(0,999) == 1:
      bot.msg(replyto, "bite")
    if message[0] == "!":
      command = message.split(" ")[0] # !command text
      text = " ".join(message.split(" ")[1:])
      args = text.split(" ") # !command args[0] args[1]...

      # Keep a trace of people using my bot
      bot.log( message + " from " + author)
      if command == '!pokemon': # Yorin
        bot.msg(replyto, "https://www.youtube.com/watch?v=q3p_dbcMBHg")
      elif command == '!ctflist': # ghozt
        my_str =""
        for i in ctftime.get_ctf():
          my_str += i + ";"
        bot.msg(my_str)
      elif command == '!daniela': # ghozt
        bot.msg(replyto, "https://www.youtube.com/watch?v=tpgXbli1dDk")
      elif command == '!bitoduc': # ghozt
        bot.msg(replyto, bullshit.getBitoduc())
      elif command == '!doku': # Dazax
        bot.msg(replyto, "http://wikisecu.fr/doku.php")
      elif command == '!meme': # Dazax
        bot.msg(replyto, meme.show(args[0]))
      elif command == '!rndmeme': # Dazax
        bot.msg(replyto, meme.random())
      elif command == '!addmeme': # Dazax
        meme.add(args[0], args[1])
      elif command == '!b64d' or command == '!base64decode': # ghozt & Yorin
        bot.msg(replyto, utils.decode(text))
      elif command == '!b64e': # ghozt & Yorin
        bot.msg(replyto, utils.encode(text))
      elif command == '!bitly': # Dazax
        bot.msg("#BFF", bitly.get(text) + " by "+author)
      elif command == '!h2s': # ghozt & Yorin
        bot.msg(replyto, utils.h2s(text))
      elif command == '!s2h': # ghozt & Yorin
        bot.msg(replyto, utils.s2h(text))
      elif command == '!setra': # ghozt
        bot.msg(replyto, remain.setR(args[0], args[1], author, "remaina"))
      elif command == '!setrm': # ghozt
        bot.msg(replyto, remain.setR(args[0], args[1], author, "remainm"))
      elif command == '!getrm': # ghozt
        bot.msg(replyto, remain.get(args[0], author, "remainm"))
      elif command == '!getra': # ghozt
        bot.msg(replyto, remain.get(args[0], author, "remaina"))
      elif command == '!github': # birdy4
        bot.msg(replyto, "http://github.com/birdy42/ircbot")
      elif command == '!whee': # Yorin
        bot.msg(replyto, "https://www.youtube.com/watch?v=-Q7wUbtT9gk")
      elif command == '!reload': # ghozt
        reload(rule)
        reload(leet)
        reload(roulette)
        reload(getimg)
        reload(bitly)
        reload(meme)
        reload(bullshit)
        reload(quotes)
        reload(remain)
        reload(utils)
        reload(ctfs)
        reload(ctftime)
        bot.msg(replyto, "Reloaded")
      elif command == '!asv': # Yorin
        bot.msg(replyto, " 2 semaines, Bot, Botville. Alors, tentée par mon énorme epenis jeune demoiselle ?")
      elif command == '!dazaxcuse': # ghozt
        bot.msg(replyto, "jpeux pas il fait trop chaud")
      elif command == '!boo': # ghozt / Yorin
        if text == '':
          bot.msg(replyto, "https://www.youtube.com/watch?v=xxsfpQOFf1Q")
        else:
          bot.msg(replyto, "boo " + text + " boo ... boo " + text + " Testaburger boo, boo "+text+" liar")
      elif command == '!hymne': # Yorin
        bot.msg(replyto, "Yorin's hymne: https://www.youtube.com/watch?v=4oUxPWnrXNk")
      elif command == '!devexcuse': # ghozt
        bot.msg(replyto, bullshit.getDevScuse())
      elif command == '!beer': # ghozt / Dazax
        beer = bullshit.getBeer()
        if args[0] == '':
          bot.msg(replyto, author + " offre une tournée de " + beer)
        else:
          to = " a "
          to = to + args[0]
          bot.msg(replyto, author + " offre une " + beer + to)
      elif command == '!votetopic':
        if bot.isVote == 0:
          bot.isVote = 1
          bot.voteTopic = text
          bot.msg(replyto, "!vote yes/no to vote for this topic")
        else:
          bot.msg(replyto, "Vote "+ bot.voteTopic +" still running")
      elif command == '!votestop':
        if bot.isVote == 1:
          bot.msg(replyto, "Result for "+bot.voteTopic+": " + str(bot.topicYes) + " - " + str(bot.topicNo))
          bot.isVote = 0
          bot.topicYes = 0
          bot.topicNo = 0
      elif command == '!vote':
        if bot.isVote == 1:
          if args[0] == 'yes':
            bot.topicYes = bot.topicYes + 1
          elif args[0] == 'no':
            bot.topicNo = bot.topicNo + 1
      elif command == '!roulette':
        bot.rouletteState = roulette.roulette(bot.rouletteState, author)
        bot.msg(replyto, bot.rouletteState[4])
      elif command == '!join':
        bot.rouletteState = roulette.join(bot.rouletteState, author)
        bot.msg(replyto, bot.rouletteState[4])
      elif command == '!start':
        bot.rouletteState = roulette.start(bot.rouletteState, author)
        bot.msg(replyto, bot.rouletteState[4])
      elif command == '!pull':
        bot.rouletteState = roulette.pull(bot.rouletteState, author)
        bot.msg(replyto, bot.rouletteState[4])
        if bot.rouletteState[5] != '':
          bot.msg(replyto, bot.rouletteState[5]+ ": You lose! Get OUT!")
          bot.rouletteState = [0,0,[],'','','']
      elif command == '!roulettestats':
        bot.msg(replyto, roulette.stats())
      elif command == '!kill':
        bot.rouletteState = roulette.kill(bot.rouletteState, args[0], author)
        bot.msg(replyto, bot.rouletteState[4])
      elif command == '!addctf':
        ctfs.add(text, author)
      elif command == '!ctf':
        bot.msg(replyto, ctfs.show(text, author))
      elif command == '!ctfsearch':
        bot.msg(replyto, ctfs.search(text, author))
      elif command == '!addquote':
        quotes.add(text, author)
      elif command == '!show':
        bot.msg(replyto, quotes.show(text, author))
      elif command == '!random':
        bot.msg(replyto, quotes.random(text, author))
      elif command == '!quotesearch':
        bot.msg(replyto, quotes.search(text, author))
      elif command == '!quotefrom':
        bot.msg(replyto, quotes.qfrom(args[0], author))
      elif command == '!echo':
        bot.msg(replyto, text)
      elif command == '!help':
        bot.msg(replyto, "!addquote !show !random !echo !getimg !leet !help !propose !setleet !rule !roulette")
      elif command == '!propose':
        open("todolist", 'a').write(text+ "\n")
      elif command == '!setleet':
        bot.isLeet = 1 if text == 'on' else 0
      elif command == '!leet':
        bot.msg(replyto, leet.leet(text))
      elif command == '!rule':
        bot.msg(replyto, rule.getRule(text))
      elif command == '!getimg':
        bot.msg(replyto, getimg.getImg(text))
      elif command == '!say':
        if author == bot.admin:
          if len(args) > 1:
            bot.msg(args[0], " ".join(args[1:]))
      else:
        #bot.msg(replyto, "Invalid command. Type !help for help")
        bot.log( "invalid command" + command)
  except:
    bot.log( "Error " + str(sys.exc_info()[0]))
    bot.msg(replyto, "te fooouuut paaas d'ma gueule")
  return bot
