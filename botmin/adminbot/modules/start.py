from adminbot import *

@bot.on(events.NewMessage(pattern=r"(?:.start|/start)$"))
@bot.on(events.CallbackQuery(data=b'start'))
async def start(event):
	inline = [
[Button.inline("PANEL CREATE ACCOUNT","menu")],
[Button.url("TELEGRAM GROUP","https://t.me/abgdinur"),
Button.url("ORDER SCRIPT","https://t.me/ConnectifyVPNBot")]]
	sender = await event.get_sender()
	val = valid(str(sender.id))
	if val == "false":
		try:
			await event.answer("Akses Ditolak", alert=True)
		except:
			await event.reply("Akses Ditolak")
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
		ver = f" wget -qO- https://github.com/Budaxcomel/permission/raw/main/version"
		z = subprocess.check_output(ver, shell=True).decode("ascii")
		sc = f""" 
IPVPS=$(curl -s ipv4.icanhazip.com)
Exp=$(wget -qO-  | grep $IPVPS | cut -d ' ' -f 3)
data_server=$(curl -v --insecure --silent https://google.com/ 2>&1 | grep Date | sed -e 's/< Date: //')
date_list=$(date +"%Y-%m-%d" -d "$data_server")
data_ip=""
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
━━━━━━━━━━━━━━━━━━━━━━━
**»👤Owner ** `@{sender.username}` 
**»🤖Bot Version  ** V2.0
"""
		x = await event.edit(msg,buttons=inline)
		if not x:
			await event.reply(msg,buttons=inline)



