import telebot

# Replace this with your actual bot token
BOT_TOKEN = "8016232431:AAF8a81EtZAI1ta-KwSIW1NpJWWJBApQDks"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to PRO_MCQ_BOT!\nSend me an image of MCQ to get started.")

# Temporary echo handler
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.reply_to(message, f"You said: {message.text}")

print("🤖 Bot is running...")
bot.polling()
