from adminbot import *

@bot.on(events.CallbackQuery(data=b'delete-ssh'))
async def delete_ssh(event):
	async def delete_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ:**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
			cmd = f'printf "%s\n" "{user}" | delssh-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User** `{user}` **ɴᴏᴛ ғᴏᴜɴᴅ**")
		else:
			await event.respond(f"**sᴜᴄᴄᴇssғᴜʟʏ ᴅᴇʟᴇᴛᴇᴅ** `{user}`")
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_ssh_(event)
	else:
		await event.answer("ᴀᴋsᴇs ᴅɪᴛᴏʟᴀᴋ",alert=True)

@bot.on(events.CallbackQuery(data=b'create-ssh'))
async def create_ssh(event):
	async def create_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**ᴜsᴇʀɴᴀᴍᴇ:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**ᴘᴀssᴡᴏʀᴅ:**")
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
		cmd = f'printf "%s\n" "{user}" "{pw}" "{exp}" | addssh'
		try:
			subprocess.check_output(cmd,shell=True)
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**     ssʜ ᴏᴠᴘɴ ᴀᴄᴄᴏᴜɴᴛ **
**◇━━━━━━━━━━━━━━━━━◇**
**» ᴜsᴇʀɴᴀᴍᴇ         :** `{user.strip()}`
**» ᴘᴀssᴡᴏʀᴅ         :** `{pw.strip()}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʜᴏsᴛ             :** `{DOMAIN}`
**» ᴘᴏʀᴛ ᴏᴘᴇɴssʜ     :** `443, 80, 22`
**» ᴘᴏʀᴛ ᴅʀᴏᴘʙᴇᴀʀ    :** `443, 109`
**» ᴘᴏʀᴛ ᴅʀᴏᴘʙᴇᴀʀ ᴡs :** `443, 109`
**» ᴘᴏʀᴛ ssʜ ᴡs      :** `80, 8080, 8081-9999 `
**» ᴘᴏʀᴛ ssʜ ssʟ ᴡs  :** `443`
**» ᴘᴏʀᴛ ssʟ/ᴛʟs     :** `222-1000`
**» ᴘᴏʀᴛ ᴏᴠᴘɴ ᴡs ssʟ :** `443`
**» ᴘᴏʀᴛ ᴏᴠᴘɴ ssʟ    :** `443`
**» ᴘᴏʀᴛ ᴏᴠᴘɴ ᴛᴄᴘ    :** `443, 1194`
**» ᴘᴏʀᴛ ᴏᴠᴘɴ ᴜᴅᴘ    :** `2200`
**» ᴘᴏʀᴛ ᴜᴅᴘ ᴄᴜsᴛᴏᴍ   :** `1-65535`
**» ᴘʀᴏxʏ sǫᴜɪᴅ      :** `3128`
**» ʙᴀᴅᴠᴘɴ ᴜᴅᴘ       :** `7100, 7300, 7300`
**◇━━━━━━━━━━━━━━━━━◇**
**» ᴘᴀʏʟᴏᴀᴅ ᴡss      :** `GET wss://BUG.COM/ HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Upgrade: websocket[crlf][crlf]`
**◇━━━━━━━━━━━━━━━━━◇**
**» ᴇxᴘɪʀᴇᴅ ᴜɴᴛɪʟ:** `{later}`
**◇━━━━━━━━━━━━━━━━━◇**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_ssh_(event)
	else:
		await event.answer("ᴀᴋsᴇs ᴅɪᴛᴏʟᴀᴋ",alert=True)

@bot.on(events.CallbackQuery(data=b'show-ssh'))
async def show_ssh(event):
	async def show_ssh_(event):
		cmd = 'bot-member-ssh'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""
```
{z}
```
**sʜᴏᴡ ᴀʟʟ ssʜ ᴜsᴇʀ**
""",buttons=[[Button.inline("‹ ᴍᴀɪɴ ᴍᴇɴᴜ ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await show_ssh_(event)
	else:
		await event.answer("ᴀᴄᴄᴇss ᴅᴇɴɪᴇᴅ",alert=True)



@bot.on(events.CallbackQuery(data=b'trial-ssh'))
async def trial_ssh(event):
	async def trial_ssh_(event):
		user = "trialX"+str(random.randint(100,1000))
		pw = "1"
		exp = "1"
		cmd = f'useradd -e `date -d "{exp} days" +"%Y-%m-%d"` -s /bin/false -M {user} && echo "{pw}\n{pw}" | passwd {user} | echo "killtrial ssh {user}" | at now +60 minutes &> /dev/null'
		try:
			subprocess.check_output(cmd,shell=True)
		except:
			await event.respond("**ᴜsᴇʀ ᴀʟʀᴇᴅʏ ᴇxɪs**")
		else:
			#today = DT.date.today()
			#later = today + DT.timedelta(days=int(exp))
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**   ssʜ ᴏᴠᴘɴ ᴀᴄᴄᴏᴜɴᴛ **
**◇━━━━━━━━━━━━━━━━━◇**
**» ᴜsᴇʀɴᴀᴍᴇ         :** `{user.strip()}`
**» ᴘᴀssᴡᴏʀᴅ         :** `{pw.strip()}`
**◇━━━━━━━━━━━━━━━━━◇**
**» ʜᴏsᴛ             :** `{DOMAIN}`
**» ᴘᴏʀᴛ ᴏᴘᴇɴssʜ     :** `443, 80, 22`
**» ᴘᴏʀᴛ ᴅʀᴏᴘʙᴇᴀʀ    :** `443, 109`
**» ᴘᴏʀᴛ ᴅʀᴏᴘʙᴇᴀʀ ᴡs :** `443, 109`
**» ᴘᴏʀᴛ ssʜ ᴡs      :** `80, 8080, 8081-9999 `
**» ᴘᴏʀᴛ ssʜ ssʟ ᴡs  :** `443`
**» ᴘᴏʀᴛ ssʟ/ᴛʟs     :** `222-1000`
**» ᴘᴏʀᴛ ᴏᴠᴘɴ ᴡs ssʟ :** `443`
**» ᴘᴏʀᴛ ᴏᴠᴘɴ ssʟ    :** `443`
**» ᴘᴏʀᴛ ᴏᴠᴘɴ ᴛᴄᴘ    :** `443, 1194`
**» ᴘᴏʀᴛ ᴏᴠᴘɴ ᴜᴅᴘ    :** `2200`
**» ᴘᴏʀᴛ ᴜᴅᴘ ᴄᴜsᴛᴏᴍ   :** `1-65535`
**» ᴘʀᴏxʏ sǫᴜɪᴅ      :** `3128`
**» ʙᴀᴅᴠᴘɴ ᴜᴅᴘ       :** `7100, 7300, 7300`
**◇━━━━━━━━━━━━━━━━━◇**
**» ᴘᴀʏʟᴏᴀᴅ ᴡss      :** `GET wss://BUG.COM/ HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Upgrade: websocket[crlf][crlf]`
**◇━━━━━━━━━━━━━━━━━◇**
**» ᴇxᴘɪʀᴇᴅ ᴜɴᴛɪʟ:** `60 ᴍɪɴᴜᴛᴇs`
**◇━━━━━━━━━━━━━━━━━◇**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_ssh_(event)
	else:
		await event.answer("ᴀᴋsᴇs ᴅɪᴛᴏʟᴀᴋ",alert=True)
		
@bot.on(events.CallbackQuery(data=b'login-ssh'))
async def login_ssh(event):
	async def login_ssh_(event):
		cmd = 'bot-cek-login-ssh'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""

{z}

**sʜᴏᴡs ʟᴏɢɢᴇᴅ ɪɴ ᴜsᴇʀs ssʜ ᴏᴠᴘɴ**
""",buttons=[[Button.inline("‹ ᴍᴀɪɴ ᴍᴇɴᴜ ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await login_ssh_(event)
	else:
		await event.answer("ᴀᴄᴄᴇss ᴅᴇɴɪᴇᴅ",alert=True)


@bot.on(events.CallbackQuery(data=b'ssh'))
async def ssh(event):
	async def ssh_(event):
		inline = [
[Button.inline(" ᴛʀɪᴀʟ ssʜ ","trial-ssh")],
[Button.inline(" ᴄʀᴇᴀᴛᴇ ssʜ ","create-ssh"),
Button.inline(" ᴅᴇʟᴇᴛᴇ ssʜ ","delete-ssh")],
[Button.inline(" ᴄʜᴇᴄᴋ ssʜ ","login-ssh"),
Button.inline(" ᴍᴇᴍʙᴇʀ ssʜ ","show-ssh")],
[Button.inline("‹ ᴍᴀɪɴ ᴍᴇɴᴜ ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**⚜️          ssʜ ᴏᴠᴘɴ ᴍᴀɴᴀɢᴇʀ            ⚜️**
━━━━━━━━━━━━━━━━━━━━━━━ 
**» 🔰sᴇʀᴠɪᴄᴇ:** `SSH OVPN`
**» 🔰ᴅᴏᴍᴀɪɴ :** `{DOMAIN}`
**» 🔰ɪsᴘ:** `{z["isp"]}`
**» 🔰ᴄᴏᴜɴᴛʀʏ:** `{z["country"]}`
━━━━━━━━━━━━━━━━━━━━━━━ 
**»👤Owner ** `@{sender.username}` 
**»🤖Bot Version  ** V2.0
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await ssh_(event)
	else:
		await event.answer("ᴀᴄᴄᴇss ᴅᴇɴɪᴇᴅ",alert=True)
