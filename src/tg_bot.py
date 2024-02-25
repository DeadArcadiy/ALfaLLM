from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from transformers import pipeline

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот Альфа Банка, который ответит на ваши вопросы')

def reply_to_text(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    # Генерация ответа моделью
    model_response = pipe(f"<s>[INST] {user_message} [/INST]")
    update.message.reply_text(model_response)


if __name__ == '__main__':
    pipe = pipeline("text-generation", model="DeadArcadiy/AlfaLLM_FINAL")
   
    TOKEN = None

    with open("../token.txt") as f:
       TOKEN = f.read().strip()

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, reply_to_text))

    updater.start_polling()
    updater.idle()
