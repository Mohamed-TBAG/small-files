from telebot import types
import telebot,requests,time

token = input('Token Bot : ')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
	if message.chat.type =='private':
		chatt = message.chat.id
		n = types.InlineKeyboardMarkup(row_width=1)
		bu1 = types.InlineKeyboardButton(text='Download Video .', callback_data='video')
		bu2 = types.InlineKeyboardButton(text='Download Music .', callback_data='music')
		bu3 = types.InlineKeyboardButton(text='Developer .', url='https://t.me/DRR44')
		bu4 = types.InlineKeyboardButton(text='Channel Developer .', url='https://t.me/BXX55')
		n.add(bu1,bu2,bu3,bu4)
		first_name = message.from_user.first_name
		bot.send_message(chatt, f'''
**
User : [{first_name}](tg://settings)
Hey, You In The Bot Download ( Video , Music ) 
**''', parse_mode='Markdown', reply_to_message_id=message.message_id, reply_markup=n)
	else:
		bot.reply_to(message,'<strong>- لا يمكنك استخدام البوت في المجموعات \n- You can use the bot in groups</strong>', parse_mode='html', reply_to_message_id=message.message_id)

@bot.callback_query_handler(func=lambda call:True)
def qwere(call):
	global link
	if call.data =='video':
		aa = bot.send_message(call.message.chat.id, 'Send Link .')
		bot.register_next_step_handler(aa,video)
	if call.data =='music':
		aa = bot.send_message(call.message.chat.id, 'Send Link .')
		bot.register_next_step_handler(aa,audio)
def video(message):
	chat_id = message.chat.id
	link = message.text
	headers = {
		'authority': 'lovetik.com',
		'accept': '*/*',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'origin': 'https://lovetik.com',
		'referer': 'https://lovetik.com/',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'sec-gpc': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest',
	}
	data = {
		'query': link}
	print(link)
	result = requests.post('https://lovetik.com/api/ajax/search', headers=headers, data=data).json()
	print(result)
	video = result['links'][3]['a']
	desc = result['desc']
	bot.send_video(chat_id, video=video, caption=desc)
	time.sleep(5)
def audio(message):
	chat_id = message.chat.id
	link = message.text
	headers = {
		'authority': 'lovetik.com',
		'accept': '*/*',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'origin': 'https://lovetik.com',
		'referer': 'https://lovetik.com/',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'sec-gpc': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest',
	}

	data = {
		'query': link}
	print(link)
	result = requests.post('https://lovetik.com/api/ajax/search', headers=headers, data=data).json()
	print(result)
	audio = result['links'][4]['a']
	desc = result['desc']
	bot.send_audio(chat_id, audio=audio, caption=desc)
bot.infinity_polling()