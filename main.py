import os
import telebot
import pytesseract
import requests
from PIL import Image
from io import BytesIO
import g4f
from dotenv import load_dotenv

# 🔐 Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

print("✅ Bot is live...")

# Greet and/or process image on any message
@bot.message_handler(func=lambda message: True, content_types=['text', 'photo'])
def handle_user_message(message):
    bot.send_message(message.chat.id, "👋 Welcome to Sakshi's *MCQ_PRO_BOT*", parse_mode='Markdown')
    bot.send_message(message.chat.id, "📸 Please send me the *image* of your MCQ question.")

    if message.content_type == 'photo':
        try:
            bot.send_message(message.chat.id, "🧠 Processing your MCQ...")

            file_info = bot.get_file(message.photo[-1].file_id)
            img_data = requests.get(f'https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}').content
            img = Image.open(BytesIO(img_data))

            extracted = pytesseract.image_to_string(img)
            print("🧾 OCR Output:\n", extracted)

            prompt = (
                "You are an expert in computer science and engineering MCQs.\n"
                f"Question:\n{extracted}\n"
                "Give only the correct option (A/B/C/D) without explanation."
            )

            response = g4f.ChatCompletion.create(
                model=g4f.models.default,
                messages=[{"role": "user", "content": prompt}]
            )

            bot.send_message(message.chat.id, f"✅ Answer: {response.strip()}")

        except Exception as e:
            bot.send_message(message.chat.id, f"❌ Failed to process image: {e}")
