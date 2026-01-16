try:
    import requests
except:
    print("[!] Install requests ")
    input("")
    exit()
try:
    import json
except:
    print("[!] Install JSON ")
    input("")
    exit()
import time
try:
    f = open("list.txt","r").read().splitlines()
except:
    print("[!] Make File (list.txt)")
    input("")
    exit()
print("""
  _____   _____  __      __  _______ 
 / ____| |_   _| \ \    / / |__   __|
| |  __    | |    \ \  / /     | |   
| | |_ |   | |     \ \/ /      | |   
| |__| |  _| |_     \  /       | |   
 \_____| |_____|     \/        |_|  
        telegram https://t.me/givtt""")
urls = ["https://api.tellonym.me/tokens/create","https://api.tellonym.me/accounts/settings"]
username = input("[?] Enter Username:")
password = input("[?] Enter Password:") #تغيرك للحقوق لا يعني انك مبرمج LOL
def login():
    global urls
    global username,password
    headers = {
        "Host": "api.tellonym.me",
        "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://tellonym.me/login",
        "tellonym-client": "web:0.52.0",
        "content-type": "application/json;charset=utf-8",
        "Content-Length": "709",
        "Origin": "https://tellonym.me",
        "DNT": "1",
        "Connection": "keep-alive",
        "TE": "Trailers"}
    data = {
        "captcha":"03AGdBq26eDPE5ylyMOTxRobY0MGKRn9kfrKJqwb0MNdZypzACDJn9nb5sxDm_5onePXs4ucur2ujny-RqSN5s5QgfLRbnvy98IPJmK9fKGzW1Fi11KkxGPsbBu6RGGlY0m_lTaptAMM-r81Og_Pjb5NOy-Utiz92E_yHpLu7V1H3uocZzzs0zaV363a4k_PkUUVUETJaymMYrNMsjFW2Ihoxpb4IVRiwC7m8W4_1f00lp9CNPjLGD3eShN4SJMAWGSh-7xBzzU1JKerQjLGzWPwFevXu14FgywtbKQiIrAvmj6eq7QU6vqlTQ8At890Rf8XxZlKpX77N6o54_jG96zZphSnKwhh7ysOz5FhAipppWQvApagVYs7N2qzxdpuKZVNR8f2WiWogTVu3MAF-IGNby5kFvD3Ipy6wYidYpxVBjIvvRQbGVaVQ6Gbx3TO_Ehowfuv2l5Gam",
        "deviceName":"Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
        "deviceType":"web",
        "email":username,
        "lang":"en",
        "limit":"25",
        "password":password}
    r = requests.post(urls[0], headers=headers,data=json.dumps(data))
    if r.text.find('Wrong credentials')>=0:
        print("[X] Error password or account")
    else:
        print("[+] Done login")
        coo = str(r.json()['accessToken'])
        swap(coo=coo)
def swap(coo):
    global urls,username,password
    a = 0
    for target in f:
        url_check = f'https://tellonym.me/{target}'
        headers_check = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
        r_check = requests.get(url_check, headers=headers_check)
        if r_check.status_code == 404:
            headers = {
                "Host": "api.tellonym.me",
                "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
                "Accept": "application/json",
                "Accept-Language": "en-US,en;q=0.5",
                "Referer": "https://tellonym.me/profile/edit",
                "tellonym-client": "web:0.52.0",
                "content-type": "application/json;charset=utf-8",
                "authorization": f"Bearer {coo}",
                "Content-Length": "77",
                "Origin": "https://tellonym.me",
                "DNT": "1",
                "Connection": "keep-alive",
                "TE": "Trailers"}
            data = {
                "instagram": "givt_ops",
                "limit": "25",
                "snapchat": "",
                "twitter": "",
                "username": target}
            r = requests.post(urls[1], headers=headers, data=json.dumps(data))
            if r.text.find('Username is already in use') >= 0:
                print(f"[-] Taken:{target}")
                a += 1
            elif r.text.find('Ratelimit reached. Slow down') >= 0:
                print('[X] Blocked --Time sleep ON')
                time.sleep(50)
            else:
                try:
                    get = str(r.json()['username'])
                    gat = str(r.json()['email'])
                    print(f"\n[+] Done !@{get}\nemail:{gat}\npassword:{password}\n")
                    break
                except:
                    print(f"[!] Done @{target}\nerror Swap")
        elif r_check.status_code == 200:
            a+=1
            print(f"\r[+] Taken:{a}",end="")
        else:
            print(f"\r[+] Taken:{a}", end="")
login()
print('Finished Checking !')
input('Enter Any Key To Exit: ')
exit()