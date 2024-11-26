from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Привіт {update.effective_user.first_name}! Це бот калькулятор. Я вмію вирішувати прості арифметичні вирази, наприклад 3+5")

async def text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text
    result = 0
    if '+' in txt:
        arr = txt.split('+')
        result = int(arr[0]) + int(arr[1])
    elif '-' in txt:
        arr = txt.split('-')
        result = int(arr[0]) - int(arr[1])
    elif '*' in txt:
        arr = txt.split('*')
        result = int(arr[0]) * int(arr[1])
    elif '/' in txt:
        arr = txt.split('/')
        if int(arr[1]) == 0:
            result = "На ноль ділити не можна!!!"
        else:
            result = int(arr[0]) / int(arr[1])

    await update.message.reply_text(txt + '=' + str(result))


app = ApplicationBuilder().token("token").build() # !!!!!!!!!!!
app.add_handler(CommandHandler("help", help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text))

app.run_polling()