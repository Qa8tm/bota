import time

from core import (bot, app, WEBHOOK_URL_BASE, WEBHOOK_URL_PATH)
import telebot
import requests
from time import sleep
import random
import re

# Telegram Bot Code 

hassan = "5300465323:AAE0HaxL1tQacRzqUHn0l1UlWTrllKOdTLw"
bot = telebot.TeleBot(hassan)
sudo = 5359109940
def id_ls(id):
    result = False
    file = open("ids.txt", 'r')
    for line in file:
        if line.strip()==id:
            result = True
    file.close()
    return result

def id_ls_pr(id):
    result = False
    file = open("private.txt", 'r')
    for line in file:
        if line.strip()==id:
            result = True
    file.close()
    return result

def id_ls_gr(id):
    result = False
    file = open("groups.txt", 'r')
    for line in file:
        if line.strip()==id:
            result = True
    file.close()
    return result

def id_ls_ca(id):
    result = False
    file = open("channels.txt", 'r')
    for line in file:
        if line.strip()==id:
            result = True
    file.close()
    return result

@bot.message_handler(commands=['start'])
def o(message):
	use = message.from_user.username
	ID = message.from_user.id
	ph = "https://pin.it/1mCHKyc"
	bot.send_photo(message.chat.id,ph, f"""
مرحبًا @{use}
• اهلاً بك في بوت اذكار،
•قم بأضافة البوت الى قروبك، قناتك وسيقوم البوت بنشر الاذكار
• ارسل تفعيل بوت الاجر ليتم تفعيل البوت،
ثبت الاجرُ ان شاء الله ❤️
المطور ~ @K_8_U""")
@bot.message_handler(func=lambda m: True)
def d(message):
    if message.text == "send" and message.chat.id == sudo:
        r = random.randint(0, 336)
        g = requests.get("https://raw.githubusercontent.com/osamayy/azkar-db/master/azkar.json").json()
        what = "\n".join(re.findall("'category': '(.*?)', '", str(g))).splitlines()[int(r)]
        base = "\n".join(re.findall(", 'description': '(.*?)', '", str(g))).splitlines()[int(r)]
        fromm = "\n".join(re.findall("'reference': '(.*?)', '", str(g))).splitlines()[int(r)]  # 'reference': '
        what_is = "\n".join(re.findall("'zekr': '(.*?)}, {'category': '", str(g))).splitlines()[int(r)]
        done = f"{what}\n{base}\n{fromm}\n{what_is}"
        done_send = 0
        private = open("private.txt", "r").read().splitlines()
        groups = open("groups.txt", "r").read().splitlines()
        of_all = private + groups
        for one in of_all:
            try:
                if one.count("-"):
                    bot.send_message(f"{one}", done)
                else:
                    bot.send_message(one,done)
                done_send += 1
            except:
                pass
        bot.send_message(message.chat.id, f"- تم الارسال الى {done_send} عضو وشخص ومجموعة وقناة .")
    if message.text == "الاحصائيات" and message.chat.id == sudo:
        private  = open("private.txt","r",encoding="utf-8").read().splitlines()
        groups = open("groups.txt","r",encoding="utf-8").read().splitlines()
        of_all = private + groups 
        al = f"""
- الاحصائيات :
- المجموعات :{len(groups)} .
- الخاص :{len(private)} .
- الكل :{len(of_all)} .
"""
        bot.reply_to(message,al)
    name = message.from_user.first_name
    msg = message.text
    #####
    ####
    if msg ==  "تفعيل" and message.chat.type == "private":
        try:
            idu = message.from_user.id
            us = str(message.chat.first_name)
            f3 = open("private.txt", 'a')
            if (not id_ls_pr(str(idu))):
                f3.write("{}\n".format(idu))
                f3.close()
                bot.reply_to(message,f"- اهلا عزيزي {name} تم تفعيل بوت الاجر بنجاح .")
            else:
                bot.reply_to(message,f"- البوت مفعل من قبل ! .")
        except Exception as err:
            bot.reply_to(message,f"- حصل خطأ !\nرمز الخطأ :\n{err}")
    if msg ==  "تفعيل بوت الاجر" and message.chat.type == "supergroup" or message.chat.type == "group":
        try:
            idu = message.chat.id
            us = str(message.chat.first_name)
            f3 = open("groups.txt", 'a')
            if (not id_ls_gr(str(idu))):
                f3.write("{}\n".format(idu))
                f3.close()
                bot.reply_to(message,f"- اهلا عزيزي {name} تم تفعيل بوت الاجر بنجاح .")
            else:
                bot.reply_to(message,f"- البوت مفعل من قبل ! .")
        except Exception as err:
            bot.reply_to(message,f"- حصل خطأ !\nرمز الخطأ :\n{err}")

@bot.channel_post_handler(func=lambda m: True)
def f(message):
    msg = message.text
    if msg == "تفعيل":
        try:
            idu = message.chat.id
            us = str(message.chat.first_name)
            f = open("channels.txt", 'a')
            if (not id_ls_ca(str(idu))):
                f.write(f"{idu}\n")
                f.close()
                bot.reply_to(message, f"- اهلا عزيزي  تم تفعيل بوت الاجر بنجاح .")
            else:
                bot.reply_to(message, f"- البوت مفعل من قبل ! .")
        except Exception as err:
            bot.reply_to(message, f"- حصل خطأ !\nرمز الخطأ :\n{err}")
            
bot.infinity_polling(True)
# Remove webhook
bot.remove_webhook()

time.sleep(0.1)

# Set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)

if __name__ == "__main__":
    app.run(host=WEBHOOK_URL_BASE)
