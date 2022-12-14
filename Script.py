class script(object):
    START_TXT = """๐ท๐ด๐ป๐ป๐พ {},
แดสษช๊ฑ ษช๊ฑ แด๊ฐ๊ฐษชแดษชแดส สแดแด ๊ฐแดส <a href='https://t.me/Cinema_Beacon_Group'><b>๐ แดษชษดแดแดแด สแดแดแดแดษด ๐</b></a> and <a href='https://t.me/Cinema_Company_Malayalam'><b>๐ฝ แดษชษดแดแดแด แดแดแดแดแดษดส ๐ฝ</b></a> ษขสแดแดแด๊ฑ"""
    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """โฎ แดณสณแตแตแต ยน: <a href='https://t.me/Cinema_Beacon_Group'><b>๐ แดษชษดแดแดแด สแดแดแดแดษด ๐</b></a>
โฎ แดณสณแตแตแต ยฒ: <a href='https://t.me/Cinema_Company_Malayalam'><b>๐ฝ แดษชษดแดแดแด แดแดแดแดแดษดส ๐ฝ</b></a>
โฎ ๐ป๐ธ๐ฑ๐๐ฐ๐๐: ๐ฟ๐๐๐พ๐ถ๐๐ฐ๐ผ
โฎ ๐ป๐ฐ๐ฝ๐ถ๐๐ฐ๐ถ๐ด: ๐ฟ๐๐๐ท๐พ๐ฝ ๐น
โฎ ๐ณ๐ฐ๐๐ฐ ๐ฑ๐ฐ๐๐ด: <a href=https://www.mongodb.com>๐ผ๐พ๐ฝ๐ถ๐พ ๐ณ๐ฑ</a>
โฎ ๐ฑ๐พ๐ ๐๐ด๐๐๐ด๐: ๐ท๐ด๐๐พ๐บ๐
โฎ แดแดกษดแดส: https://t.me/Ramanan_TG"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>  
- Filter is the feature were users can set automated replies for a particular keyword and Bot will respond whenever a keyword is found the message
<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
โพ /filter - <code>add a filter in chat</code>
โพ /filters - <code>list all the filters of a chat</code>
โพ /del - <code>delete a specific filter in chat</code>
โพ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
- Bot Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:Link)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
โพ /connect  - <code>connect a particular chat to your PM</code>
โพ /disconnect  - <code>disconnect from a chat</code>
โพ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
These are the extra features of ALEXA
<b>Commands and Usage:</b>
โพ /id - <code>get id of a specifed user.</code>
โพ /info  - <code>get information about a user.</code>
โพ /imdb  - <code>get the film information from IMDb source.</code>
โพ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my OแฏแEแโก
<b>Commands and Usage:</b>
โพ /logs - <code>to get the rescent errors</code>
โพ /stats - <code>to get status of files in db.</code>
โพ /delete - <code>to delete a specific file from db.</code>
โพ /users - <code>to get list of my users and ids.</code>
โพ /chats - <code>to get list of the my chats and ids </code>
โพ /leave  - <code>to leave from a chat.</code>
โพ /disable  -  <code>do disable a chat.</code>
โพ /ban  - <code>to ban a user.</code>
โพ /unban  - <code>to unban a user.</code>
โพ /channel - <code>to get list of total connected channels</code>
โพ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โฎ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โฎ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โฎ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โฎ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#๐๐๐ฐ๐๐ซ๐จ๐ฎ๐ฉ
โฎ ๐๐ซ๐จ๐ฎ๐ฉ โบโบ {}(<code>{}</code>)
โฎ ๐๐จ๐ญ๐๐ฅ ๐๐๐ฆ๐๐๐ซ๐ฌ โบโบ <code>{}</code>
โฎ ๐๐๐๐๐ ๐๐ฒ โบโบ {}
"""
    LOG_TEXT_P = """#๐๐๐ฐ๐๐ฌ๐๐ซ
โฎ ๐๐ โบโบ <code>{}</code>
โฎ ๐๐๐ฆ๐ โบโบ {}
"""
    CARBON_TXT = """ <b>๐ฒ๐ฐ๐๐ฑ๐พ๐ฝ ๐ผ๐พ๐ณ๐๐ป๐ด</b>
<b>๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐ฑ๐ด๐ฐ๐๐๐ธ๐ต๐ ๐๐พ๐๐ ๐ฒ๐พ๐ณ๐ด๐ ๐ฑ๐ ๐๐๐ธ๐ฝ๐ถ ๐๐ท๐ ๐ต๐ด๐ฐ๐๐๐๐ด...</b>
<b>๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ.!</b>
<b>/carbon โบโบ ๐๐ด๐ฟ๐ป๐ ๐๐พ ๐ฐ๐ฝ๐ ๐๐ด๐๐ ๐ผ๐ด๐๐๐ฐ๐ถ๐ด</b>
<b>๐๐พ๐๐บ๐ ๐พ๐ฝ ๐ฑ๐พ๐๐ท ๐ถ๐๐พ๐๐ฟ ๐ฐ๐ฝ๐ณ ๐ฟ๐ผ</b>"""
