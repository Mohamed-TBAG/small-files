from requests import *
from random import *
from user_agent import *
from os import system
import datetime
import requests
from time import *
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
j = '\033[2;35m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
E = '\033[1;31m'
class alaa:
		def LOGIN():
			user = input(f"{Z}({F}•{Z}) {B}ENTER USERNAME YOU'R {Z}ACCOUNT {B}: {Z}")
			pas = input(f"{Z}({F}•{Z}){B} ENTER PASSWORd YOU'R {Z}ACCOUNT {B}: {Z}")
			h = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','content-length': '385','content-type': 'application/x-www-form-urlencoded','cookie': 'mid=YiNDbwALAAHloyK8S59Xs3XDLabd; ig_did=9FACA874-80BE-45PrWcWBvSAXGj8bD2EAcwLJEf6Bkfw9Y1EknVsZCggqiNixWMwTX9HNJQ24FVfuLa4t8eXt1HPA1iUitADJLCoS5ua3WQR\0542128710131\0541682210436:01f7ae827a1dfd2afd29d87081c4b6fcfcd7d69ac63489b22b379109f617f21e3ab951f3"; shbts="1650674436\0542128710131\0541682210436:01f706ba04ce9a92a6957907ede1c5b5cf6da47433d1a5eacfa10f47cf26e8a89db1079b"; csrftoken=3Iz5CjmeHnmFWnSvtGSwOkF42GLMngNX; fbsr_124024574287414=sNIow6DXyx1ZYhd6J16RNaJNWd7mscEsZvlkyJqA2oU.eyJ1c2VyX2lkIjoiMTAwMDExMDI5MTQ2MjgwIiwiY29kZSI6IkFRRHRuX0liU001Z0FhX3RNV1hMZG1DMkdNQXU0cW1oVGl3UnNmVFJjSE9BSmxWZWFZdWlWNEQxT0pXZlY1OTJLTUhnMXBzcTZmTS1IWjlxcC1xalZTellLOEt5X3VFUkNaUWx2THFxN0pmSG1nbnJwbXV6b1pNRzZLVUlaMEU5Y0plU0NTdXA3Y1FiT1lQdTN2SnhoaXE4VU1ZaE1mWXhCb2NqdXkyZ0N1cktMRVNiYUQ3OU5GeFFjajY2MG1LeGxvQkpzY3YtekVpNjR6YVF3dzZtZ3Nhbjg4WVhlWlFZWjhPblNTSHB6OThFR25uZlJVanJhNVE2cVRHZ3hoUWdJMENmWWpZTXRSVDVhOXhoTFhCVFNoOXJsV1VmRXBPX1ZOTC1NM1NPM1RlOU9kRTlGN091aVVSQVc0UkFRWGt3emoybjlGRkg2UTZ3OG93OVJrZ1hEUTBPIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUpicmtyOHM0SnQ3OE9FelZjNnVEZ2Z6WkNudlVxNzIzaDZLVElLcVpDVXdmaUJydlk3Zlc1VzdmdTNvZGFuMFFJZGIzaWNBYlRKeHAyYjFXZWNRakdPeGZCODdCaVlza0tCMlpCU3dLWFVWb1MxaW4wWkFHelM0WkFMRGk2OUw3WFBjcnVCY3RaQ1pDUGdzSXlPT2xaQlpBd1h4bkIwV252ZlpCNUdpNkFodkYxIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NTEwMDk5NDl9','dnt': '1','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/''sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36','x-asbd-id': '198387','x-csrftoken': '3Iz5CjmeHnmFWnSvtGSwOkF42GLMngNX','x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-instagram-ajax': '20e2a5e214f4','x-requested-with': 'XMLHttpRequest'}
			try:
				Login_IG = post("https://www.instagram.com/accounts/login/ajax/",headers=h,data = {'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+pas,'username':user,'queryParams': '{}','optIntoOneTap': False,'stopDeletionNonce': "",'trustedDeviceRecords': '{}'})
				if "userId" in Login_IG.text:
					print(F+f"DONE LOGIN IN ACCOUNT {X}!")
					sis = Login_IG.cookies.get_dict()['sessionid']
					coo = Login_IG.cookies.get_dict()
					csrf = Login_IG.cookies.get_dict()['csrftoken']
					cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"
					sleep(2)
					system('clear')
					start(sis,cookie,csrf)
				elif 'challenge' in Login_IG.text:
					print(B+f"YOUR ACCOUNT IS {X}SECURE !")
				elif '"ip_block"' in Login_IG.text:
					print(X+f'YOUR IP IS {Z}BLOCKED !')
					sleep(2)
					system('clear')
				else:
					print(Z+f"USERNAME OR PASSWORD IS {Z}ERROR !")
					sleep(2)
					system('clear')
					alaa.LOGIN()
			except requests.exceptions.ConnectionError:
				print(A+"YOUR NET IS SO BAD !")
				sleep(2)
				system('clear')
				alaa.LOGIN()
		def Follow(sis,id,uss):
		    had = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': f'ig_did=3228C28C-878C-4032-B1BA-805CA7DCDE80; mid=YCMNFgALAAGTkjQS4zQTJ887fFG5; ig_nrcb=1; csrftoken=vudL37NP1XL22tCTKXluvvZCwm7kI2Yp; ds_user_id=46015777379; sessionid={sis}; rur=RVA','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36','x-csrftoken': 'vudL37NP1XL22tCTKXluvvZCwm7kI2Yp','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR2Ba9nmJROdSoghzs45qrHKC88BhLBeE0C1g5XLvznnHW1d','x-instagram-ajax': '0edc1000e5e7','x-requested-with': 'XMLHttpRequest'}
		    follo = post(f'https://www.instagram.com/web/friendships/{id}/follow/',headers=had)
		    US = uss.upper()
		    if follo.status_code == 200:
		    	print(B+f"- DONE FOLLOWING => {F}{US}")
		    elif follo.status_code == 400:
		    	print(Z+"- YOUR ACCOUNT CAN'T FOLLOWING USERS {B}=> {Z}{US} !")
		    else:
		    	print(X+"DON'T FOLLOWING !")
		def Get_Id(sis):
			User = input(B+f"USERNAME TO GET {Z}FOLLOWING {B}THEM {Z}:- {X}")
			print(C+"-"*50)
			hea = {'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'cookie':f'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; datr=H9vzYq35j3WCu3W5Jw-BuqMb; dpr=1.75; csrftoken=BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT; ds_user_id=10851247180; shbid="2195,10851247180,1693733333:01f781e1606e53e58d1108b28b348650b4413de9e963e2af156f7f8349ac2dcc009bb77c"; shbts="1662197333,10851247180,1693733333:01f7922667728add527198adb9bb332520bd0b4a233ecb4c650da3524912630fa3ac7645"; sessionid={sis}; rur="RVA,10851247180,1693912293:01f78ed1bfb4b31b309a892edebcbf222a838f50d84e29bcbbf806e997099b1b5deca4b9"','origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty',
'sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','x-asbd-id':'198387',
'x-csrftoken':'BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT','x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR16wNjyuckc0qk4ogcBIWjOuYHm4V6EFi8U2XCJriHI4KVv','x-instagram-ajax':'1006141724'}
			hd = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar,en;q=0.9',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent': generate_user_agent(),
'x-csrftoken':'8uoEYgxjJwHho1KYWE6s2LwIYf6CSgKb',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'}
			FD = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={User}",headers=hd).json()
			IID = FD['data']['user']['id']
			cont = FD['data']['user']['edge_follow']['count']
			re = get(f'https://i.instagram.com/api/v1/friendships/{IID}/following/?count={cont}',headers=hea).json()['users']
			for i in re:
				uss = i['username']
				sleep(int(randint(5,20)))
				rr = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={uss}",headers=hd).json()
				alaa.Follow(sis,rr['data']['user']['id'],uss)			
		def Follo(sis,id,uss):
		    had = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': f'ig_did=3228C28C-878C-4032-B1BA-805CA7DCDE80; mid=YCMNFgALAAGTkjQS4zQTJ887fFG5; ig_nrcb=1; csrftoken=vudL37NP1XL22tCTKXluvvZCwm7kI2Yp; ds_user_id=46015777379; sessionid={sis}; rur=RVA','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36','x-csrftoken': 'vudL37NP1XL22tCTKXluvvZCwm7kI2Yp','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR2Ba9nmJROdSoghzs45qrHKC88BhLBeE0C1g5XLvznnHW1d','x-instagram-ajax': '0edc1000e5e7','x-requested-with': 'XMLHttpRequest'}
		    follo = post(f'https://www.instagram.com/web/friendships/{id}/follow/',headers=had)
		    US = uss.upper()
		    if follo.status_code == 200:
		    	print(B+f"DONE FOLLOWING {B}=> {F}{US}")
		    elif follo.status_code == 400:
		    	print(Z+"- YOUR ACCOUNT CAN'T FOLLOWING USERS {B}=> {Z}{US} !")
		    else:
		    	print(X+"- DON'T FOLLOWING !")
		def Get_I(sis):
			us = input(B+f"USERNAME TO GET {Z}FOLLOWING {B}THEM {Z}:- {X}")
			print(C+"-"*50)
			hea = {'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'cookie':f'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; datr=H9vzYq35j3WCu3W5Jw-BuqMb; dpr=1.75; csrftoken=BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT; ds_user_id=10851247180; shbid="2195,10851247180,1693733333:01f781e1606e53e58d1108b28b348650b4413de9e963e2af156f7f8349ac2dcc009bb77c"; shbts="1662197333,10851247180,1693733333:01f7922667728add527198adb9bb332520bd0b4a233ecb4c650da3524912630fa3ac7645"; sessionid={sis}; rur="RVA,10851247180,1693912293:01f78ed1bfb4b31b309a892edebcbf222a838f50d84e29bcbbf806e997099b1b5deca4b9"','origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty',
'sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','x-asbd-id':'198387',
'x-csrftoken':'BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT','x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR16wNjyuckc0qk4ogcBIWjOuYHm4V6EFi8U2XCJriHI4KVv','x-instagram-ajax':'1006141724'}
			hd = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar,en;q=0.9',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent': generate_user_agent(),
'x-csrftoken':'8uoEYgxjJwHho1KYWE6s2LwIYf6CSgKb',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'}
			FD = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={User}",headers=hd).json()
			IID = FD['data']['user']['id']
			cont = FD['data']['user']['edge_follow']['count']
			re = get(f'https://i.instagram.com/api/v1/friendships/{IID}/following/?count={cont}',headers=hea).json()['users']
			for i in re:
				uss = i['username']
				sleep(2)
				hd = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar,en;q=0.9',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent': generate_user_agent(),
'x-csrftoken':'8uoEYgxjJwHho1KYWE6s2LwIYf6CSgKb',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'}
				rer = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={uss}",headers=hd).json()
				Name = rer['data']['user']['full_name']
				FOLO=rer['data']['user']['edge_followed_by']['count']
				FOO=rer['data']['user']['edge_follow']['count']
				ID = rer['data']['user']['id']
				lok = get(f"https://o7aa.pythonanywhere.com/?id={ID}").json()['data']
				print(Z+"-"*50)
				print(B+f"USER {X}:- {C}"+str(uss)+B+f"\nNAME {X}:- {C}"+str(Name)+B+f'\nFOLLOWER {X}:- {C}'+str(FOLO)+B+f'\nFOLOWING {X}:- {C}'+str(FOO)+B+f'\nID :- {C}'+str(ID)+B+f"\nDATE {X}:- {C}"+str(lok))
				DS = input(f"{F}[{Z}×{F}] {j}Do you want to follow this account {X}• {C}Y or N {X}• {B}:- ")
				if DS == 'Y' or DS == 'y':
					
					alaa.Follo(sis,rer['data']['user']['id'],uss)
				elif DS == 'N' or DS == 'n':
					pass
				
					
		def Story(User,sis,cookie,csrf):
				hd = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar,en;q=0.9',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent': generate_user_agent(),
'x-csrftoken':'8uoEYgxjJwHho1KYWE6s2LwIYf6CSgKb',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'}
				FD = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={User}",headers=hd).json()
				IID = FD['data']['user']['id']
				cont = FD['data']['user']['edge_follow']['count']
				hea = {'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'cookie':f'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; datr=H9vzYq35j3WCu3W5Jw-BuqMb; dpr=1.75; csrftoken=BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT; ds_user_id=10851247180; shbid="2195,10851247180,1693733333:01f781e1606e53e58d1108b28b348650b4413de9e963e2af156f7f8349ac2dcc009bb77c"; shbts="1662197333,10851247180,1693733333:01f7922667728add527198adb9bb332520bd0b4a233ecb4c650da3524912630fa3ac7645"; sessionid={sis}; rur="RVA,10851247180,1693912293:01f78ed1bfb4b31b309a892edebcbf222a838f50d84e29bcbbf806e997099b1b5deca4b9"','origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty',
'sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','x-asbd-id':'198387',
'x-csrftoken':'BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT','x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR16wNjyuckc0qk4ogcBIWjOuYHm4V6EFi8U2XCJriHI4KVv','x-instagram-ajax':'1006141724'}
				re = get(f'https://i.instagram.com/api/v1/friendships/{IID}/following/?count={cont}',headers=hea).json()['users']
				for i in re:
					uuss = i['username']
					hd = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar,en;q=0.9',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent': generate_user_agent(),
'x-csrftoken':'8uoEYgxjJwHho1KYWE6s2LwIYf6CSgKb',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'}
					id_user = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={uuss}",headers=hd).json()['data']['user']['id']
					d = {
                        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-language':'en-US,en;q=0.9,ar;q=0.8',
                        'cookie': cookie,
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47',
                    }
					surl = f'https://www.instagram.com/graphql/query/?query_hash=c9c56db64beb4c9dea2d17740d0259d9&variables=%7B%22reel_ids%22%3A%5B%22{id_user}%22%5D%2C%22tag_names%22%3A%5B%5D%2C%22location_ids%22%3A%5B%5D%2C%22highlight_reel_ids%22%3A%5B%5D%2C%22precomposed_overlay%22%3Afalse%2C%22show_story_viewer_list%22%3Atrue%2C%22story_viewer_fetch_count%22%3A50%2C%22story_viewer_cursor%22%3A%22%22%2C%22stories_video_dash_manifest%22%3Afalse%7D'
					DF = get(surl,headers=d).json()
					stry =  len(DF["data"]["reels_media"][0]["items"])
					for i in range(0,stry):
					   id_story = DF["data"]["reels_media"][0]["items"][i]['id']
					   taken_at_timestamp = DF["data"]["reels_media"][0]["items"][i]['taken_at_timestamp']
					   heades = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7','content-length':'127',
'content-type':'application/x-www-form-urlencoded','cookie':cookie,'origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"',
'sec-fetch-dest':'empty','sec-fetch-mode':'cors',
'sec-fetch-site':'same-site','user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
'x-asbd-id':'198387','x-csrftoken':csrf,
'x-ig-app-id':'1217981644879628','x-ig-www-claim':'hmac.AR16wNjyuckc0qk4ogcBIWjOuYHm4V6EFi8U2XCJriHI4Cpd','x-instagram-ajax':'1006164169',}
					Data = {'reelMediaId': id_story,
'reelMediaOwnerId': id_user,
'reelId': id_user,
'reelMediaTakenAt': taken_at_timestamp,
'viewSeenAt': taken_at_timestamp}
					sleep(int(randint(1,5)))
					sry = post("https://www.instagram.com/stories/reel/seen",headers=heades,data=Data)
					US = uuss.upper()
					if sry.status_code == 200:
					   print(F+f"- THE STORY HAS BEEN SEEN {Z}=> {B}{US}")
					else:
						print(X+f"- THE STORY HAS NOT BEEN SEEN {Z}=> {X}{US}")
		def unf(sis):
				User = input(B+f"USERNAME TO GET {Z}FOLLOWING {B}THEM {Z}:- {X}")
				print(C+"-"*50)
				hea = {'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'cookie':f'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; datr=H9vzYq35j3WCu3W5Jw-BuqMb; dpr=1.75; csrftoken=BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT; ds_user_id=10851247180; shbid="2195,10851247180,1693733333:01f781e1606e53e58d1108b28b348650b4413de9e963e2af156f7f8349ac2dcc009bb77c"; shbts="1662197333,10851247180,1693733333:01f7922667728add527198adb9bb332520bd0b4a233ecb4c650da3524912630fa3ac7645"; sessionid={sis}; rur="RVA,10851247180,1693912293:01f78ed1bfb4b31b309a892edebcbf222a838f50d84e29bcbbf806e997099b1b5deca4b9"','origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty',
'sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','x-asbd-id':'198387',
'x-csrftoken':'BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT','x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR16wNjyuckc0qk4ogcBIWjOuYHm4V6EFi8U2XCJriHI4KVv','x-instagram-ajax':'1006141724'}
				hd = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar,en;q=0.9',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent': generate_user_agent(),
'x-csrftoken':'8uoEYgxjJwHho1KYWE6s2LwIYf6CSgKb',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'}
				FD = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={User}",headers=hd).json()
				IID = FD['data']['user']['id']
				cont = FD['data']['user']['edge_follow']['count']
				re = get(f'https://i.instagram.com/api/v1/friendships/{IID}/following/?count={cont}',headers=hea).json()['users']
				for i in re:
					uss = i['username']
					sleep(int(randint(5,20)))
					YU = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={uss}",headers=hd).json()
					DDI = YU['data']['user']['id']
					head = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7','content-length':'0',
'content-type':'application/x-www-form-urlencoded',
'cookie':f'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; datr=H9vzYq35j3WCu3W5Jw-BuqMb; dpr=1.75; csrftoken=BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT; ds_user_id=10851247180; shbid="2195,10851247180,1694164853:01f78dd4a4c0b70f3dc58b393c09bf2615d39bb860329cf9631b55c48af17296e1bccc69"; shbts="1662628853,10851247180,1694164853:01f768b4a406b5c8cdcc1229042fe6bfce3eb708e046794f5ce38dcfb18b7402cc385e6e"; fbm_124024574287414=base_domain=.instagram.com; sessionid={sis}; fbsr_124024574287414=uGitD8NHUtZITE9yHcOcJ3y93RV7JZfaeZSkFC2CDbI.eyJ1c2VyX2lkIjoiMTAwMDE5NTA1MTAxMTMxIiwiY29kZSI6IkFRQlZnMk1EcmNDZkh2bFpWYUFPZUFPYXl0bmJQMVJzanJhRmd3MTVYaGhSTjExM1VHaGhSSDFoTTVua2lsWFFweXN6WlRVNE5aci1oUHY0NHFLVFdRc21HdG9mTXByZlZ6YmpsaHBER05wUjBtRncwaWFqUzFlTS1KNl8wY2lmSm5MTlRteGNJVEplWF91cXRVekhRcHV1dnR4OEhnMUsySVpTZnVWWXpMLVM2bTUyc2xzUkJWem52MTNuaFBXM0c3d3VHSmppOEk2cFJ3dUFBbTRobEpITFBTeEo5V1k0WDFfcm1DeEg1aFB1V3NlZkl2ZWp3WHFkZnVvdUl2SEZkNHhONkRQNkd6aEJMaFhmNmtwWDdqRUpKY2M5NjRTdjQxRkE4Yk5kR0c5a1BmNUo1STR0WU8xZkdrV1Q3TzJCTGFZIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUVvNE9MVklZWGRyTEJ4MFJUSGhBMFJiNlR1R3pBZWV1SXdoNjZlc1pDODUyODdaQWJ4RjJsaFpDRGhSRmpYNENxNXNMUUN0c0QwWVliMk45WkJaQ244Z2hwQlpCdElyWkNPc3BiQzJiVFpDd0hqNkt4YVg3cVFRMFpDU1pBSkw0TjJIeVNsOGxpeWlaQkh6NkZYQjNYU0laQ3hFeHhzZDhNMWRtaWxsMFd2R0pKS1EiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY2MjczNTU3N30; rur="LDC,10851247180,1694271643:01f757c9ccb40a650fb0cdc72206b873ca1c374821dbb7f6327a956bebe4de154bec128b"','origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"','sec-ch-ua-mobile':'?1',
'sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty','sec-fetch-mode':'cors',
'sec-fetch-site':'same-site','user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
'x-asbd-id':'198387','x-csrftoken':'BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT','x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR16wNjyuckc0qk4ogcBIWjOuYHm4V6EFi8U2XCJriHI4Ibg',
'x-instagram-ajax':'1006173205'}
					req = post(f"https://i.instagram.com/api/v1/web/friendships/{DDI}/unfollow/",headers=head)
					US = uss.upper()
					if req.status_code == 200:
						print(F+f"- DONE {Z}UNFOLLOWING => {X}{US}")
					else:
						print(X+f"- DON'T {Z}FOLLOWING => {X}{US}")
				
def start(sis,cookie,csrf):
	bk = input(f"{Z}({F}1{Z}) {B}AUTO FOLLOW FROM{Z} FOLLOWING {B}USER {X}•\n{Z}({F}2{Z}){B} MANUAL FOLLOW FROM {Z}FOLLOWING {B}USER{X} •\n{Z}({F}3{Z}) {B}WATCH FOLLOWING {Z}STORIES {B}FROM USER{X} •\n{Z}({F}4{Z}) {Z}UNFOLLOW {B}FROM YOUR ACC OR OTHER {X}•{F}\n*{C}--------------------------------------{F}*\n{F}({Z}+{F}) CHOOSE : ")
	if bk == '1':
		system('clear')
		alaa.Get_Id(sis)
	if bk == '2':
		system('clear')
		alaa.Get_I(sis)
	if bk == '3':
		system('clear')
		User = input(B+f"USERNAME TO GET {Z}FOLLOWING {B}THEM {Z}:- {X}")
		print(C+"-"*50)
		alaa.Story(User,sis,cookie,csrf)
	if bk == '4':
		system('clear')
		alaa.unf(sis)
		
alaa.LOGIN()
