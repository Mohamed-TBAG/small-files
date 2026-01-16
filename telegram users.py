import requests
import telebot
import random

token = "5919961394:AAHYg96LTWO-bxQ8l95_ajc6fYRFWvRKbjE"

bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['greet','start'])
def start(message):
 zix = f'''
 • مرحبأ اهلين نورت بوت المبرمج زيد 
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
للتواصل مع مبرمح البوت  @P_W_7 هناا
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
'''
 bot.send_message(message.chat.id, f"{zix}")
 bot.send_message(message.chat.id, f"""
• بوت صيد معرفات تلكرام مجأني ✅
 ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
• اختار نوع المعرف من الاتي🖋 
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
 • ارسل رقم 5 لصيد خماسي مميز
• ارسل رقم 6 لصيد سداسي مميز
 ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
 المبرمج : @P_W_7 """)
 @bot.message_handler(func=lambda followinG:True )

 def re(message):
  zood =(message.text)
  if zood > '6':
    rr='Bad Namber'
    bot.send_message(message.chat.id, f"{rr}")
    exit()
  elif zood < '5':
    ss='Bad Namber'
    bot.send_message(message.chat.id, f"{ss}")
    exit()
    
  fe = '''
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
بدأ الصيد بنجاح انتضر الصيد ✅
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
ـ @P_W_7 // @P_W_77 
'''
  bot.send_message(message.chat.id, f"{fe}")
  while True:
   zz = int(zood)
   zaid24 = 'qwert_yuiop_asdfghjklzxc_vbnm123_4567890'
   user = ("".join(random.choice(zaid24)for i in range(zz)))
   ii = requests.get(f'https://t.me/{user}').text
   if 'robots' and 'nofollow' and 'noindex' in ii:
    reg = f'''
✅ Available Telegram
•-•
• User ﴾ @{user} ﴿
•-•
🔎 @P_W_7 : @P_W_77
'''
    bot.send_message(message.chat.id, f"{reg}")
        #Soon
   else:
    zzodo = ii
   
bot.polling(none_stop=True)