from telegram import Update
from telegram.ext import *
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    pipeline,
    logging,
)
import torch
import asyncio
from transformers import AutoModelForCausalLM
from peft import LoraConfig, PeftModel

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("DeadArcadiy/AlfaLLM_FINAL",
                                             low_cpu_mem_usage=True,
                                             return_dict=True,
                                             torch_dtype=torch.float16,)

tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"
logging.set_verbosity(logging.CRITICAL)

pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=80)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я бот Альфа Банка, который ответит на ваши вопросы. Учтите что время генерации ответа может достигать 10 минут, а ответы могут быть короткими.')

async def reply_to_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Генерирует ответ на полученное текстовое сообщение."""
    user_message = update.message.text
    print("Generating")
    result = pipe(f"<s>[INST] {user_message} [/INST]")
    print("Done")
    await update.message.reply_text(result[0]['generated_text'])

if __name__ == '__main__':
    TOKEN = None

    with open("token.txt") as f:
        TOKEN = f.read().strip()

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_to_text))

    print('Bot is up')

    application.run_polling(0.1)
