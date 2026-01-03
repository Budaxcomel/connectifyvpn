from regis import *
import os

@bot.on(events.CallbackQuery(data=b"registrasi"))
async def registrasii(event):
    async def registrasii_(event):
        chat = event.chat_id
        sender = await event.get_sender()

        async with bot.conversation(chat) as conv:
            await event.respond("**Nama pengguna:**")
            user_ev = conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user_ev).raw_text

            await event.respond("**Masukkan IP VPS:**")
            ip_ev = conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            ip_vps = (await ip_ev).raw_text

            await event.respond(
                "**Tempoh Tamat (hari):**",
                buttons=[
                    [Button.inline(" 30 Hari ", b"30"), Button.inline(" 60 Hari ", b"60")],
                    [Button.inline(" 90 Hari ", b"90"), Button.inline(" 360 Hari ", b"360")],
                ],
            )
            exp_ev = conv.wait_event(events.CallbackQuery)
            days = (await exp_ev).data.decode("ascii")

        shell_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "shell")
        script = os.path.join(shell_dir, "bot-registrasi")
        cmd = f'printf "%s\n" "{user}" "{ip_vps}" "{days}" | bash "{script}"'
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
        await registrasii_(event)
    else:
        await event.answer("Akses ditolak", alert=True)
