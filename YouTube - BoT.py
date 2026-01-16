#حقوق (باتريك)
#اذكر مصدر من تنشرة
#مصدر الملف : @B8B_2 & @BOT_PATREK
# اذا خمطت الملف ما ابريلك الذمة الى يوم القيامة 
#بس استمتع بلملف
import pyrogram
from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import *
import yt_dlp
from yt_dlp import *
import youtube_search
from youtube_search import *
import json
from json import *
import wget
import os
#IMPORTING
token="توكن"
api_hash="api_hash"
data={"check":"True"}
api_id=int("api_id")
name="اسم حساب المطور"
name_bot="اسم البوت"
username_bot="يوزر البوت بدون @"
with open(f"check-youtube.json","a+") as ll:
    json.dump(data,ll)
#CONFIG
app=Client(name=name,bot_token=token,api_hash=api_hash,api_id=api_id)
print(True)
#STARTING
@app.on_message(filters.regex("الاوامر"))
def aoamer(app,message):
    message.reply(f"""⚘ اليـوتيوب

تفعيل اليوتيوب 
تعطيل اليوتيوب 

❋ البـحث عن اغنية ↓

بحث اسم الاغنية

يوت اسم الاغنية

YT اسم الاغنية""")
@app.on_message(filters.group&filters.regex("تفعيل اليوتيوب"))
def tf3el(app,message):
    mm=open(f"check-youtube.json")
    m=json.load(mm)['check']
    if m=="True":
        message.reply("⇜ اليوتيوب مفعل من قبل يالطيب ..")
    else:
        chat_member=app.get_chat_member(message.chat.id, message.from_user.id)
        if chat_member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
            data={"check":"True"}
            os.system('rm -rf check-youtube.json')
            with open(f"check-youtube.json","a+") as ll:
                json.dump(data,ll)
            message.reply(f"""
    ⇜ من 「 {message.from_user.mention} 」 
    ⇜ ابشر فعلت اليوتيوب
    ༄
                """)
        else:
            message.reply("⇜ الامر يخص ( المالك ، الادمن )")
    
@app.on_message(filters.group&filters.regex("تعطيل اليوتيوب"))
def t3del(app,message):
    mm=open(f"check-youtube.json")
    m=json.load(mm)['check']
    if m=="False":
        message.reply("⇜ اليوتيوب معطل من قبل يالطيب ..")
    else:
        chat_member=app.get_chat_member(message.chat.id, message.from_user.id)
        if chat_member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
            data={"check":"False"}
            os.system('rm -rf check-youtube.json')
            with open(f"check-youtube.json","a+") as ll:
                json.dump(data,ll)
            message.reply(f"""
    ⇜ من 「 {message.from_user.mention} 」 
    ⇜ ابشر عطلت اليوتيوب
    ༄
                """)
        else:
            message.reply("⇜ الامر يخص ( المالك ، الادمن )")
def check_youtube():
    mm=open(f"check-youtube.json")
    m=json.load(mm)['check']
    if m=="True":
        return True
    else:
        return False
@app.on_message(filters.command("start")&filters.private)
def starting(app,message):
    you_bot=f"""[{name_bot}](t.me/{username_bot})"""
    you=f"""[{message.from_user.first_name}](t.me/{message.from_user.username})"""
    app.send_message(chat_id=message.chat.id,text=f"""👋┇أهلاً بك عزيزي ({you})
في بـوت بحـث وتحـمـيل من اليوتـيوب 
البـوت يـوفر لـك طرق كثيـرا للبـحث
يمكـنك التحميل بسـهولة 
فقط من ارسـال الرابـط 

-""",disable_web_page_preview=True,parse_mode=enums.ParseMode.MARKDOWN)
@app.on_message(filters.group&filters.regex("بحث"))
def serche(app,message):
    chk=check_youtube()
    if chk==False:
        message.reply("⇜ اليوتيوب معطل من قبل يالطيب ..")
    else:
       if len(message.text.split(None, 1)) < 2:
           return 
       query = message.text.split(None, 1)[1]
       ser=YoutubeSearch(query,max_results=5).to_dict()
       title_list=[]
       vid_list=[]
       duration_list=[]
       views_list=[]
       for r in ser:
           title_list.append(r["title"][:22])
           vid_list.append(r["id"])
           duration_list.append(r["duration"])
           views_list.append(r["views"])
       text=f"""🔎┇نتائج بحث اليوتيوب ل {query}

🎬 {title_list[0]}
🕛 {duration_list[0]} - 👁 {views_list[0]} 
🔗 /dl_{vid_list[0]}

🎬 {title_list[1]}
🕛 {duration_list[1]} - 👁 {views_list[1]} 
🔗 /dl_{vid_list[1]}

🎬 {title_list[2]}
🕛 {duration_list[2]} - 👁 {views_list[2]} 
🔗 /dl_{vid_list[2]}

🎬 {title_list[3]}
🕛 {duration_list[3]} - 👁 {views_list[3]} 
🔗 /dl_{vid_list[3]}

🎬 {title_list[4]}
🕛 {duration_list[4]} - 👁 {views_list[4]} 
🔗 /dl_{vid_list[4]}
        """
       message.reply(text)
@app.on_message(filters.group&filters.regex('يوت (.*?)'))
def yut(app,message):
    chk=check_youtube()
    if chk==False:
        message.reply("⇜ اليوتيوب معطل من قبل يالطيب ..")
    else:
           if len(message.text.split(None, 1)) < 2:
               return 
           query = message.text.split(None, 1)[1]
           if "https://youtu.be/" in query or "https://www.youtube.com/" in query or "https://youtube.com/" in query:
               download = InlineKeyboardMarkup([[InlineKeyboardButton(name_bot, url=f'T.me/{username_bot}')]])
               hi=app.send_message(chat_id=message.chat.id,text="**جاري التحميل ..**", reply_markup=download)
               yt = YoutubeSearch(query, max_results=1).to_dict()
               duration=yt[0]["duration"]
               with yt_dlp.YoutubeDL({"format": "bestaudio[ext=m4a]"}) as ytdl:
                   info = ytdl.extract_info(query, download=False)
                   audio = ytdl.prepare_filename(info)
                   ytdl.process_info(info)
               message.reply_audio(audio=audio,caption=f"@{username_bot} ~  ⏳ [{duration}]({query})",reply_to_message_id=message.id)
               app.delete_messages(message.chat.id,hi.id)
           else:
               yt = YoutubeSearch(query, max_results=1).to_dict()
               vid_id=yt[0]["id"]
               query = f'https://youtu.be/{vid_id}'
               download = InlineKeyboardMarkup([[InlineKeyboardButton(name_bot, url=f'T.me/{username_bot}')]])
               hi=app.send_message(chat_id=message.chat.id,text="**جاري التحميل ..**", reply_markup=download)
               yt = YoutubeSearch(query, max_results=1).to_dict()
               duration=yt[0]["duration"]
               with yt_dlp.YoutubeDL({"format": "bestaudio[ext=m4a]"}) as ytdl:
                   info = ytdl.extract_info(query, download=False)
                   audio = ytdl.prepare_filename(info)
                   ytdl.process_info(info)
               message.reply_audio(audio=audio,caption=f"@{username_bot} ~  ⏳ [{duration}]({query})",reply_to_message_id=message.id)
               app.delete_messages(message.chat.id,hi.id)
@app.on_message(filters.group&filters.regex('YT (.*?)'))
def yt(app,message):
    chk=check_youtube()
    if chk==False:
        message.reply("⇜ اليوتيوب معطل من قبل يالطيب ..")
    else:
           if len(message.text.split(None, 1)) < 2:
               return 
           query = message.text.split(None, 1)[1]
           if "https://youtu.be/" in query or "https://www.youtube.com/" in query or "https://youtube.com/" in query:
               download = InlineKeyboardMarkup([[InlineKeyboardButton(name_bot, url=f'T.me/{username_bot}')]])
               hi=app.send_message(chat_id=message.chat.id,text="**جاري التحميل ..**", reply_markup=download)
               yt = YoutubeSearch(query, max_results=1).to_dict()
               duration=yt[0]["duration"]
               with yt_dlp.YoutubeDL({"format": "bestaudio[ext=m4a]"}) as ytdl:
                   info = ytdl.extract_info(query, download=False)
                   audio = ytdl.prepare_filename(info)
                   ytdl.process_info(info)
               message.reply_audio(audio=audio,caption=f"@{username_bot} ~  ⏳ [{duration}]({query})",reply_to_message_id=message.id)
               app.delete_messages(message.chat.id,hi.id)
           else:
               yt = YoutubeSearch(query, max_results=1).to_dict()
               vid_id=yt[0]["id"]
               query = f'https://youtu.be/{vid_id}'
               download = InlineKeyboardMarkup([[InlineKeyboardButton(name_bot, url=f'T.me/{username_bot}')]])
               hi=app.send_message(chat_id=message.chat.id,text="**جاري التحميل ..**", reply_markup=download)
               yt = YoutubeSearch(query, max_results=1).to_dict()
               duration=yt[0]["duration"]
               with yt_dlp.YoutubeDL({"format": "bestaudio[ext=m4a]"}) as ytdl:
                   info = ytdl.extract_info(query, download=False)
                   audio = ytdl.prepare_filename(info)
                   ytdl.process_info(info)
               message.reply_audio(audio=audio,caption=f"@{username_bot} ~  ⏳ [{duration}]({query})",reply_to_message_id=message.id)
               app.delete_messages(message.chat.id,hi.id)
@app.on_message(filters.group&filters.regex('/dl_(.*?)'))
def dl_(app,message):
    chk=check_youtube()
    if chk==False:
        message.reply("⇜ اليوتيوب معطل من قبل يالطيب ..")
    else:
        if message.text=="/dl_":
            return
        vid_id=message.text.split("/dl_")[1]
        url=f'https://youtu.be/{vid_id}'
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("صوت 💿", callback_data=f'AUDIO{vid_id}'),InlineKeyboardButton("فيديو 🎥", callback_data=f'VIDEO{vid_id}'),]])
        yt = YoutubeSearch(f'https://youtu.be/{vid_id}', max_results=1).to_dict()
        title = yt[0]['title']
        thumbnails=yt[0]["thumbnails"][0]
        message.reply_photo(photo=thumbnails,caption=f"""**⤶ العنوان - [{title}]({url})**""",reply_markup=reply_markup)
@app.on_callback_query(filters.group&filters.regex("AUDIO"))
def get_audio(app,query:CallbackQuery):
    chk=check_youtube()
    if chk==False:
        query.message.reply("⇜ اليوتيوب معطل من قبل يالطيب ..")
    download = InlineKeyboardMarkup([[InlineKeyboardButton(name_bot, url=f'T.me/{username_bot}')]])
    vid_id = query.data.split("AUDIO")[1]
    url = f'https://youtu.be/{vid_id}'
    hi=query.edit_message_text("**جاري التحميل ..**", reply_markup=download)
    yt = YoutubeSearch(f'https://youtu.be/{vid_id}', max_results=1).to_dict()
    duration=yt[0]["duration"]
    print(duration)
    with yt_dlp.YoutubeDL({"format": "bestaudio[ext=m4a]"}) as ytdl:
        info = ytdl.extract_info(url, download=False)
        audio = ytdl.prepare_filename(info)
        ytdl.process_info(info)
    query.message.reply_audio(audio=audio,caption=f"@{username_bot} ~  ⏳ [{duration}]({url})",reply_to_message_id=query.message.id)
    app.delete_messages(query.message.chat.id,hi.id)
@app.on_callback_query(filters.group&filters.regex("VIDEO"))
def get_video(app,query:CallbackQuery):
    chk=check_youtube()
    if chk==False:
        query.message.reply("⇜ اليوتيوب معطل من قبل يالطيب ..")
    download = InlineKeyboardMarkup([[InlineKeyboardButton(name_bot, url=f'T.me/{username_bot}')]])
    vid_id = query.data.split("VIDEO")[1]
    url = f'https://youtu.be/{vid_id}'
    hi=query.edit_message_text("**جاري التحميل ..**", reply_markup=download)
    yt = YoutubeSearch(f'https://youtu.be/{vid_id}', max_results=1).to_dict()
    duration=yt[0]["duration"]
    thumbnails=yt[0]["thumbnails"][0]
    with yt_dlp.YoutubeDL({"format": "best","keepvideo": True,"prefer_ffmpeg": False,"geo_bypass": True,"outtmpl": "%(title)s.%(ext)s","quite": True}) as ytdl:
        info = ytdl.extract_info(url, download=False)
        video = ytdl.prepare_filename(info)
        ytdl.process_info(info)
    thumb = wget.download(thumbnails)
    query.message.reply_video(video=video,thumb=thumb,caption=f"@{username_bot} ~  ⏳ [{duration}]({url})")
    app.delete_messages(query.message.chat.id,hi.id)
app.run()
#حقوق (باتريك)
#اذكر مصدر من تنشرة
#مصدر الملف : @B8B_2 & @BOT_PATREK
# اذا خمطت الملف ما ابريلك الذمة الى يوم القيامة 
#بس استمتع بلملف