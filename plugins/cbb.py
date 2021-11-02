#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f" <code>Creator         :</code> <a href='t.me/Callmeshackle'>Lord Shackle</a>\n <code>Language        :</code> <code>Python3</code>\n <code>Library         :</code> <a href='https://docs.pyrogram.org/'>Pyrogram {__version__}</a>\n <code>Source Code     :</code> <a href='t.me/CallMeShakle'>Click Here</a>\n <code>Channel         :</code> @Asupanvirall\n <code>Support Group   :</code> @WorldOFsex1",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(" Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass