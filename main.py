import os
import telebot
import pytesseract
import requests
from PIL import Image
from io import BytesIO
import g4f
from dotenv import load_dotenv
from datetime import datetime

# 🔐 Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# 📊 Log user activity
def log_user_action(username, action):
    with open("user_logs.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] @{username} - {action}\n")

print("✅ Public MCQ Solver Bot is live.")

# ✅ Welcome message for any kind of text (including /start)
@bot.message_handler(func=lambda m: True, content_types=['text'])
def handle_text(message):
    log_user_action(message.from_user.username, f"Text: {message.text}")
    bot.reply_to(message, "📸 Send me your MCQ question image.")

# 📷 Handle MCQ image
@bot.message_handler(content_types=['photo'])
def handle_image(message):
    log_user_action(message.from_user.username, "Sent photo")
    print(f"📥 Image from @{message.from_user.username}")

    bot.reply_to(message, "🧠 Solving your MCQ...")

    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        img_data = requests.get(
            f'https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}'
        ).content
        img = Image.open(BytesIO(img_data))

        extracted = pytesseract.image_to_string(img)
        print("🧾 OCR Output:\n", extracted)

        prompt = (
            "You are an expert in DSA and CS Fundamentals.\n"
            f"Question:\n{extracted}\n"
            "Give only the correct option (A/B/C/D) without explanation."
        )

        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=[{"role": "user", "content": prompt}]
        )

        print("✅ GPT Reply:", response)
        bot.reply_to(message, f"✅ Answer: {response.strip()}")

    except Exception as e:
        print("❌ Error:", e)
        bot.reply_to(message, f"❌ Failed: {e}")

# 🔁 Start polling
bot.polling()
