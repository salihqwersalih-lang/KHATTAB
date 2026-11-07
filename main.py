from telethon import TelegramClient, events
import config

client = TelegramClient(config.SESSION, config.API_ID, config.API_HASH)

@client.on(events.NewMessage(pattern=r"\.فحص"))
async def check(event):
    await event.edit("**سورس خطاب شغال 🔥**\n`المطور : خطاب`")

@client.on(events.NewMessage(pattern=r"\.الاوامر"))
async def cmds(event):
    await event.edit("**اوامر سورس خطاب 📜**\n\n`.فحص` - فحص السورس\n`.الاوامر` - هاي القائمة\n\n**المطور : خطاب**")

client.start()
print("سورس خطاب اشتغل - المطور خطاب")
client.run_until_disconnected()
