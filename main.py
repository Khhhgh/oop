import requests,time,re
from time import sleep
import telebot
from telebot import types
import os
from uuid import uuid4 as uid
from secrets import token_hex
from OneClick import *
import requests
from uuid import uuid4 as uid
from secrets import token_hex
from OneClick import *
import requests
import telebot
from telebot import types
import instaloader
import HamodyTools
from HamodyTools import *
import os
from uuid import uuid4
import json
import requests
from requests import get
from dragonxxdlib import *
import telebot,pyshorteners
from user_agent import generate_user_agent
import requests
from bs4 import BeautifulSoup
import re
import json
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
    channel = "" # Your channel username without @
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
      b = types.InlineKeyboardButton(text = "programmer 🇮🇶",url=f"t.me/T_4IJ")
      aa.add(b)
      bot.send_message(message.chat.id,f"""*💌Welcome to the bot💌* [{a}](tg://user?id={id})*
اهلا \t بك في بوت التحميل من التيك توك 

🌿❤️ لبدأ \t التحميل اضغط \n /TIKTOK*
""",parse_mode='markdown',reply_markup=aa,reply_to_message_id=message.message_id)
@bot.message_handler(commands = ["instagram"])
def Start(message):
 global ti
 m = message.text
 mm = message.chat.id
 Name = message.chat.first_name
 User = message.from_user.username 
 ID = message.chat.id
 bot.reply_to(message, """  
*- اهلا بك في بوت انستقرام ( {} )                             
• بـوت معلومات انستا\nريست انستا\nاستخراج سيشن ايدي انستجرام\nفحص ايميل انستا\nفحص يوزر انستا •
- USERNAME : [ @{} ]                                    
- ID : [ *`{}`* ] 
- Telegram : [ @hope521 ]                                       *
""".format(Name,User,ID) , parse_mode = "markdown" , reply_markup = A)
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
	if call.data=="n1":
		n1(call.message)
	if call.data=="n2":
		n2(call.message)
	if call.data=="n3":
		n3(call.message)
	if call.data=="n4":
		n4(call.message)
	if call.data=="n5":
		n5(call.message)	
A = types.InlineKeyboardMarkup(row_width=2)
B = types.InlineKeyboardButton(text ="ᴿᴬᴳᴺᴬᴿ" , url = "https://t.me/PPGBB")
CH = types.InlineKeyboardButton(text ="Channel" , url = "https://t.me/PYTHON_PG")
D = types.InlineKeyboardButton(f"- معلومات انستا .",callback_data='n1')
F = types.InlineKeyboardButton(f"الحصول علئ سيشن انستا .",callback_data='n2')
G = types.InlineKeyboardButton(f"ارسال ريست انستا .",callback_data='n3')
H = types.InlineKeyboardButton(f"فحص يوزر انستا .",callback_data='n4')
J = types.InlineKeyboardButton(f"فحص متاح انستا .",callback_data='n5')
A.add(B,CH,D,F,G,H,J)		
def n1(message):
    mj=bot.send_message(message.chat.id,"""  
* -  اهلا بك في بوت معلومات حساب انستجرام\n- ارسـل الـيـوزر . 
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
    bot.register_next_step_handler(mj,agvc)
def agvc(message):
	global us,ti
	us = message.text
	api = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={us}'
	head = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar',
f'cookie': 'mid=YwTJcAAEAAFcZMrQPSTepvHIl6wf; ig_did=E8C65BEE-FF49-420B-BCA5-3EB87DB30A83; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'x-asbd-id': '198387',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
	}
	g = requests.get(api,headers=head).json()
	if g['status']=='ok':
		ti+=1
		print(f'{ti} - Good')
		pc = str(g['data']["user"]["profile_pic_url"])
		nAEGOS = str(g['data']['user']['full_name'])
		bAEGOS = str(g['data']['user']['biography'])
		pAEGOS = str(g['data']['user']['edge_owner_to_timeline_media']['count'])
		fsAEGOS = str(g['data']['user']['edge_followed_by']['count'])
		fgAEGOS = str(g['data']['user']['edge_follow']['count'])
		iAEGOS = str(g['data']['user']['id'])
		re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iAEGOS}").json()
		dAEGOS = re['date']
		bot.send_photo(message.chat.id,pc,caption=f'Name : {nAEGOS} \nPio : {bAEGOS} \nPosts : {pAEGOS} \nFollowers : {fsAEGOS} \nFollowing : {fgAEGOS} \nID : {iAEGOS} \nDate : {dAEGOS} \nBY : @hope521  -  @hope521',parse_mode="html")
	else:
		bot.send_message(message.chat.id,'Error .')
def n2(message):
    hj=bot.send_message(message.chat.id,"""  
* -  - اهلا بك عزيزي في بوت اضهار سيزن ايدي انستا\n———————×———————\nارسل حسابك الانستا الوهمي بهاذه الشكل ⬇️\n\n  *`username:password`*\nاو بهاذه الشكل\n  vvll_l:iioopp . 
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
    bot.register_next_step_handler(hj,ses)
def ses(message):
   global usre,psse,ti
   try:    
    usre = message.text.split(':')[0]
    psse = message.text.split(':')[1]
    print(usre,psse)
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "385",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "csrftoken=Lk9Lfwj0Hp0T3zCBYwjoeGBUBjU1sVXC; mid=YSuaiwAEAAEzvEB8maY7IzJ6MDzJ; ig_did=07753880-8B96-4C09-93E9-BA39B801DD08",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/accounts/login/",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "x-asbd-id": "437806",
        "x-csrftoken": "Lk9Lfwj0Hp0T3zCBYwjoeGBUBjU1sVXC",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "0",
        "x-instagram-ajax": "56f3c2d2a823",
        "x-requested-with": "XMLHttpRequest"
    }
    data = {
        "username": f"{usre}",
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:1613414957:{psse}",
        "queryParams": "{}",
        "optIntoOneTap": "false"
    }

    req_login = requests.post(url, headers=headers, data=data)
    if '"authenticated":true' in req_login.text:
    	bot.send_message(message.chat.id,"Done Login ✔️")
    	sess = req_login.cookies['sessionid']
    	bot.reply_to(message,text=f""" 	
USER = {usre}    	
PASS = {psse}
    	
#Sessionid سيزن ايدي    	

{sess}

━━━━━━━━⧪━━━━━━━━
By :- @hope521 - @hope521
""")
    elif '"message":"checkpoint_required"' in req_login.text:
    	bot.reply_to(message,text='هاذه الحساب سكيور 😵') 
    elif '"authenticated":false' in req_login.text:
    	bot.send_message(message.chat.id,"خطا في اليوزر او الباسورد ❌")
   except:
   	bot.reply_to(message,text="عذرا لايوجد هكذا زر ارجو اعادة المحاولة بشكل صحيح ⚠️")
def n3(message):
    hj=bot.send_message(message.chat.id,"""  
* -  اهلا بك عزيزي في بوت ارسال الريست
ارســل الــيوزر لعمل ريست
- مع اضهار الريست الخاص بالحساب مشفر
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
    bot.register_next_step_handler(hj,restins)
def restins(message):
   global msg,ti
   msg = message.text
   ggg = instaloader.Instaloader()
   profile = instaloader.Profile.from_username(ggg.context, msg)
   iddd = (profile.userid)
   try:
   	check = Hamody.Reset(message.text)
   	headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',

        'Accept-Language': 'en-US',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': 'AQ==',
							}
   	data = {
        'ig_sig_key_version': '4',
        "user_id":iddd
							}
   	res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers, data=data).json()
   	rs =str(res['obfuscated_email'])
   	if check==True:
   		bot.send_message(message.chat.id,f"تم توصيل الريست [ {message.text} ] ✅\nRest : {rs}")
   		print("•  تم توصيل الريست •")
   	else:
   		bot.send_message(message.chat.id,f"الريست خطا او الحساب سكيور [ {message.text} ] ❌")
   		print("\033[1;31m• ريست خطا •")
   except:
   	bot.reply_to(message,text="ارسل اليوزر بشكل صحيح رجاً ♻️-او-خطا 🚫") 
def n4(message):
    hj=bot.send_message(message.chat.id,"""  
* -  اهلا بك عزيزي في بوت فحص اليوزر متاح او غير متاح
- ارســل اليـوزر للفحص هل هو متاح ام لا
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
    bot.register_next_step_handler(hj,userins)
def userins(message):
		global user,ti
		user = message.text
		url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',headers ={'Host':'www.instagram.com',
'content-length':'85',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'0',
'sec-ch-ua-mobile':'?0',
'x-instagram-ajax':'81f3a3c9dfe2',
'content-type':'application/x-www-form-urlencoded',
'accept':'*/*',
'x-requested-with':'XMLHttpRequest',
'x-asbd-id':'198387',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'sec-ch-ua-platform':'"Linux"',
'origin':'https://www.instagram.com',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.instagram.com/accounts/emailsignup/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-IQ,en;q=0.9',
'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
'cookie':'ig_nrcb=1'},data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false')
		if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
			print('ERIR')		
		elif  '"errors": {"username":' in url.text or  '"code": "username_is_taken"' in url.text:
			bot.send_message(message.chat.id,f"اليوزر غير متاح [ {user} ] ❌")
		else:
			bot.send_message(message.chat.id,f"""
اليوزر متاح ✔️
☆━━━━━━━━━━━━━━☆

✇ 𝑼𝑺𝑬𝑹 ☛ `{user}`

☆━━━━━━━━━━━━━━☆""",parse_mode = "markdown")
def n5(message):
    hj=bot.send_message(message.chat.id,"""  
* -  اهلا بك عزيزي في بوت فحص ايميل الانستا متاح او لا
- ارسل اليوزر لفحص المتاح

ملاحضة -: ارسل يوزر وليس ايميل البوت يعمل اليوزر ايميل من خلاله. 
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
    bot.register_next_step_handler(hj,instg)
def instg(message):
	global email,ti
	email = message.text
	url = 'https://b.i.instagram.com/api/v1/accounts/login/'
	headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
	uid = str(uuid4())
	data = {
			'uuid':uid, 
			'password':'ffffdddddaaa666', 
			'username':'{}' .format(email),
			'device_id':uid, 
			'from_reg':'false', 
			'_csrftoken':'missing', 
			'login_attempt_countn':'0'
			}
	re = requests.post(url,headers=headers,data=data).text
	if ('"invalid_user"')in re:
		bot.send_message(message.chat.id,f"الايميل غير متاح في الانستا [ {email} ] ❌")
	elif ('"bad_password"') in re:
		bot.send_message(message.chat.id,f"الايميل متاح في الانستا [ {email} ] ✔️") 
@bot.message_handler(commands = ["download"])
def donload(message):
 m = message.text
 mm = message.chat.id
 Name = message.chat.first_name
 User = message.from_user.username 
 ID = message.chat.id
 bot.reply_to(message, """  
*- اهلا بك في بوت التحميلات ( {} )                             
• 
تحميل تيك توك /tiktok
تحميل انستجرام /insta
تحميل فيسبوك /facebook
تحميل يوتيوب /YouTube
تحميل بينترست /pinterest
•
- USERNAME : [ @{} ]                                    
- ID : [ *`{}`* ]
- Py : [@hope521]                                        *
""".format(Name,User,ID) , parse_mode = "markdown")
@bot.message_handler(commands = ["TIKTOK"])
def s1(message):
    mj=bot.send_message(message.chat.id,"""  
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
		bot.send_video(message.chat.id,video,caption="- تم تحميل الفيديو\nرابط بوت التحميل : @T_4IJ . ")
	except:
		bot.send_message(message.chat.id,f"-  الرابط غير صالح ❌ . ")
@bot.message_handler(commands = ["YouTube"])
def s2(message):
    mg=bot.send_message(message.chat.id,"""  
* -  بوت تحميل من اليوتيوب . 
- لتحميل فديو ارسل رابط المنشور 
- التحميل بدون علامة مائية او اي حقوق اخرى. 
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
    bot.register_next_step_handler(mg,sg)
def sg(message):
	global url,ti
	url = message.text
	try:
		rr = youtube(url)
		bot.send_video(message.chat.id,rr,caption="- تم تحميل الفيديو\nرابط بوت التحميل : @hope521 . ")
	except:
		bot.send_message(message.chat.id,f"-  الرابط غير صالح ❌ . ")
@bot.message_handler(commands = ["facebook"])		
def s3(message):
    mk=bot.send_message(message.chat.id,"""  
* -  بوت تحميل من الفيس بوك . 
- لتحميل فديو ارسل رابط المنشور 
- التحميل بدون علامة مائية او اي حقوق اخرى. 
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
    bot.register_next_step_handler(mk,sl)
def sl(message):
	global url,ti
	url = message.text
	try:
		rr = facebook(url)
		bot.send_video(message.chat.id,rr,caption="- تم تحميل الفيديو\nرابط بوت التحميل : @hope521 . ")
	except:
		bot.send_message(message.chat.id,f"-  الرابط غير صالح ❌ . ")
@bot.message_handler(commands = ["insta"])
def s4(message):
    mp=bot.send_message(message.chat.id,"""  
* -  بوت تحميل من الانستجرام . 
- لتحميل فديو ارسل رابط المنشور 
- التحميل بدون علامة مائية او اي حقوق اخرى. 
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
    bot.register_next_step_handler(mp,sogvx)
def sogvx(message):
    global ulrg,tm,ti
    tm = str(time.time()).split('.')[0]
    ulrg = message.text
    url = f"https://api.sssgram.com/st-tik/ins/dl?url={ulrg}&timestamp={tm}" 
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://www.sssgram.com',
        'referer': 'https://www.sssgram.com/',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    } 
    data = {
        'url': ulrg,
        'timestamp': tm,
    }
    r1 = requests.get(url,headers=headers,data=data).json()
    rr = r1['result']['insBos'][0]['url']
    bot.send_video(message.chat.id,rr,caption="- تم تحميل الفيديو\nرابط بوت التحميل : @hope521 . ")
@bot.message_handler(commands = ["pinterest"])  
def s5(message):
    mw=bot.send_message(message.chat.id,"""  
* -  بوت تحميل من البنترست . 
- لتحميل صورة ارسل فقط الاسم/مثال : كريستيانو 
- التحميل بجودة عالية جداً الجوده 4k. 
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
    bot.register_next_step_handler(mw,sv)
def sv(message):
    global query,ti
    query = message.text
    url = 'https://www.pinterest.com/resource/BaseSearchResource/get/?source_url=/search/my_pins/?q=avengers&rs=rs&eq=naruto%208K&etslf=15092&term_meta[]=avengers%7Crecentsearch%7C4&data={"options":{"article":null,"applied_filters":null,"appliedProductFilters":null,"auto_correction_disabled":false,"corpus":null,"customized_rerank_type":null,"filters":null,"query":"'+query+'","query_pin_sigs":null,"redux_normalize_feed":true,"rs":"direct_navigation","scope":"pins","source_id":null,"no_fetch_context_on_resource":false},"context":{}}&_=1662617352806'

    headers = {
        'accept': 'application/json, text/javascript, */*, q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en,ar;q=0.9,en-US;q=0.8',
        'cache-control': 'no-cache',
        'cookie': 'csrftoken=0e018d7a846bbb9b8fa7832662c63ed2; _b="AWbcYA0FqcRO6pt4TXz6L96G+/bXeigv/QK5RoON+UKFoKfeyCZZ/IQx+Ka7R9tJhOc="; g_state={"i_l":0}; _auth=1; _pinterest_sess=TWc9PSZoUjNlM2o4dlk2Nis0K3M5bThOOWlzcVVZQ2xKK0grQVhScjU0Vk14M0dYTEswUUMrako1YmNiYk8xaStHSHpnQ2Ezbzc1Rlg1TkZqZkM3djVqRkg2VEg3MTNGZEd4UURRZHc2Njlpam5BdmxFV1hhaW9LNzJ2TWpLdkg3K3krTDJzYXhqbndWeXltYUh5NzVQNEF0M2NQZTc4dVl5RkhDNlFkbGNBa1F0cU0rSEpHclY0dDJHRGdrRWdRdkpoeXhBK3lmMkp3MHh2Z3NJZzVkVm1WTDdJd2ZsQTB3YWI4N2h3c3hnU2tiWU9zYW5sQUJxWFBiSElyRGZTY3hWd2MrZURnSk9idnZ2cFhoUmtTTlRjWGhxTHhNVE9EaTVSQ1FMM2toQmRIYjdCSmVDSklJSFNlMVVycjJ6STdXbnNBaG5nL0xRUFVZYmhxZEtMOUJTKzNqTE9zK1ZYTDNHeEpzOWxXTmpVWkRXRHg4SDUyVkZIZEtxMzZBVnVBZjd2czBKSHp1K0QyV21rOEt3OG03MUdYcVFIVTEvci9VRW9jblplSHE2TGFQZVgrKzlvS2JJK2pRcis1S1JHbU9IYUtYSkVJaENaT05pZXNvd2krMUxNeDVkYnhtK3N0cEMwMzRlMSsrZXVQUEpZdTJtSXZsTTBxWGs1ZmtqYnBUcmJJMlEwSW55ak1mWXVtclV5bzhtTEhadGtLV21LbkVqdzFKelBZWmVlZWE4eGRVNjQ4NFNablRDUTJnb3F0ZTVkWWx1UHdjOXVJWGtwRWtsSit2dHpkMmVzeUxEOHFzdzdmS3NKVnFITDJwUjlDYnRMWWJSeURtQWZ5MloxV1c0WEp4RkQ3SWRKTm1Bc0ZYMDdUR0pubkRXUVpKRS8xNmxQNWNvYUpSb3dtNHlWencvWncrS2hkOXFBNlNsTW5Ha1lpVkdhZ2dMQmhsOUxGN2s4cmdwQUpDRmV5ODVDb0sreWtnNzdhdjZUWjBnLzJ4MlJjdXVHOVI2ZXovUm1KTTQwVmFTREJTUkVvWUF3WEx0QnhwWEtEU2NxSmpXZjNWREcxTWpTb0MrOCtiOW1JbFEvOUlUUFJCNTc4SzJkSTByOG5ieW94UWZ0OWVFR3RPUmpWRGZ2NFRYNTYzRGd5RVlZK1o3UkhVTG5xVUZ5cVlzakl6a2U0Vks1YmQ5SUpkckgvVTlTY2tqblVIU3dmUnRTdkhtL2F6SnFWUnVsMkVwZGRyUlQ5Rk9CMlNzb2VieFYxTDc2UU8vcnBZcjFMR1h5aFV2VFRSRlFrbGppczNYYVh4NXAwcG54TUx3TnpiczZhQTJOMHMxdzgyVitFPSZtUTFDTnV5UTdrNit6R0Q5VDJyS0dXZGN3R0k9; _routing_id="2446e1bc-a370-4e3c-8e3c-ec9ec536d20f"; sessionFunnelEventLogged=1; cm_sub=none',
        'pragma': 'no-cache',
        'referer': 'https://www.pinterest.com/',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-app-version': 'a332b16',
        'x-pinterest-appstate': 'active',
        'x-pinterest-experimenthash': 'c519017d978aab61a2dc39b3ed657696bcb130c2aa27632777fcafe1dcae2bce503172a4f5554e6bf64bdce07f29915629f8bc0c126647930a83f3fe6f8d8795',
        'x-pinterest-pws-handler': 'www/search/[scope].js',
        'x-pinterest-source-url': '/search/pins/?q=avengers&rs=typed&term_meta[]=avengers%7Ctyped',
        'x-requested-with': 'XMLHttpRequest',
    }
    try:
        req = requests.get(url, headers=headers)
        mr = 0
        while True:
            mr += 1
            q = req.json()['resource_response']['data']['results'][mr]['images']['orig']['url']
            bot.send_photo(message.chat.id, q,caption=f'تم تحميل الصورة \nرقم الصورة {mr}\nبوت التحميل : @hope521 . ')    
    except Exception as s:
        pass    

@bot.message_handler(commands = ["usersp"])
def num_users(message):
 if message.from_user.id == sudo:
  file = open("users.txt","r")
  len_num = len(file.readlines())
  bot.send_message(message.chat.id,text="all users : {}".format(len_num))
 else:
  bot.send_message(message.chat.id,text="you are not my developer")
     
   #اذاعه 
   #message for all users from devloper or from bot admin
@bot.message_handler(commands=["all"])
def all_u(message):
 try:
  if message.from_user.id == sudo:
   idu = message.from_user.id
   t = message.text.replace("/all" ,"")
   f = open("users.txt","r")
   for idu in f:
    bot.send_message(idu , text="{}".format(t))
  else:
   bot.send_message(message.chat.id, text= " you'r not my developer (: ")
 except:
  bot.send_message(message.chat.id,text="Error")

###########################
 
@bot.message_handler(commands=["urldownload"])
def send_welcome(message):
    bot.reply_to(message,'مرحبا في بوت انشاء رابط تحميل مباشر للوسائط ول ملفات ارسل (فيديو, مقطع صوتي , صوره , ملف)')
@bot.message_handler(content_types=['photo', 'video', 'audio', 'document'])
def file_sent(message):
    try:
        bot.send_message(message.chat.id,"تم صنع الرابط\nالرابط ⬇️")
        bot.send_message(message.chat.id, short(bot.get_file_url(message.document.file_id)))
        
    except AttributeError:
        try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.photo[0].file_id)))
        except AttributeError:
            try:
                bot.send_message(message.chat.id, short(bot.get_file_url(message.audio.file_id)))
            except AttributeError:
                try:
                    bot.send_message(message.chat.id, short(bot.get_file_url(message.video.file_id)))
                except AttributeError:
                    pass
@bot.message_handler(commands=["urlcd"])
def vg(message):
	hj=bot.send_message(message.chat.id,"""  
* -  بوت انشاء رابط مختصر يفيد جماعة الاندكس
ارســل الـرابــط .
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
	bot.register_next_step_handler(hj,shoturl)
def shoturl(message):
	global link
	link = message.text
	url = 'https://is.gd/create.php'
	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
		'cache-control': 'no-cache',
		'content-length': '43',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://is.gd',
		'pragma': 'no-cache',
		'referer': 'https://is.gd/',
		'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': "Windows",
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': generate_user_agent() ,
}
	data = {
		'url': f'{link}',
		'shorturl': '',
		'opt': '0',
	
}
	req = requests.post(url,headers=headers,data=data)
	newurl = re.findall('id="short_url" value="(.*?)"',req.text)[0]
	bot.send_message(message.chat.id,f'''<strong>تم صنع الرابط ✅
- الرابط : {newurl}
- @hope521</strong>''',parse_mode='html')
@bot.message_handler(commands = ["zakrafa"])
def nj(message):
	hj=bot.send_message(message.chat.id,"""  
* - 🏖️  أهلاً بك في بوت زخرفة النصوص 
ارسل الكلمة المراد زخرفتها
يدعم زخرفة — انكليزي – عربي.
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
	bot.register_next_step_handler(hj,zakrf)
def zakrf(message):
	ssz = message.text
	url = f'https://dev-ooooo2oo.pantheonsite.io/z.php?text={ssz}'
	req = requests.get(url).json()["results"]
	for i in req:
		bot.send_message(message.chat.id,f"`{i}`",parse_mode = "markdown")

@bot.message_handler(commands=["infoTiktok"])
def no(message):
	hj=bot.send_message(message.chat.id,"""  
* - اهلا بك في بوت معلومات تيك توك
ارسـل اليـوزر .
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
	bot.register_next_step_handler(hj,szxd)
def szxd(message):
	user=(message.text)
	url=f'https://api.dlyar-dev.tk/info-tiktok.json?user={user}'
	try:
		req=requests.get(url).json()
		id=req['id']
		name=req['name']
		fol=req['followers']
		fols=req['following']
		uid=req['uid']
		likes=req['likes']
		ima=req['img']
		country = req["country"]
		flag = req["flag"]
		ya=(f'Name : {name}\nUser : {user}\nFollowers : {fol}\nFollowing : {fols}\nuid : {uid}\nLikes : {likes}\nID : {id}\nCountry : {country}\nFlag : {flag}\nBY : @hope521  -  @hope521')
			
		bot.send_photo(message.chat.id,ima,ya)
	except:
		bot.send_message(message.chat.id,'Eror .')
@bot.message_handler(commands=["infotwitter"])
def no(message):
	hj=bot.send_message(message.chat.id,"""  
* - اهلا بك في بوت معلومات تويتر
ارسـل اليـوزر .
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
	bot.register_next_step_handler(hj,twsx)
def twsx(message):
	iip = (message.text)
	user_agent = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'Referer' : 'https://twitter.com/sw.js' }
	url = "https://twitter.com/home?precache=1"
	r_token = requests.get(url, headers=user_agent)
	soup = BeautifulSoup(r_token.text, "html.parser") 
	token = re.findall(r'"gt=\d{19}', str(soup.find_all('script')[-1]), re.IGNORECASE)[0].replace("\"gt=","")
	url8 = f"https://mobile.twitter.com/i/api/graphql/gr8Lk09afdgWo7NvzP89iQ/UserByScreenName?variables=%7B%22screen_name%22%3A%22{iip}%22%2C%22withSafetyModeUserFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%7D"
	head8 = {
"x-csrf-token":"192e8d70a4b47525f760b6ab4d7179c7","User-Agent":"Mozilla\/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/14.0.3 Mobile\/15E148 Safari\/604.1","Accept-Encoding":"gzip, deflate, br","x-guest-token":token,"Cookie":"missing","Accept-Language":"en-us","x-twitter-active-user":"yes","Accept":"*\/*","Connection":"keep-alive","Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA","Content-Type":"application\/json","x-twitter-client-language":"en","Host":"mobile.twitter.com"
}
	rr =requests.get(url8,headers=head8).json()
	try:
		ag1 = rr["data"]["user"]["result"]["legacy"]["name"]
	except KeyError:
		ag1 = 'Not name'
	try:
		ag2 = rr["data"]["user"]["result"]["rest_id"]
	except KeyError:
		ag2 = "not id"
	try:
		ag3 = rr["data"]["user"]["result"]["legacy"]["followers_count"]
	except KeyError:
		ag3 = '0'
	try:
		ag4 =rr["data"]["user"]["result"]["legacy"]["friends_count"]
	except KeyError:
		ag4='0'
	try:
		ag11 = rr["data"]["user"]["result"]["legacy"]["created_at"]
	except KeyError:
		ag11 = 'Not Date'
	try:
		ag12 = f'Username - {iip}\nName  - {ag1}\nID - {ag2}\nFollowers - {ag3}\nFollowing - {ag4}\nDate - {ag11}'
		bot.send_message(message.chat.id,ag12)
	except:
		bot.send_message(message.chat.id,'Eror .')			

@bot.message_handler(commands=["infoCard"])
def hko(message):
	hj=bot.send_message(message.chat.id,"""  
* - اهلا بك في بوت معلومات الفيزا
ارسـل الكارد الان  .
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
	bot.register_next_step_handler(hj,visc)
def visc(message):
	card = message.text
	num= card.split('|')[0]
	mo= card.split('|')[1]
	ye= card.split('|')[2]
	cvc= card.split('|')[3]
	url=f'https://api.dlyar-dev.tk/info-bin?bin={num}{mo}{ye}{cvc}'
	req=requests.get(url).json()
	a1=req["status"]
	a2=req["bin"]
	a3=req["scheme"]
	a4=req["type"]
	a5=req["brand"]
	a6=req["bank"]
	a7=req["ccode"]
	a8=req["country"]
	a9=req["currency"]
	a10=req["flag"]
	a11=req["phone"]
	try:
		sfccod = (f"""
`status -> {a1}`
*Bin -> *`{a2}`
*Scheme ->* `{a3}`
*Type -> *`{a4}`
*Brand ->* {a5}
*Code ->* `{a6}`
*Bank ->* `{a7}`
*Country ->* `{a8}`
*Currency ->* {a9}
*Flag ->* {a10}
*Phone ->* `{a11}`

*Crde —> [ {card} ]*
""")
		bot.send_message(message.chat.id,sfccod,parse_mode = "markdown")
	except:
		bot.send_message(message.chat.id,'Eror .')
@bot.message_handler(commands=["infoBin"])
def hko(message):
	hj=bot.send_message(message.chat.id,"""  
* - اهلا بك في بوت معلومات الـBin
ارسـل الـBin الان  .
--------------------------------------
@hope521 - @hope521                                          *
""",parse_mode = "markdown")
	bot.register_next_step_handler(hj,binsuv)
def binsuv(message):
	Bin = message.text
	url=f'https://api.dlyar-dev.tk/info-bin?bin=Bin'
	req=requests.get(url).json()
	a1=req["status"]
	a2=req["bin"]
	a3=req["scheme"]
	a4=req["type"]
	a5=req["brand"]
	a6=req["bank"]
	a7=req["ccode"]
	a8=req["country"]
	a9=req["currency"]
	a10=req["flag"]
	a11=req["phone"]
	try:
		sfccod = (f"""
`status -> {a1}`
*Bin -> *`{a2}`
*Scheme ->* `{a3}`
*Type -> *`{a4}`
*Brand ->* {a5}
*Code ->* `{a6}`
*Bank ->* `{a7}`
*Country ->* `{a8}`
*Currency ->* {a9}
*Flag ->* {a10}
*Phone ->* `{a11}`

*Crde —> [ {Bin} ]*
""")
		bot.send_message(message.chat.id,sfccod,parse_mode = "markdown")
	except:
		bot.send_message(message.chat.id,'Eror .')		
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
	       print(e)
	       sleep(10)   
