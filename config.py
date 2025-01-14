import os, time, re
id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "28744454")
    API_HASH  = os.environ.get("API_HASH", "debd37cef0ad1a1ce45d0be8e8c3c5e7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7629093637:AAELMuIlnb0eJSikh28KRLhBmmsEy2gfviI") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Renamex")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://jeffymoses123:jeffymoses123@cluster0.ybmj0.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/vC2.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "-1002076655534") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002402968652"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """Hᴇʏ {} 🌹

🫧 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍᴇ ʙᴏᴛ!
ᴡʜɪᴄʜ ᴄᴀɴ ᴍᴀɴᴜᴀʟʟʏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ғɪʟᴇs ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴀʟsᴏ ᴄᴀɴ sᴇᴛ ᴘʀᴇғɪx ᴀɴᴅ sᴜғғɪx ᴏɴ ʏᴏᴜʀ ғɪʟᴇs.⚡️

<blockquote>✨ ᴛʜɪs ʙᴏᴛ ɪs ᴅᴇᴘʟᴏʏᴇᴅ ʙʏ @JeffySama</blockquote>
─────────────────"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>My Name</b> : {}
├<b>Developer</b> : <a href=https://t.me/JeffySama>Dᴇᴠᴇʟᴏᴘᴇʀ</a> 
├<b>Main Channel</b> : <a href=https://t.me/Anime_Stardust>Aɴɪᴍᴇ Sᴛᴀʀᴅᴜsᴛ</a>
├<b>Main Channel</b> : <a href=https://t.me/Anime_Weekends>Aɴɪᴍᴇ Wᴇᴇᴋᴇɴᴅs</a>
├<b>Support Channel</b> : <a href=https://t.me/Weebs_Weekends>Sᴜᴘᴘᴏʀᴛ</a>
├<b>Bot Updates</b> : <a href=https://t.me/EmitingStars_Botz>Mᴏʀᴇ Bᴏᴛᴢ</a>
├<b>Network</b> : <a href=https://t.me/Eminence_Society>Nᴇᴛᴡᴏʀᴋ</a>
├<b>Pookie</b> : <a href=https://t.me/Alisa_Zoe>Assɪsᴛᴀɴᴛ</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/JeffySama>Developer</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
 <b>🍀 Join @Anime_Weekends
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `clementrajadurai@okhdfcbank`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>By :- @Anime_Weekends</code>

💬 For Any Help Contact @JeffySama
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
