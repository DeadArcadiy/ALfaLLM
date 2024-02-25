from telegram import Update
from telegram.ext import *
from transformers import pipeline,BitsAndBytesConfig
import torch
import asyncio

pipe = pipeline("text-generation", model="DeadArcadiy/AlfaLLM_FINAL",torch_dtype=torch.bfloat16, device_map={"": 0})

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я бот Альфа Банка, который ответит на ваши вопросы')

async def reply_to_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Генерирует ответ на полученное текстовое сообщение."""
    user_message = update.message.text
    # Генерация ответа моделью
    model_response = pipe(f"<s>[INST] {user_message} [/INST]")
    await update.message.reply_text(model_response)

if __name__ == '__main__':
  TOKEN = None

  with open("token.txt") as f:
      TOKEN = f.read().strip()

  application = ApplicationBuilder().token(TOKEN).build()

  application.add_handler(CommandHandler("start", start))
  application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_to_text))


  application.run_polling(0.1)
