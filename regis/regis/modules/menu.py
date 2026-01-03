from regis import *
import os

def _get_permission_url() -> str:
    conf = "/etc/connectifyvpn/permission.conf"
    if os.path.isfile(conf):
        for line in open(conf, "r").read().splitlines():
            line = line.strip()
            if line.startswith("PERMISSION_URL="):
                # remove PERMISSION_URL= and surrounding quotes
                val = line.split("=", 1)[1].strip().strip('"').strip("'")
                return val
    return ""

@bot.on(events.NewMessage(pattern=r"(?:\.regis|/regis|/start)$"))
@bot.on(events.CallbackQuery(data=b"menu"))
async def menu(event):
    inline = [
        [Button.inline(" DAFTAR ", b"registrasi"), Button.inline(" PADAM ", b"deleteip")],
        [Button.url(" Join Grup ", "https://t.me/connectifyvpn")],
    ]
    sender = await event.get_sender()
    val = valid(str(sender.id))
    if val == "false":
        try:
            await event.answer("Akses ditolak", alert=True)
        except Exception:
            await event.reply("Akses ditolak")
        return

    perm_url = _get_permission_url()
    if perm_url:
        sh = f'curl -fsSL "{perm_url}" | grep -vE "^[[:space:]]*#" | grep -vE "^[[:space:]]*$" | wc -l'
        try:
            total = subprocess.check_output(sh, shell=True).decode("ascii").strip()
        except Exception:
            total = "?"
    else:
        total = "?"

    msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━
**☘️ PENDAFTARAN IP AUTO SCRIPT ☘️**
━━━━━━━━━━━━━━━━━━━━━━━
Hai {sender.first_name}
**Jumlah pelanggan:** `{total}`
"""
    x = await event.edit(msg, buttons=inline)
    if not x:
        await event.reply(msg, buttons=inline)
