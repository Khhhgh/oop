import telebot
import requests
from telebot import types
requests.urllib3.disable_warnings()
sudo = 1310488710 #خلي ايدي حسابك التلي 

def id_file1(id):
 all = False
 file = open("users.txt","r")
 for line in file:
  if line.strip() ==id:
   all = True
 file.close()
 return all
 
ti=0
users = []
token = "6477545499:AAFurq6jQ1J5BuYeV3xdEdKSwnIU3HsZUzE"
print('- اذهب للبوت واضغط \n /start')
bot = telebot.TeleBot(token) 
def short(url):
    return pyshorteners.Shortener().tinyurl.short(url)


@bot.message_handler(commands = ["start"])
def start(message):
   id = message.from_user.id
   with open('users.txt','a') as f3:
    f3.write(f'{id}\n')
    channel = "mane5u" # Your channel username without @
    a = message.from_user.first_name
    b = message.from_user.username
    if message.chat.type == "private":
      if not id in users:
        users.append(id)
        stats = len(users)
        bot.send_message(sudo,"""-» قام شخص جديد بالدخول الى البوت الخاص بك 
- -» اسمه : {}
-» معرفه : @{}
-» ايديه : {}
➖ أصبح عدد مستخدمين البوت : ~ {}""".format(a,b,id,stats),disable_web_page_preview=True)
      x = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{channel}&user_id={id}").text
      if x.count("left") or x.count("Bad Request: user not found"):
      	z = types.InlineKeyboardMarkup()
      	x = types.InlineKeyboardButton(text = "➕ channel ",url=f"t.me/{channel}")
      	z.add(x)
      	return bot.send_message(message.chat.id,f'''<strong>- ⌔︙عليك الاشتراك في قناة البوت لأستخدام الاوامر
-» اشترك في القناة @{channel} .
-» ثم ارسل /start ✅ </strong>''',reply_markup=z,parse_mode='html')
      aa = types.InlineKeyboardMarkup()
      sh_btn = types.InlineKeyboardButton(text='تحميل', callback_data='s1')
      aa.add(sh_btn)
      bot.send_message(message.chat.id,f"""*💌Welcome to the bot* [{a}](tg://user?id={id})*
اهلا بك في بوت التحميل من التيك توك 

🌿❤️ لبدأ التحميل اضغط تحميل⬇️*
""",parse_mode='markdown',reply_markup=aa,reply_to_message_id=message.message_id)
@bot.callback_query_handler(func=lambda call: True)
def sh(call):
  if call.data=='s1':
    mj=bot.send_message(call.message.chat.id,"""  
* -  بوت تحميل من التيك توك . 
- لتحميل فديو وصور ارسل رابط المنشور 
- التحميل بدون علامة مائية او اي حقوق اخرى. 
--------------------------------------
@T_4IJ - @T_4IJ                                          *
""",parse_mode = "markdown")
    bot.register_next_step_handler(mj,ag)
def ag(message):
	global us,ti
	url = message.text
	try:
		request = get(f"https://www.tikwm.com/api/?url={url}").json()
		video = request["data"]["play"]
		bot.send_video(message.chat.id,video,caption="- تم تحميل الفيديو\nرابط بوت التحميل : @hope521 . ")
	except:
		bot.send_message(message.chat.id,f"-  الرابط غير صالح ❌ . ")
bot.polling(True)
