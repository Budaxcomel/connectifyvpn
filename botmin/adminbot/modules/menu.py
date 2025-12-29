from adminbot import *

@bot.on(events.NewMessage(pattern=r"(?:.menu|/menu)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def menu(event):
	inline = [
[Button.inline(" ssʜ ᴍᴇɴᴜ ","ssh")],
[Button.inline(" ᴠᴍᴇss ᴍᴇɴᴜ ","vmess"),
Button.inline(" ᴠʟᴇss ᴍᴇɴᴜ ","vless")],
[Button.inline(" ᴛʀᴏᴊᴀɴ ᴍᴇɴᴜ ","trojan"),
Button.inline(" shadows ᴍᴇɴᴜ ","shadowsocks")],
[Button.inline(" ɪɴғᴏ sᴇʀᴠɪᴄᴇ ᴠᴘs ","info"),
Button.inline(" sᴇᴛᴛɪɴɢ ᴍᴇɴᴜ ","setting")],
[Button.url(" Telegram Grup ","https://t.me/abgdinur")]]
	sender = await event.get_sender()
	val = valid(str(sender.id))
	if val == "false":
		try:
			await event.answer("Not Access ❌", alert=True)
		except:
			await event.reply("Not Access❌")
	elif val == "true":
		sh = f' cat /etc/ssh/.ssh.db | grep "###" | wc -l'
		ssh = subprocess.check_output(sh, shell=True).decode("ascii")
		vm = f' cat /etc/vmess/.vmess.db | grep "###" | wc -l'
		vms = subprocess.check_output(vm, shell=True).decode("ascii")
		vl = f' cat /etc/vless/.vless.db | grep "###" | wc -l'
		vls = subprocess.check_output(vl, shell=True).decode("ascii")
		tr = f' cat /etc/trojan/.trojan.db | grep "###" | wc -l'
		trj = subprocess.check_output(tr, shell=True).decode("ascii")
		ss = f' cat /etc/shadowsocks/.shadowsocks.db | grep "###" | wc -l'
		sss = subprocess.check_output(ss, shell=True).decode("ascii")
		sdss = f" cat /etc/os-release | grep -w PRETTY_NAME | head -n1 | sed 's/=//g' | sed 's/PRETTY_NAME//g' | cut -d ' ' -f 1-3 "
		namaos = subprocess.check_output(sdss, shell=True).decode("ascii")
		ipvps = f" curl -s ipv4.icanhazip.com"
		ipsaya = subprocess.check_output(ipvps, shell=True).decode("ascii")
		citsy = f" cat /etc/xray/city"
		city = subprocess.check_output(citsy, shell=True).decode("ascii")
		ver = f" wget -qO- https://github.com/FighterTunnel/tunnel/raw/main/fodder/versi/releases"
		z = subprocess.check_output(ver, shell=True).decode("ascii")
		sc = f""" 
IPVPS=$(curl -s ipv4.icanhazip.com)
Exp=$(wget -qO- https://raw.githubusercontent.com/Budaxcomel/izinvps/ipuk/ip | grep $IPVPS | cut -d ' ' -f 3)
data_server=$(curl -v --insecure --silent https://google.com/ 2>&1 | grep Date | sed -e 's/< Date: //')
date_list=$(date +"%Y-%m-%d" -d "$data_server")
data_ip="https://raw.githubusercontent.com/Budaxcomel/izinvps/ipuk/ip"
d2=$(date -d "$date_list" +"+%s")
d1=$(date -d "$Exp" +"+%s")
dayleft=$(( ($d1 - $d2) / 86400 ))
echo "$dayleft"
"""
		g = subprocess.check_output(sc, shell=True).decode("ascii")


		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**⟨⚜️         ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ ᴍᴇɴᴜ         ⚜️⟩**
━━━━━━━━━━━━━━━━━━━━━━━ 
**» SYS OS :** `{namaos.strip().replace('"','')}`
**» CITY :** `{city.strip()}`
**» DOMAIN :** `{DOMAIN}`
**» IP VPS :** `{ipsaya.strip()}`
**» EXP SC :** `{g.strip()} Day left`

          **⨳ Total Account Created ⨳**           
** 🔰SSH OVPN    :** `{ssh.strip()}` __account__
** 🔰XRAY VMESS  :** `{vms.strip()}` __account__
** 🔰️XRAY VLESS  :** `{vls.strip()}` __account__
** 🔰XRAY TROJAN :** `{trj.strip()}` __account__
━━━━━━━━━━━━━━━━━━━━━━━ 
**»👤Owner ** `@{sender.username}` 
**»🤖Bot Version  ** V1.8

"""
		x = await event.edit(msg,buttons=inline)
		if not x:
			await event.reply(msg,buttons=inline)

