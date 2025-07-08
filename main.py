import telebot
import pytesseract
import requests
from PIL import Image
from io import BytesIO
import g4f

# 🔐 Bot Token — paste your real Telegram bot token below
bot = telebot.TeleBot("8016232431:AAF8a81EtZAI1ta-KwSIW1NpJWWJBApQDks")
AUTHORIZED_USER = '@ro_sakshi'  # Change this if needed

print("✅ FREE GPT Bot is live. Waiting for MCQ images...")

@bot.message_handler(content_types=['photo'])
def handle_image(message):
    print(f"📥 Image from @{message.from_user.username}")

    if message.from_user.username != AUTHORIZED_USER[1:]:
        bot.reply_to(message, "🚫 Unauthorized user.")
        return

    bot.reply_to(message, "🧠 Processing MCQ (free mode)...")

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

        # ✅ Free GPT response (g4f)
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,  # safest model
            messages=[{"role": "user", "content": prompt}]
        )

        print("✅ GPT Reply:", response)
        bot.reply_to(message, f"✅ Answer: {response.strip()}")

    except Exception as e:
        print("❌ Error:", e)
        bot.reply_to(message, f"❌ Failed: {e}")

bot.polling()
