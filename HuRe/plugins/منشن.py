# By Reda for HuRe
# Tel: @rd0r0
# شعندك داخل للملف تريد تخمطة ههههههههه اخمط ونسبة لنفسك ماوصيك :*
from HuRe import l313l
import asyncio
from ..core.managers import edit_or_reply
from telethon import events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

spam_chats = []

@l313l.ar_cmd(pattern="منشن(?:\s|$)([\s\S]*)")
async def menall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await edit_or_reply(event, "** ᯽︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
    msg = event.pattern_match.group(1)
    if not msg:
        return await edit_or_reply(event, "** ᯽︙ ضع رسالة للمنشن اولاً**")
    is_admin = False
    try:
        partici_ = await l313l(GetParticipantRequest(
          event.chat_id,
          event.sender_id
        ))
    except UserNotParticipantError:
        is_admin = False
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ''
    async for usr in l313l.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrtxt = f"{msg}\n[{usr.first_name}](tg://user?id={usr.id}) "
        await l313l.send_message(chat_id, usrtxt)
        await asyncio.sleep(2)
        await event.delete()
    try:
        spam_chats.remove(chat_id)
    except:
        pass
@l313l.ar_cmd(pattern="الغاء منشن")
async def ca_sp(event):
  if not event.chat_id in spam_chats:
    return await edit_or_reply(event, "** ᯽︙ 🤷🏻 لا يوجد منشن لألغائه**")
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await edit_or_reply(event, "** ᯽︙ تم الغاء المنشن بنجاح ✓**")
@l313l.ar_cmd(pattern="تاكك(?:\s|$)([\s\S]*)")
async def Hussein(event):
    chat = await event.get_chat()
    async for member in l313l.iter_participants(chat):
        mention = f"[{member.first_name}](tg://user?id={member.id})"
        try:
            await l313l.send_message(event.chat_id, mention, reply_to=event.reply_to_msg_id)
        except Exception as e:
            print(f"حدث خطأ أثناء الإرسال: {e}")
    await event.delete()
