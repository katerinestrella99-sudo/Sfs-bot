import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

TOKEN=os.environ.get("TOKEN")
logging.basicConfig(level=logging.INFO)

async def start(update, context):
 keyboard=[
 [InlineKeyboardButton("1 SFS x SFS",callback_data='1')],
 [InlineKeyboardButton("3 SFS Historia",callback_data='3')],
 [InlineKeyboardButton("5 Like x Like",callback_data='5')],
 [InlineKeyboardButton("7 SFS VIP",callback_data='7')],
 [InlineKeyboardButton("9 Reglas",callback_data='9')],
 [InlineKeyboardButton("11 Mi Canal",callback_data='11')],
 ]
 await update.message.reply_text("Bienvenida a Sfs-bot! Elige:",reply_markup=InlineKeyboardMarkup(keyboard))

async def buttons(update, context):
 q=update.callback_query
 await q.answer()
 await q.edit_message_text(f"Opcion {q.data} elegida!")

def main():
 app=Application.builder().token(TOKEN).build()
 app.add_handler(CommandHandler("start",start))
 app.add_handler(CallbackQueryHandler(buttons))
 app.run_polling()

if __name__=="__main__":
 main()
