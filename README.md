# 🤖 Telegram MCQ Solver Bot

A smart Telegram bot that reads MCQ questions from images (like DSA, CS Fundamentals, etc.) and solves them using GPT — all with a single click.

👉 **Try it now:** [MCQ_PRO_BOT on Telegram](https://t.me/MCQ_SOLVER_PRO_BOT)

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
