import requests , time  ,os,sys,json,pyfiglet
log = pyfiglet.figlet_format("Tik tok \n info")
s = """
عربي -1
2- English
"""
lo = ('\033[93m'+log +'\033[96m'+ '\n'+s)
print(lo)
ad = input("Enter your choice | اكتب اختيارك : ")
if ad =='1':
	os.system('clear')
	time.sleep(1)
	print(log)
	a = input(" : اكتب يوزر الحساب   ")
	b = input(' : اكتب ايدي حساب التليكرام ')
	url = f"https://tufaah.osc-fr1.scalingo.io/tiktok/?user={a}"
	c = input(" : اكتب توكن بوت التليكرام  ")
	print('انتضر شوي ')
	time.sleep(2)
	os.system("clear")
	req = requests.get(url)
	res = req.json()
	name =res['name']
	bio =res['bio']
	fs= res['followers']
	fg = res['following']
	id = res['id']
	img = res['image']
	info =f"""
	hi bro this the info :
		---------------------------
		اليوزر : {a}
		الايدي : {id}
		الاسم :  {name}
		يتابعونه : {fs}
		يتابع :  {fg}
		بايو : {bio}
		صوره : {img}
		---------------------------
	"""
	print('\033[95mتم ارسال المعلومات لبوت التليكرام ')
	requests.post(f'https://api.telegram.org/bot{c}/sendMessage?chat_id={b}&text= all info  {info}')
if ad=='2':
	print(log)
	a = input("enter user : ")
	b = input("your telegram id : ")
	url = f"https://tufaah.osc-fr1.scalingo.io/tiktok/?user={a}"
	c =input("Enter your token bot : ")
	print('\033[95m please white ')
	time.sleep(2)
	os.system('clear')
	req = requests.get(url)
	res = req.json()
	name =res['name']
	bio =res['bio']
	fs= res['followers']
	fg = res['following']
	id = res['id']
	img = res['image']
	info =f"""
	hi bro this the info :
		---------------------------
		user : {a}
		id : {id}
		name : {name}
		followers : {followers}
		folowing : {following}
		bio : {bio}
		img url : {img}
		---------------------------
	"""
	print('\033[95mDon Send to telegram bot' )
	requests.post(f'https://api.telegram.org/bot{c}/sendMessage?chat_id={b}&text= all info  {info}')