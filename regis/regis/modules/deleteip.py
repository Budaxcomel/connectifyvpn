from regis import *
import os

@bot.on(events.CallbackQuery(data=b"deleteip"))
async def deleteipp(event):
    async def deleteipp_(event):
        chat = event.chat_id
        sender = await event.get_sender()

        async with bot.conversation(chat) as conv:
            await event.respond("**Masukkan IP VPS:**")
            ip_ev = conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            ip_vps = (await ip_ev).raw_text

        shell_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "shell")
        script = os.path.join(shell_dir, "bot-deleteip")
        cmd = f'printf "%s\n" "{ip_vps}" | bash "{script}"'
        try:
            out = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception:
            await event.respond("**Gagal / tidak wujud**")
        else:
            msg = f"```{out}```\n**» 🤖@connectifyvpn**"
            await event.respond(msg)

    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await deleteipp_(event)
    else:
        await event.answer("Akses ditolak", alert=True)
