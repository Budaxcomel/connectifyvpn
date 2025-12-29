from adminbot import *

@bot.on(events.CallbackQuery(data=b'create-vless'))
async def create_vless(event):
	async def create_vless_(event):
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
		cmd = f'printf "%s\n" "{user}" "{exp}" "{pw}" | addvless-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			x = [x.group() for x in re.finditer("vless://(.*)",a)]
			print(x)
			# remarks = re.search("#(.*)",x[0]).group(1)
			# domain = re.search("@(.*?):",x[0]).group(1)
			uuid = re.search("vless://(.*?)@",x[0]).group(1)
			# path = re.search("path=(.*)&",x[0]).group(1)
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
** xʀᴀʏ/ᴠʟᴇss ᴀᴄᴄᴏᴜɴᴛ **
**◇━━━━━━━━━━━━━━━━━◇**
**» ʀᴇᴍᴀʀᴋs     :** `{user}`
**» ʜᴏsᴛ sᴇʀᴠᴇʀ :** `{DOMAIN}`
**» ᴜsᴇʀ ʟɪᴍɪᴛ ɢʙ  :** `{pw} GB`
**» ᴘᴏʀᴛ ᴛʟs    :** `443-900`
**» ᴘᴏʀᴛ ɴᴏɴᴛʟs   :** `80, 8080, 8081-9999`
**» ɴᴇᴛᴡᴏʀᴋ     :** `(WS) or (gRPC)`
**» ᴜsᴇʀ ɪᴅ     :** `{uuid}`
**» ᴘᴀᴛʜ ᴠʟᴇss  :** `vless `
**» ᴘᴀᴛʜ ᴅʏɴᴀᴍɪᴄ:** `http://BUG.COM/vless `
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴛʟs   : **
`{x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ɴᴛʟs  :**
`{x[1].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ɢʀᴘᴄ  :**
`{x[2].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴊsᴏɴ  :** `https://${DOMAIN}:81/vless-{user}.txt`
**◇━━━━━━━━━━━━━━━━━◇**
**» ᴇxғɪʀᴇᴅ ᴜɴᴛɪʟ:** `{later}`
**◇━━━━━━━━━━━━━━━━━◇**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_vless_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'cek-vless'))
async def cek_vless(event):
	async def cek_vless_(event):
		cmd = 'bot-cek-vless'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""

{z}

**Shows Logged In Users Vless**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await cek_vless_(event)
	else:
		await event.answer("Access Denied",alert=True)
		
@bot.on(events.CallbackQuery(data=b'renew-vless'))
async def ren_vless(event):
	async def ren_vless_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**Choose Expiry Day**",buttons=[
[Button.inline(" 3 ᴅᴀʏ ","3"),
Button.inline(" 7 ᴅᴀʏ ","7")],
[Button.inline(" 30 ᴅᴀʏ ","30"),
Button.inline(" 60 ᴅᴀʏ ","60")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		cmd = f'printf "%s\n" "{user}" {exp} | renewvless-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Not Found**")
		else:
			msg = f"""**Successfully Renewes {user} {exp} Days**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await ren_vless_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'delete-vless'))
async def delete_vless(event):
	async def delete_vless_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		cmd = f'printf "%s\n" "{user}" | delvless-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Not Found**")
		else:
			msg = f"""**Successfully Deleted**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_vless_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'trial-vless'))
async def trial_vless(event):
	async def trial_vless_(event):
		async with bot.conversation(chat) as exp:
			cmd = f'printf "%s\n"| trialvless-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			#today = DT.date.today()
			#later = today + DT.timedelta(days=int(exp))
			x = [x.group() for x in re.finditer("vless://(.*)",a)]
			print(x)
			remarks = re.search("#(.*)",x[0]).group(1)
			# domain = re.search("@(.*?):",x[0]).group(1)
			uuid = re.search("vless://(.*?)@",x[0]).group(1)
			# path = re.search("path=(.*)&",x[0]).group(1)
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
** xʀᴀʏ/ᴠʟᴇss ᴀᴄᴄᴏᴜɴᴛ **
**◇━━━━━━━━━━━━━━━━━◇**
**» ʀᴇᴍᴀʀᴋs     :** `{remarks}`
**» ʜᴏsᴛ sᴇʀᴠᴇʀ :** `{DOMAIN}`
**» ᴜsᴇʀ ʟɪᴍɪᴛ ɢʙ  :** `{pw} GB`
**» ᴘᴏʀᴛ ᴛʟs    :** `443-900`
**» ᴘᴏʀᴛ ɴᴏɴᴛʟs   :** `80, 8080, 8081-9999`
**» ɴᴇᴛᴡᴏʀᴋ     :** `(WS) or (gRPC)`
**» ᴜsᴇʀ ɪᴅ     :** `{uuid}`
**» ᴘᴀᴛʜ ᴠʟᴇss  :** `vless `
**» ᴘᴀᴛʜ ᴅʏɴᴀᴍɪᴄ:** `http://BUG.COM/vless `
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴛʟs   : **
`{x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ɴᴛʟs  :**
`{x[1].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ɢʀᴘᴄ  :**
`{x[2].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴊsᴏɴ  :** `https://${DOMAIN}:81/vless-{user}.txt`
**◇━━━━━━━━━━━━━━━━━◇**
**» ᴇxᴘɪʀᴇᴅ ᴜɴᴛɪʟ :** `60 Minutes`
**◇━━━━━━━━━━━━━━━━━◇**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_vless_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'vless'))
async def vless(event):
	async def vless_(event):
		inline = [
[Button.inline(" ᴛʀɪᴀʟ ᴠʟ ","trial-vless")],
[Button.inline(" ᴄʀᴇᴀᴛᴇ  ᴠʟ ","create-vless"),
Button.inline(" ᴄʜᴇᴄᴋ ᴠʟ ","cek-vless")],
[Button.inline(" ᴅᴇʟᴇᴛᴇ ᴠʟ ","delete-vless"),
Button.inline(" ʀᴇɴᴇᴡ ᴠʟ ","renew-vless")],
[Button.inline("‹ ᴍᴀɪɴ ᴍᴇɴᴜ ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**⚜️           ᴠʟᴇss ᴍᴀɴᴀɢᴇʀ               ⚜️**
━━━━━━━━━━━━━━━━━━━━━━━ 
🔰sᴇʀᴠɪᴄᴇ:** `VLESS`
🔰ᴅᴏᴍᴀɪɴ :** `{DOMAIN}`
🔰ɪsᴘ:** `{z["isp"]}`
🔰ᴄᴏᴜɴᴛʀʏ:** `{z["country"]}`
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await vless_(event)
	else:
		await event.answer("Access Denied",alert=True)
