from adminbot import *

#CRATE VMESS
@bot.on(events.CallbackQuery(data=b'create-vmess'))
async def create_vmess(event):
	async def create_vmess_(event):
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
		cmd = f'printf "%s\n" "{user}" "{exp}" "{pw}" | addws-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			b = [x.group() for x in re.finditer("vmess://(.*)",a)]
#			c = [x.group() for x in re.finditer("Host XrayDNS(.*)",a)]
#			d = [x.group() for x in re.finditer("Pub Key(.*)",a)]
			print(b)
#			print(d)
#			print(c)
#			xx = re.search("Pub Key      :(.*)",d[0]).group(1)
#			xxx = re.search("Host XrayDNS :(.*)",d[0]).group(1)
			z = base64.b64decode(b[0].replace("vmess://","")).decode("ascii")
			z = json.loads(z)
			z1 = base64.b64decode(b[1].replace("vmess://","")).decode("ascii")
			z1 = json.loads(z1)
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**  xʀᴀʏ/ᴠᴍᴇss ᴀᴄᴄᴏᴜɴᴛ **
**◇━━━━━━━━━━━━━━━━━◇**
**» ʀᴇᴍᴀʀᴋs      :** `{z["ps"]}`
**» ᴅᴏᴍᴀɪɴ       :** `{z["add"]}`
**» ᴜsᴇʀ ʟɪᴍɪᴛ ɢʙ   :** `{pw} GB`
**» ᴘᴏʀᴛ ᴛʟs     :** `443`
**» ᴘᴏʀᴛ ɴᴏɴᴛʟs    :** `80, 8080, 8081-9999`
**» ᴘᴏʀᴛ ɢʀᴘᴄ    :** `443`
**» ᴜsᴇʀ ɪᴅ      :** `{z["id"]}`
**» ᴀʟᴛᴇʀɪᴅ      :** `0`
**» sᴇᴄᴜʀɪᴛʏ     :** `auto`
**» ɴᴇᴛᴡᴏʀᴋ      :** `(WS) or (gRPC)`
**» ᴘᴀᴛʜ ᴛʟs     :** `bug.com/vmess`
**» ᴘᴀᴛʜ ɴʟs     :** `bug.com/vmess`
**» ᴘᴀᴛʜ ᴅʏɴᴀᴍɪᴄ :** `http://BUG.COM`
**» sᴇʀᴠɪᴄᴇɴᴀᴍᴇ  :** `vmess-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴛʟs     :** 
`{b[0].strip("'").replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ɴᴛʟs    :** 
`{b[1].strip("'").replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ɢʀᴘᴄ    :** 
`{b[2].strip("'")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴊsᴏɴ  :** `https://${DOMAIN}:81/vmess-{user}.txt`
**◇━━━━━━━━━━━━━━━━━◇**
**» ᴇxᴘɪʀᴇᴅ ᴜɴᴛɪʟ:** `{later}`
**◇━━━━━━━━━━━━━━━━━◇**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

# TRIAL VMESS
@bot.on(events.CallbackQuery(data=b'trial-vmess'))
async def trial_vmess(event):
	async def trial_vmess_(event):
		cmd = f'printf "%s\n"| trialws-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			b = [x.group() for x in re.finditer("vmess://(.*)",a)]
			print(b)
			z = base64.b64decode(b[0].replace("vmess://","")).decode("ascii")
			z = json.loads(z)
			z1 = base64.b64decode(b[1].replace("vmess://","")).decode("ascii")
			z1 = json.loads(z1)
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
** xʀᴀʏ/ᴠᴍᴇss ᴀᴄᴄᴏᴜɴᴛ **
**◇━━━━━━━━━━━━━━━━━◇**
**» ʀᴇᴍᴀʀᴋ      :** `{z["ps"]}`
**» ᴅᴏᴍᴀɪɴ       :** `{z["add"]}`
**» ᴘᴏʀᴛ ᴛʟs     :** `443`
**» ᴘᴏʀᴛ ɴᴏɴᴛʟs    :** `80, 8080, 8081-9999`
**» ᴘᴏʀᴛ ɢʀᴘᴄ    :** `443`
**» ᴜsᴇʀ ɪᴅ      :** `{z["id"]}`
**» ᴀʟᴛᴇʀɪᴅ      :** `0`
**» sᴇᴄᴜʀɪᴛʏ     :** `auto`
**» ɴᴇᴛᴡᴏʀᴋ      :** `(WS) or (gRPC)`
**» ᴘᴀᴛʜ ᴛʟs     :** `bug.com/vmess`
**» ᴘᴀᴛʜ ɴʟs     :** `bug.com/vmess`
**» ᴘᴀᴛʜ ᴅʏɴᴀᴍɪᴄ :** `http://BUG.COM`
**» sᴇʀᴠɪᴄᴇɴᴀᴍᴇ  :** `vmess-grpc`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴛʟs     :** 
`{b[0].strip("'").replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ɴᴛʟs    :** 
`{b[1].strip("'").replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ɢʀᴘᴄ    :** 
`{b[2].strip("'")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʟɪɴᴋ ᴊsᴏɴ  :** `https://${DOMAIN}:81/vmess-{user}.txt`
**◇━━━━━━━━━━━━━━━━━◇**
**» ᴇxᴘɪʀᴇᴅ ᴜɴᴛɪʟ:** `60 Minutes`
**◇━━━━━━━━━━━━━━━━━◇**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

#CEK VMESS
@bot.on(events.CallbackQuery(data=b'cek-vmess'))
async def cek_vmess(event):
	async def cek_vmess_(event):
		cmd = 'bot-cek-ws'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""

{z}

**Shows Logged In Users Vmess**
""",buttons=[[Button.inline("‹ ᴍᴀɪɴ ᴍᴇɴᴜ ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await cek_vmess_(event)
	else:
		await event.answer("Access Denied",alert=True)

@bot.on(events.CallbackQuery(data=b'delete-vmess'))
async def delete_vmess(event):
	async def delete_vmess_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**ᴜsᴇʀɴᴀᴍᴇ:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		cmd = f'printf "%s\n" "{user}" | delws-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Not Found**")
		else:
			msg = f"""**Successfully Deleted {user} **"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'renew-vmess'))
async def ren_vmess(event):
	async def ren_vmess_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**ᴜsᴇʀɴᴀᴍᴇ:**')
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
		cmd = f'printf "%s\n" "{user}" {exp}| renewws-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Not Found**")
		else:
			msg = f"""**Successfully Renewed  {user} {exp} Days**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await ren_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'vmess'))
async def vmess(event):
	async def vmess_(event):
		inline = [
[Button.inline(" ᴛʀɪᴀʟ ᴠᴍ ","trial-vmess")],
[Button.inline(" ᴄʀᴇᴀᴛᴇ ᴠᴍ ","create-vmess"),
Button.inline(" ᴄʜᴇᴄᴋ ᴠᴍ ","cek-vmess")],
[Button.inline(" ᴅᴇʟᴇᴛᴇ ᴠᴍ ","delete-vmess"),
Button.inline(" ʀᴇɴᴇᴡ ᴠᴍ ","renew-vmess")],
[Button.inline("‹ ᴍᴀɪɴ ᴍᴇɴᴜ ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**⚜️           ᴠᴍᴇss ᴍᴀɴᴀɢᴇʀ               ⚜️**
━━━━━━━━━━━━━━━━━━━━━━━ 
🔰sᴇʀᴠɪᴄᴇ:** `VMESS`
🔰ᴅᴏᴍᴀɪɴ :** `{DOMAIN}`
🔰ɪsᴘ:** `{z["isp"]}`
🔰ᴄᴏᴜɴᴛʀʏ:** `{z["country"]}`
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await vmess_(event)
	else:
		await event.answer("Access Denied",alert=True)
