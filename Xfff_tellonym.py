import requests
import sys

user = input('user_tellonym -> ')


url = "https://api.tellonym.me/profiles/name/"+user

print("""

---------------------------------------

0wW    Ww0800                 
(O)\  /(O)  wWw   wWw   wWw   
 `. \/ .'   (O)_  (O)_  (O)_  
   \  /    .' __).' __).' __) 
   /  \   (  _) (  _) (  _)   
 .' /\ `.  )/    )/    )/     
(_.'  `._)(     (     (       
	
++ The developer : Falah - 0xfff080 ++

snapchat : flaah999

---------------------------------------
	
	
    """)

payload = ""
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "X-Parse-Installation-Id": "25cfde8f-7204-434e-a7fb-dde295ee4f70", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36", 
    "Connection": "close", 
    "X-Parse-Application-Id": "RTE8CXsUiVWfG1XlXOyJAxfonvt", 
    "Host": "api.tellonym.me", 
    "Accept-Encoding": "gzip, deflate", 
    "Upgrade-Insecure-Requests": "1", 
    "Accept-Language": "en-US,en;q=0.9", 
    "X-Parse-Client-Version": "i1.17.3", 
    "X-Parse-Session-Token": "HjAtuvE2ARmFRh53w7k3ANxruC2Tm1XUVNJpo0Ik4FU-1695798140-0-ATgsEHEuVOvYl1UMjCsolYczv95Owx5sR+jXTyW5S8J8aIY3QyWeGEAy+gBNQLIkJBz6/Za1rD1jBBqWxQLKzIY=", 
    "X-Parse-OS-Version": "12.9 (saud)"
}
print(url)
response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)


