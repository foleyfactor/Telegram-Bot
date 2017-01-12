from twx.botapi import TelegramBot, ReplyKeyboardMarkup, TelegramBotRPCRequest, InputFile, InputFileInfo
import random
import time

"""
Setup the bot
"""

memepaths = ["baby.jpg", "baby2.jpg", "baby3.jpg", "baby4.jpg", "baby5.jpg", "baby6.png", "bern.jpg", "bern2.jpg", "bern3.png", "brian.jpg", "brian2.jpg", "brian3.jpg", "brian4.jpg", "cat.jpg", "cat2.jpg", "cat3.jpg", "cat4.jpg", "cat5.gif", "daniel.jpg", "doge.png", "doge2.jpg", "doge3.jpg", "duck.jpg", "duck2.jpg", "feels.jpg", "feels2.png", "foo.png", "guy.jpg", "guy2.jpg", "haters.jpg", "news.jpg", "news2.jpg", "overly_attached.jpg", "pepe4.jpg", "sanic.png", "sanic2.png", "sanic3.png", "sky.jpg", "spoderman.jpg", "spoderman2.gif", "spoderman3.gif"]

bot = TelegramBot('182831736:AAFQiQ-5J-9sKPenhduBdONH7Dhw13dr76Q')
bot.update_bot_info().wait()
print(bot.username)

"""
Send a message to a user
"""
started = []

"""
Get updates sent to the bot
"""
offset = 682276492
lastSpam = []

found_memes = False

def sendCena():
	fp = open("JohnCena.mp3", 'rb')
	file_info = InputFileInfo("inconspicuousAudioFile.mp3", fp, 'audio/mpeg')
	bot.send_audio(chat_id=chat_id, audio=InputFile('audio', file_info))

def sendMeme():
	path = random.choice(memepaths)
	fp = open(path, 'rb')
	file_info = InputFileInfo(path, fp, 'image/png')
	bot.send_photo(chat_id=chat_id, photo=InputFile('photo', file_info))

def sendAllMemes(chat_id):
	for i in memepaths:
		path = i
		fp = open(path, 'rb')
		file_info = InputFileInfo(path, fp, 'image/png')
		bot.send_photo(chat_id=chat_id, photo=InputFile('photo', file_info))

def checkForDev(msg):
	msg = msg.lower()
	danger = False
	if "liberals" in msg:
		danger = True
	elif "dev" in msg and "views" in msg:
		danger = True
	return danger

def checkLastSpam(chat_id):
	global lastSpam, started
	t = time.time()
	l = started.index(chat_id)
	if t - lastSpam[l] >= 600:
		lastSpam[l] = t
		return True
	return False

while True:
	updates = bot.get_updates(limit=20, offset=offset).wait()

	for update in updates:
		offset = update.update_id
		msg = update.message.text
		chat_id = update.message.chat.id
		print(msg)
		if msg == "/start":
			if not (chat_id in started):
				started.append(chat_id)
				lastSpam.append(0)
				bot.send_message(chat_id, 'Hello! My name is $weggybot v1.1. I am a telegram bot created by Alex Foley. Nice to meet you! Type /info for my commands.').wait()
				print("I have been started in chat " + str(chat_id))
		if chat_id in started:
			if msg == "/memes":
				print("dank")
				sendMeme()
			elif msg == "/cena":
				print("ITS JOHHHHN CENA!")
				sendCena()
			elif msg == "/info":
				bot.send_message(chat_id, 'My current features are as follows:\nType /memes for a dank meme to appear.\nType /cena for a pleasant surprise.\nType /xkcd for a random comic.\nType /spam if you\'re feeling devious.\nType /credits for my credits.').wait()
			elif msg == "/credits":
				bot.send_message(chat_id, 'I was written by Alex Foley using the twx.botapi library for Python. The dank meme selection was aided by his sister who downloaded memes while he typed code into his computer like a nerd. Andrew Seto and Laura Harvey deserve credit for the suggestions that they gave me that I implemented.').wait()
			elif msg == "/quit":
				bot.send_message(chat_id, 'No one can stop me now, tonight I\'m on the loose!').wait()
			elif msg == "/xkcd":
				bot.send_message(chat_id, 'http://xkcd.com/' + str(random.randint(1,1650)) + "/").wait()
			elif checkForDev(msg):
				bot.send_message(chat_id, 'Tread lightly...').wait()
			elif msg == "/spam":
				if checkLastSpam(chat_id):
					for i in range(10):
						bot.send_message(chat_id, 'Never gonna give you up, never gonna let you down').wait()
						bot.send_message(chat_id, 'Never gonna run around and desert you').wait()
						bot.send_message(chat_id, 'Never gonna make you cry, never gonna say goodbye').wait()
						bot.send_message(chat_id, 'Never gonna tell a lie and hurt you').wait()
				else:
					bot.send_message(chat_id, 'To prevent the spamming of the /spam command, I have a cool-down before spam can be sent again. Please try again later.').wait()
			elif msg == "/quit_all":
				if update.message.sender.id == 199460414:
					print("aww okay.")
					bot.send_message(chat_id, 'Master has given $weggybot a sock! $weggybot is a free meme now!').wait()
					found_memes = True
				else:
					bot.send_message(chat_id, 'Only master can tell the bot to completely stop. You\'re not master!').wait()

		

	offset += 1

	if found_memes:
		updates = bot.get_updates(limit=1, offset=offset).wait()
		break