import requests
import os
import telebot
token = input(" << Enter Token telegram >> : ")
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"Hello\n Wellcome To Instagram Downloader Bot : video and Reels and photo  and Tv :  \nSend Link  Now 📎✅ \nCH  : @")
@bot.message_handler(func=lambda m:True)
def send(message):
    bot.send_message(message.chat.id,f"Wait Please",parse_mode="html") 
    url = requests.get(f"https://mr-abood.herokuapp.com/Get/Video/Insta?Link={message.text}").json()
    io = url["link"]
    bot.send_video(message.chat.id,io,caption="Done ✅")
bot.polling()
