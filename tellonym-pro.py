import requests
import json
from time import sleep
import os , sys





red_color = "\033[1;31m"
info_color = "\033[1;33m"
detect_color = "\033[1;34m"
end_banner_color = "\33[00m"

print("""
Unofficial and unstable alert, it may be closed at any time

    
    ⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠈⣿
    ⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⣿⣿⣿⣿⡄⠄⣿
    ⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⣿⣿⣿⣿⡇⠄⣿
    ⣿⣿⣿⣿⣿⣿⣦⣀⠄⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⡟⠄⠄⣿⣿⣿⣿⡇⠄⣿
    ⣿⣿⣿⣿⣿⡿⠿⠿⠄⠄⠄⠿⢿⣿⣿⣿⣿⣿⣿⣿⣇⠄⠄⣿⣿⣿⣿⡇⠄⣿
    ⣿⣿⡿⠟⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠻⣿⣿⣿⣿⡟⠄⠄⠉⠉⠉⠉⠄⠄⣿
    ⣿⣿⣥⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣿⣿

   ⚠️ ++ The developer : Falah - 0xfff080 ++ ⚠️
            
---------------------------------------""")

url = "https://api.tellonym.me/tokens/create"
# Login API URL

headers = {
    "Host": "api.tellonym.me",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Connection": "keep-alive",
    "tellonym-client": "ios:3.0.1:772:14:iPhone13,2",
    "User-Agent": "Tellonym/772 CFNetwork/1206 Darwin/20.1.0",
    "Accept-Language": "en",
    }

email = input("Username/Email: ")
# Email Or Username Input
password = input("Password: ")

data = {
    "activeExperimentId": 0,
    "password": password,
    "country": "US",
    "deviceName": "Soud’s iPhone",
    "deviceType": "ios",
    "lang": "en",
    "limit": 16,
    "email": email
}
# Login API Data

req = requests.post(url, json=data, headers=headers)
# Login API Request

if "WRONG_CREDENTIALS" in req.text:
    print("\033[1;31m" + "Login Failed, Try Again")

elif "PARAMETER_MISSING" in req.text:
    print("\033[1;31m"+ "Missing Something, Try Again")

elif "accessToken" in req.text:
    print("""
    
    Login Success
    
    """)
    token = json.loads(req.text)["accessToken"]
    
    
    print("""
    تبديل المدينه الي مدينه من اختيارك  مثال :

    latitude -> 24.786182
    longitude -> 46.675641

    https://www.google.com.sa/maps : تستخرج الاحداثيات من
    
     """)
    
    
    ss = input ('latitude -> ')
    ss1 = input ('longitude -> ')
    url = "https://api.tellonym.me/accounts/settings"

    headers = {
    "Host": "api.tellonym.me",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "tellonym-client": "ios:2.77.2:676:14:iPhone13,2",
    "User-Agent": "Tellonym/676 CFNetwork/1206 Darwin/20.1.0",
    "Authorization": f"Bearer {token}",
    "Accept-Language": "en",
    }

    data = {
    "hasAllowedSearchByLocation": "true",
    "latitude":ss,
    "longitude":ss1,
    "limit":16,
}

    req = requests.post(url, json=data , headers=headers)
    print("تم ذلك راجع حسابك من فضلك")

    print("""
    
    ايموجيات مدفوعه ونادره اختارها لحسابك 
    
     """)

    print("""
    
    0 = Delet emoji
    1  = 🥰
    2  = 😎
    4  = 🤬
    5  = 😭
    6  = 😔
    8  = 💪
    9  = 🤯
    10 = 👿
    11 = 🥳
    12 = 💩
    13 = 🤩
    14 = 😍
    16 = 🧻
    17 = 😢
    18 = 🎉
    21 = 👻
    22 = 👊
    23 = 🦄
    24 = 🙉
    25 = 🌈
    26 = ☠️
    
    """)
    
    flo = int(input("-> "))
    url = "https://api.tellonym.me/accounts/settings"

    headers = {
    "Host": "api.tellonym.me",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "tellonym-client": "ios:3.0.1:772:14:iPhone13,2",
    "User-Agent": "Tellonym/772 CFNetwork/1206 Darwin/20.1.0",
    "Authorization": f"Bearer {token}",
    "Accept-Language": "en",
    }

    data = {
    "statusEmoji": flo,
    "limit": 16,
}

    req = requests.post(url, json=data , headers=headers)
    print("تم ذلك راجع حسابك من فضلك")

else:
    print(red_color+"Error !")
    print(req)
    print(req.text)
    exit()


