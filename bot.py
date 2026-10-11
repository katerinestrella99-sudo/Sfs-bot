import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
TOKEN="AQUI_VA_TU_TOKEN"
logging.basicConfig(level=logging.INFO)
async def start(update, context):
 keyboard=[
 [InlineKeyboardButton("1 SFS x SFS",callback_data='1'),InlineKeyboardButton("2 SFS 24H",callback_data='2')],
 [InlineKeyboardButton("3 SFS Historia",callback_data='3'),InlineKeyboardButton("4 SFS Post",callback_data='4')],
 [InlineKeyboardButton("5 Like x Like",callback_data='5'),InlineKeyboardButton("6 Comenta",callback_data='6')],
 [InlineKeyboardButton("7 SFS VIP",callback_data='7'),InlineKeyboardButton("8 Premium",callback_data='8')],
 [InlineKeyboardButton("9 Reglas",callback_data='9'),InlineKeyboardButton("10 Precios",callback_data='10')],
 [InlineKeyboardButton("11 Mi Canal",callback_data='11'),InlineKeyboardButton("12 Contacto",callback_data='12')]]
 await update.message.reply_text("Bienvenida a Sfs-bot! Elige:",reply_markup=InlineKeyboardMarkup(keyboard))
async def buttons(update, context):
 q=update.callback_query
 await q.answer()
 await q.edit_message_text(f"Opcion {q.data}")
def main():
 app=Application.builder().token(TOKEN).build
