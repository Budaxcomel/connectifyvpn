from adminbot import *

@bot.on(events.CallbackQuery(data=b'create-shadowsocks'))
async def create_shadowsocks(event):
	async def create_shadowsocks_(event):
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
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(3)
		await event.edit("`Processing Crate Premium Account`")
		time.sleep(1)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(2)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(3)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(2)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "{user}" "{exp}" "{pw}" | addss-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			x = [x.group() for x in re.finditer("ss://(.*)",a)]
			print(x)
			# remarks = re.search("#(.*)",x[0]).group(1)
			# domain = re.search("@(.*?):",x[0]).group(1)
			uuid = re.search("ss://(.*?)@",x[0]).group(1)
			# path = re.search("path=(.*)&",x[0]).group(1)
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**👑  sʜᴅᴡsᴄᴋ ᴀᴄᴄᴏᴜɴᴛ 👑**
**◇━━━━━━━━━━━━━━━━━◇**
**» ʀᴇᴍᴀʀᴋ     :** `{user}`
**» ʜᴏsᴛ sᴇʀᴠᴇʀ :** `{DOMAIN}`
**» ʜᴏsᴛ xʀᴀʏᴅɴs:** `{HOST}`
**» ᴜsᴇʀ ʟɪᴍɪᴛ ɢʙ  :** `Unlimited`
**» ᴘᴜʙ ᴋᴇʏ     :** `{PUB}`
**» ᴘᴏʀᴛ ᴛʟs    :** `222-1000`
**» ᴘᴏʀᴛ ɢʀᴘᴄ   :** `443`
**» ᴘᴏʀᴛ ᴅɴs    :** `443, 53`
**» ᴘᴀssᴡᴏʀᴅ    :** `{uuid}`
**» ᴄɪᴘʜᴇʀ      :** `aes-128-gcm`
**» ɴᴇᴛᴡᴏʀᴋ     :** `(WS) or (gRPC)`
**» ᴘᴀᴛʜ        :** `(/multi path)/ss-ws`
**» sᴇʀᴠɪᴄᴇɴᴀᴍᴇ :** `ss-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴛʟs    :**
`{x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ɢʀᴘᴄ   :** 
`{x[1].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴊsᴏɴ  :** `https://${DOMAIN}:81/ss-{user}.txt`
**◇━━━━━━━━━━━━━━━━━◇**
**» ᴇxғɪʀᴇᴅ ᴜɴᴛɪʟ:** `{later}`
**» 🤖@ᴍʏʀɪᴅᴛᴜɴɴᴇʟ**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_shadowsocks_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'cek-shadowsocks'))
async def cek_shadowsocks(event):
	async def cek_shadowsocks_(event):
		cmd = 'bot-cek-ss'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""

{z}

**Shows Logged In Users Shadowsocks**
**» 🤖@ᴍʏʀɪᴅᴛᴜɴɴᴇʟ**
""",buttons=[[Button.inline("‹ ᴍᴀɪɴ ᴍᴇɴᴜ ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await cek_shadowsocks_(event)
	else:
		await event.answer("Access Denied",alert=True)

@bot.on(events.CallbackQuery(data=b'delete-shadowsocks'))
async def delete_shadowsocks(event):
	async def delete_shadowsocks_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**ᴜsᴇʀɴᴀᴍᴇ:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		cmd = f'printf "%s\n" "{user}" | bot-delss'
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
		await delete_shadowsocks_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'trial-shadowsocks'))
async def trial_shadowsocks(event):
	async def trial_shadowsocks_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**ᴄʜᴏᴏsᴇ ᴇxᴘɪʀʏ ᴍɪɴᴜᴛᴇs**",buttons=[
[Button.inline(" 10 ᴍᴇɴɪᴛ ","10"),
Button.inline(" 15 ᴍᴇɴɪᴛ ","15")],
[Button.inline(" 30 ᴍᴇɴɪᴛ ","30"),
Button.inline(" 60 ᴍᴇɴɪᴛ ","60")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(3)
		await event.edit("`Processing Crate Premium Account`")
		time.sleep(1)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(2)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(3)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(2)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "{exp}" | bot-trialss'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			#today = DT.date.today()
			#later = today + DT.timedelta(days=int(exp))
			x = [x.group() for x in re.finditer("ss://(.*)",a)]
			print(x)
			remarks = re.search("#(.*)",x[0]).group(1)
			# domain = re.search("@(.*?):",x[0]).group(1)
			uuid = re.search("ss://(.*?)@",x[0]).group(1)
			# path = re.search("path=(.*)&",x[0]).group(1)
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**👑  sʜᴅᴡsᴄᴋ ᴀᴄᴄᴏᴜɴᴛ 👑**
**◇━━━━━━━━━━━━━━━━━◇**
**» ʀᴇᴍᴀʀᴋ     :** `{remarks}`
**» ʜᴏsᴛ sᴇʀᴠᴇʀ :** `{DOMAIN}`
**» ʜᴏsᴛ xʀᴀʏᴅɴs:** `{HOST}`
**» ᴜsᴇʀ ʟɪᴍɪᴛ ɢʙ  :** `Unlimited`
**» ᴘᴜʙ ᴋᴇʏ     :** `{PUB}`
**» ᴘᴏʀᴛ ᴛʟs    :** `222-1000`
**» ᴘᴏʀᴛ ɢʀᴘᴄ   :** `443`
**» ᴘᴏʀᴛ ᴅɴs    :** `443, 53`
**» ᴘᴀssᴡᴏʀᴅ    :** `{uuid}`
**» ᴄɪᴘʜᴇʀ      :** `aes-128-gcm`
**» ɴᴇᴛᴡᴏʀᴋ     :** `(WS) or (gRPC)`
**» ᴘᴀᴛʜ        :** `(/multi path)/ss-ws`
**» sᴇʀᴠɪᴄᴇɴᴀᴍᴇ :** `ss-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴛʟs    :**
`{x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ɢʀᴘᴄ   :** 
`{x[1].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴊsᴏɴ  :** `https://${DOMAIN}:81/ss-{remarks}.txt`
**◇━━━━━━━━━━━━━━━━━◇**
**» ᴇxᴘɪʀᴇᴅ ᴜɴᴛɪʟ :** `{exp} Minutes`
**» 🤖@ᴍʏʀɪᴅᴛᴜɴɴᴇʟ**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_shadowsocks_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'shadowsocks'))
async def shadowsocks(event):
	async def shadowsocks_(event):
		inline = [
[Button.inline("✨ ᴛʀɪᴀʟ sʜᴅᴡsᴄsᴋ ✨","trial-shadowsocks"),
Button.inline("✨ ᴄʀᴇᴀᴛᴇ sʜᴅᴡsᴄsᴋ ✨","create-shadowsocks")],
[Button.inline("✨ ᴄᴇᴋ sʜᴅᴡsᴄsᴋ ✨","cek-shadowsocks"),
Button.inline("✨ ᴅᴇʟᴇᴛᴇ sʜᴅᴡsᴄsᴋ ✨","delete-shadowsocks")],
[Button.inline("‹ ᴍᴀɪɴ ᴍᴇɴᴜ ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**👑 sʜᴅᴡsᴄsᴋ ᴍᴀɴᴀɢᴇʀ 👑**
**◇━━━━━━━━━━━━━━━━━◇**
**» 🌶sᴇʀᴠɪᴄᴇ:** `SHADOWSOCKS`
**» 🌺ʜᴏsᴛɴᴀᴍᴇ/ɪᴘ:** `{DOMAIN}`
**» 💎ɪsᴘ:** `{z["isp"]}`
**» 🔥ᴄᴏᴜɴᴛʀʏ:** `{z["country"]}`
**◇━━━━━━━━━━━━━━━━━◇**
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await shadowsocks_(event)
	else:
		await event.answer("Access Denied",alert=True)
