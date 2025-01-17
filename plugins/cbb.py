#Coded by @Its_Tartaglia_Childe

from pyrogram import Client 
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text = f"<b>Bot Cammands\n❏ Commands For BOT Admins\n├/start : start the bot or get posts\n├/batch : Create Group Message\n├/genlink : create link for one post\n├/users : view bot statistics\n├/broadcast : broadcast Message\n└/stats : checking your bot uptime\n\nMaintained by Team @AnimeSigma</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Close ❌", callback_data="close"),
                        InlineKeyboardButton("⚡ About ⚡", callback_data="about")
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text = f"<b>Hi there this is a file store bot which is convert any file to link...\nthen you can access this file through a specific link...!\n\nBot Owner - @Vedant_vn\nOngoing Channel - @Ongoing_AnimeSigma\nChat Group - @Anime_Sigma</a>\n\n👨‍💻 Maintained by Team @AnimeSigma</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Close ❌", callback_data="close"),
                        InlineKeyboardButton("🤖 Help Section 🤖", callback_data="help")
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
