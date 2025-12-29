from adminbot import *

@bot.on(events.CallbackQuery(data=b'create-trojan'))
async def create_trojan(event):
	async def create_trojan_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**ᴜsᴇʀɴᴀᴍᴇ:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**ʟɪᴍɪᴛ ɢʙ:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**ᴄʜᴏᴏsᴇ ᴇxᴘɪʀʏ ᴅᴀʏ**",buttons=[
[Button.inline(" 3 ᴅᴀʏ ","3"),
Button.inline(" 7 ᴅᴀʏ ","7")],
[Button.inline(" 30 ᴅᴀʏ ","30"),
Button.inline(" 60 ᴅᴀʏ ","60")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "{user}" "{exp}" "{pw}" | addtr'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**ᴜsᴇʀ ᴀʟʀᴇᴅʏ ᴇxɪsᴛ**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			b = [x.group() for x in re.finditer("trojan://(.*)",a)]
			print(b)
			domain = re.search("@(.*?):",b[0]).group(1)
			uuid = re.search("trojan://(.*?)@",b[0]).group(1)
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
** xʀᴀʏ/ᴛʀᴏᴊᴀɴ ᴀᴄᴄᴏᴜɴᴛ **
**◇━━━━━━━━━━━━━━━━━◇**
**» ʀᴇᴍᴀʀᴋ     :** `{user}`
**» ᴜsᴇʀ ʟɪᴍɪᴛ ɢʙ  :** `{pw} GB`
**» ᴘᴏʀᴛ ᴅɴs    :** `443, 53`
**» ᴘᴏʀᴛ ᴛʟs    :** `222-1000`
**» ᴜsᴇʀ ɪᴅ     :** `{uuid}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴡs    :** 
`{b[0].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ɢʀᴘᴄ  :** 
`{b[1].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴊsᴏɴ  :** `https://${DOMAIN}:81/trojan-{user}.txt`
**◇━━━━━━━━━━━━━━━━━◇**
**ᴇxᴘɪʀᴇᴅ ᴜɴᴛɪʟ:** `{later}`
**◇━━━━━━━━━━━━━━━━━◇**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_trojan_(event)
	else:
		await event.answer("ᴀᴋsᴇs ᴅɪᴛᴏʟᴀᴋ",alert=True)

@bot.on(events.CallbackQuery(data=b'cek-trojan'))
async def cek_trojan(event):
	async def cek_trojan_(event):
		cmd = 'bot-cek-tr'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""

{z}

**sʜᴏᴡs ʟᴏɢɢᴇᴅ ɪɴ ᴜsᴇʀs ᴛʀᴏᴊᴀɴ**
""",buttons=[[Button.inline("‹ ᴍᴀɪɴ ᴍᴇɴᴜ ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await cek_trojan_(event)
	else:
		await event.answer("ᴀᴄᴄᴇss ᴅᴇɴɪᴇᴅ",alert=True)

@bot.on(events.CallbackQuery(data=b'trial-trojan'))
async def trial_trojan(event):
	async def trial_trojan_(event):
		cmd = f'printf "%s\n" | trialtr-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**ᴜsᴇʀ ᴀʟʀᴇᴅʏ ᴇxɪs**")
		else:
			#today = DT.date.today()
			#later = today + DT.timedelta(days=int(exp))
			b = [x.group() for x in re.finditer("trojan://(.*)",a)]
			print(b)
			remarks = re.search("#(.*)",b[0]).group(1)
			domain = re.search("@(.*?):",b[0]).group(1)
			uuid = re.search("trojan://(.*?)@",b[0]).group(1)
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**  xʀᴀʏ/ᴛʀᴏᴊᴀɴ ᴀᴄᴄᴏᴜɴᴛ **
**◇━━━━━━━━━━━━━━━━━◇**
**» ʀᴇᴍᴀʀᴋs     :** `{remarks}`
**» ʜᴏsᴛ sᴇʀᴠᴇʀ :** `{domain}`
**» ᴜsᴇʀ ʟɪᴍɪᴛ ɢʙ  :** `Unlimited`
**» ᴘᴏʀᴛ ᴅɴs    :** `443, 53`
**» ᴘᴏʀᴛ ᴛʟs    :** `222-1000`
**» ᴜsᴇʀ ɪᴅ     :** `{uuid}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴡs    :** 
`{b[0].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ɢʀᴘᴄ  :** 
`{b[1].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴊsᴏɴ  :** `https://${DOMAIN}:81/trojan-{user}.txt`
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `60 Minutes`
**◇━━━━━━━━━━━━━━━━━◇**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_trojan_(event)
	else:
		await event.answer("ᴀᴋsᴇs ᴅɪᴛᴏʟᴀᴋ",alert=True)

@bot.on(events.CallbackQuery(data=b'renew-trojan'))
async def ren_trojan(event):
	async def ren_trojan_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**ᴜsᴇʀɴᴍᴇ:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**ᴄʜᴏᴏsᴇ ᴇxᴘɪʀʏ ᴅᴀʏ**",buttons=[
[Button.inline(" 3 ᴅᴀʏ ","3"),
Button.inline(" 7 ᴅᴀʏ ","7")],
[Button.inline(" 30 ᴅᴀʏ ","30"),
Button.inline(" 60 ᴅᴀʏ ","60")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		cmd = f'printf "%s\n" "{user}" {exp} | renewtr-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**ᴜsᴇʀ ɴᴏᴛ ғᴏᴜɴᴅ**")
		else:
			msg = f"""**sᴜᴄᴄᴇsғᴜʟʟʏ ʀᴇɴᴇᴡᴇᴅ {user} {exp}**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await ren_trojan_(event)
	else:
		await event.answer("ᴀᴋsᴇs ᴅɪᴛᴏʟᴀᴋ",alert=True)
		
@bot.on(events.CallbackQuery(data=b'delete-trojan'))
async def delete_trojan(event):
	async def delete_trojan_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**ᴜsᴇʀɴᴀᴍᴇ:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		cmd = f'printf "%s\n" "{user}" | deltr-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**ᴜsᴇʀ ɴᴏᴛ ғᴏᴜɴᴅ**")
		else:
			msg = f"""**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_trojan_(event)
	else:
		await event.answer("ᴀᴋsᴇs ᴅɪᴛᴏʟᴀᴋ",alert=True)

@bot.on(events.CallbackQuery(data=b'trojan'))
async def trojan(event):
	async def trojan_(event):
		inline = [
[Button.inline(" ᴛʀɪᴀʟ ᴛʀ ","trial-trojan")],
[Button.inline(" ᴄʀᴇᴀᴛᴇ ᴛʀ ","create-trojan"),
Button.inline(" ᴄʜᴇᴄᴋ ᴛʀ ","cek-trojan")],
[Button.inline(" ᴅᴇʟᴇᴛᴇ ᴛʀ ","delete-trojan"),
Button.inline(" ʀᴇɴᴇᴡ ᴛʀ ","renew-trojan")],
[Button.inline("‹ ᴍᴀɪɴ ᴍᴇɴᴜ ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**⚜️           ᴛʀᴏᴊᴀɴ ᴍᴀɴᴀɢᴇʀ              ⚜️**
━━━━━━━━━━━━━━━━━━━━━━━ 
🔰sᴇʀᴠɪᴄᴇ:** `TROJAN`
🔰ᴅᴏᴍᴀɪɴ :** `{DOMAIN}`
🔰ɪsᴘ:** `{z["isp"]}`
🔰ᴄᴏᴜɴᴛʀʏ:** `{z["country"]}`
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trojan_(event)
	else:
		await event.answer("Access Denied",alert=True)
