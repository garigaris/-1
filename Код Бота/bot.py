from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "8139542567:AAExX0FgokW8DcmL3B0izSdBUcR0QPzB1Gg"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Я ваш Telegram-бот. Используйте /help для списка команд.")

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Доступные команды:\n/start - Запустить бота\n/help - Получить список команд")

async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(update.message.text)

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
