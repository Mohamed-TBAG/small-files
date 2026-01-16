import telebot,random,requests
from telebot import types
from user_agent import generate_user_agent
bot = telebot.TeleBot('6050561096:AAHnLn9PYcRobnOyhJBd88chu5zspAI9oII')
@bot.message_handler(commands=['start'])
def start(message):
	fe = types.InlineKeyboardMarkup(row_width=2)
	dirt = types.InlineKeyboardButton(text='بدأ الصيد ،',callback_data='bda')
	fe.add(dirt)
	name = message.from_user.first_name
	id = message.from_user.id
	dmj = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
	bot.reply_to(message,f'اهلاً عزيزي {dmj} في شيكر يوزرات تام تام ،\nلبدأ الصيد اضغط على زر بدأ الصيد لأختيار اقسام الصيد ،',parse_mode='markdown',reply_markup=fe)
@bot.callback_query_handler(func=lambda call:True)
def nkk(call):
	data = call.data
	if data =='bda':
		bot.delete_message(call.message.chat.id, call.message.message_id)
		qsm = types.InlineKeyboardMarkup(row_width=2)
		shb = types.InlineKeyboardButton(text='شبه ثلاثي ،',callback_data='s3')
		sb = types.InlineKeyboardButton(text='شبه ثلاثي شخطه ،',callback_data='s33')
		rb4 = types.InlineKeyboardButton(text='رباعي ،',callback_data='s4')
		kmasi = types.InlineKeyboardButton(text='خماسي مكرر',callback_data='s5')
		sd = types.InlineKeyboardButton(text='سداسي مكرر ،',callback_data='s6')
		sb = types.InlineKeyboardButton(text='سباعي مكرر ،',callback_data='s7')
		thman = types.InlineKeyboardButton(text='ثماني مكرر ،',callback_data='s8')
		qsm.add(shb,sb,rb4,sd,sb,thman)
		bot.send_message(call.message.chat.id,'اختار عزيزي من القائمة ،',reply_markup=qsm)
	mn = call.data
	if mn =='s4':
		bot.delete_message(call.message.chat.id, call.message.message_id)
		ch = 'qwertyuioplkjhgfdsazxcvbnm1234567890_-.'
		ch1= 'qwertyuioplkjhgfdsazxcvbnm_.-'
		while True:
				a = random.choice(ch1)
				b = random.choice(ch)
				c = random.choice(ch)
				d = random.choice(ch)
				e = random.choice(ch)
				uer = f'{a}{b}{e}{d}'
				u = requests.get(f'https://User-tam.romiomatheo.repl.co/?user={uer}').text
				if 'متاح' in u:
					mj = f'[{call.message.from_user.first_name}](tg://user?id={call.message.from_user.id})'
				bot.send_message(call.message.chat.id,f'تم صيد يوزر جديد ✓ ،\nاليوزر : {uer} ،\n@devSmJa / @itmason ,')
		else:
			bot.send_message(call.message.chat.id,'غير متاح')	
	if mn =='s3':
					bot.delete_message(call.message.chat.id, call.message.message_id)
					ch = 'qwertyuioplkjhgfdsazxcvbnm1234567890_-.'
					ch1= 'qwertyuioplkjhgfdsazxcvbnm_.-'
					while True:
						a = random.choice(ch1)
						b = random.choice(ch)
						c = random.choice(ch)
						d = random.choice(ch)
						e = random.choice(ch)
						uer = f'{a}_{b}_{e}'
						u = requests.get(f'https://User-tam.romiomatheo.repl.co/?user={uer}').text
						if 'متاح' in u:
							mj = f'[{call.message.from_user.first_name}](tg://user?id={call.message.from_user.id})'
							bot.send_message(call.message.chat.id,f'تم صيد يوزر جديد ✓ ،\nاليوزر : {uer} ،\n@devSmJa / @itmason ,')		
						else:
							bot.send_message(call.message.chat.id,'غير متاح')	
								
	if mn =='s5':
					bot.delete_message(call.message.chat.id, call.message.message_id)
					ch = 'qqwweerrttyyuuiiooppllkkjjhhggffddssaazzxxccvvbbnnmm1234567890'
					ch1= 'qqwweerrttyyuuiiooppllkkjjhhggffddssaazzxxccvvbbnnmm'
					while True:
						a = random.choice(ch1)
						b = random.choice(ch)
						c = random.choice(ch)
						d = random.choice(ch)
						e = random.choice(ch)
						uer = f'{b}{e}{e}{b}{e}'
						u = requests.get(f'https://User-tam.romiomatheo.repl.co/?user={uer}').text
						if 'متاح' in u:
							mj = f'[{call.message.from_user.first_name}](tg://user?id={call.message.from_user.id})'
							bot.send_message(call.message.chat.id,f'تم صيد يوزر جديد ✓ ،\nاليوزر : {uer} ،\n@devSmJa / @itmason ,')		
						else:
							bot.send_message(call.message.chat.id,'غير متاح')	
								
bot.infinity_polling()