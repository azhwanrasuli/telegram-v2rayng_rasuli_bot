from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8109661657:AAFMj8VDeS9tbV52ZVsj4lUQhabBhtYWUfE"
MY_LINK = "https://t.me/v2rayng_rasuli_bot"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = InlineKeyboardButton("رفتن به لینک", url=MY_LINK)
    keyboard = InlineKeyboardMarkup([[button]])

    await update.message.reply_text(
        "سلام! برای دیدن لینک، روی دکمه زیر کلیک کن 👇",
        reply_markup=keyboard
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
