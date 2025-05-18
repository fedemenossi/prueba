from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot de Telegram.")

if __name__ == '__main__':
    import os

    # Token del bot
    TOKEN = "123456789:ABCdefGHIjklMNOpqrSTUvwxYZ"
    # Pegá aquí tu token de BotFather

    # Crear la aplicación
    app = ApplicationBuilder().token(TOKEN).build()

    # Agregar manejador para el comando /start
    app.add_handler(CommandHandler("start", start))

    # Ejecutar el bot
    app.run_polling()
