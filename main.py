import requests , telebot
from telebot import types

bot = "5792319780:AAEjmtpDtFQu-IjOb1-gDRXOArlZIKBoWxk"
bot = telebot.TeleBot(bot)

sh_btn = types.InlineKeyboardButton(text='تحميل', callback_data='s1')

@bot.message_handler(commands=["start"])
def start(message):
    
    b = types.InlineKeyboardMarkup()
    b.row_width = 2
    b.add(sh_btn)
    
    bot.send_message(message.chat.id,f"""
    *مرحبا بك {message.from_user.first_name} في بوت تحميل من تيك توك يحمل فيديو وصوت 💿*""",parse_mode='markdown',reply_markup=b)

@bot.callback_query_handler(func=lambda call: True)
def sh(call):
  if call.data=='s1':
   bot.send_message(call.message.chat.id,'- ارسل الرابط!')
   @bot.message_handler(func=lambda m: True)
   def Url(message):
    bot.send_message(message.chat.id,"<strong>جاري التحميل انتظر قليلا ...</strong>",parse_mode="html")
    msg = message.text
    try:
     url = request = get(f"https://www.tikwm.com/api/?url={url}").json()
     a = url["video"]["videoURL"]
     b = url['audioURL']
     
     bot.send_video(message.chat.id,a,caption='تم تحميل بواسطة @T_4IJ')
     bot.send_voice(message.chat.id,b,caption='تم تحميل بواسطة @T_4IJ')
    
    
    except:
     bot.send_message(message.chat.id,"تأكد من الرابط..!")
  
print('run')
bot.infinity_polling()
