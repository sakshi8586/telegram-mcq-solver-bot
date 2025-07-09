# 🤖 Telegram MCQ Solver Bot

A smart Telegram bot that reads MCQ questions from images (like DSA, CS Fundamentals, etc.) and solves them using GPT — all with a single click.

👉 **Try it now:** [PRO_MCQ_BOT on Telegram](https://t.me/PRO_MCQ_BOT)

---

## 🚀 Features

- 🧠 GPT-based AI to solve multiple-choice questions  
- 📸 Accepts images of MCQ questions (screenshots, scanned pages, etc.)  
- 🔍 OCR-powered text extraction using Tesseract  
- ✅ No need to type — just send the image  
- 🤖 Automatically greets and guides the user  
- 🔓 Public access — anyone can use it freely  
- 💬 Works on first message or image (no `/start` required)  
- 🔁 Stateless — works even after chat is cleared

---

## 🧱 Tech Stack

| Layer         | Tool/Library             |
|---------------|---------------------------|
| Bot Platform  | Telegram + `pyTelegramBotAPI` |
| OCR Engine    | Tesseract OCR             |
| AI Backend    | GPT (via `g4f` API)       |
| Image Parsing | Pillow + Requests         |
| Hosting       | Replit                    |
| Version Ctrl  | Git + GitHub              |

---

## 🖼️ How It Works

1. User sends **any message** or **MCQ image**  
2. Bot replies:  
   - 👋 “Welcome to Sakshi's MCQ_PRO_BOT”  
   - 📸 “Please send me the image of your MCQ question”  
3. Bot extracts text from image using OCR  
4. Sends it to GPT and replies with correct option (A/B/C/D) ✅

---

## 🧑‍💻 Author

Made with ❤️ by [@ro_sakshi](https://github.com/sakshi8586)

