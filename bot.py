import time
import random
import datetime
import telepot
import cricket_api

"""
After **inserting token** in the source code, run it:
```
$ python2.7 diceyclock.py
```
[Here is a tutorial](http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/)
teaching you how to setup a bot on Raspberry Pi. This simple bot does nothing
but accepts two commands:
- `/roll` - reply with a random integer between 1 and 6, like rolling a dice.
- `/time` - reply with the current time, like a clock.
"""

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    #help(handle)

    print 'Got command: %s' % command
    #print msg['text']
    #print(str(msg))

    if command == 'roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == 'time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == 'score':
    	bot.sendMessage(chat_id, "Hang on! Fetching scores...")
    	scores = cricket_api.get_scores()
    	print scores
    	for score in scores:
    		bot.sendMessage(chat_id, str(score))
    elif command == ('Hi' or 'hi') :
        bot.sendMessage(chat_id,"Hello " + msg['chat']['first_name'])
    else:
    	bot.sendMessage(chat_id, "I'm not smart enough to understand what you said :(")

bot = telepot.Bot('133284745:AAHPwZvfFZpac_g7mQ2CPOB8UlUh5KoGBgA')
bot.message_loop(handle)
print 'I am listening ...'

while 1:
	time.sleep(10)
