# 🤖 Telegram MCQ Solver Bot

A smart Telegram bot that reads MCQ questions from images (like DSA, CS Fundamentals, etc.) and solves them using GPT — all with a single click.

---

## 🚀 Features

- 🧠 Uses GPT-based AI to solve MCQ questions
- 📸 Accepts images (screenshots/scans) of multiple-choice questions
- 🔍 OCR-powered text extraction (using Tesseract)
- ✅ No need to type — just send the image
- 📚 Automatically greets and prompts users for their question
- 🔓 Public usage — anyone can try!

---

## 🧱 Tech Stack

| Layer         | Tool/Library         |
|---------------|----------------------|
| Bot Platform  | Telegram + python-telegram-bot |
| OCR Engine    | Tesseract OCR        |
| AI Backend    | GPT (via `g4f` API)  |
| Image Parsing | Pillow + Requests    |
| Hosting       | Replit               |
| Version Ctrl  | Git + GitHub         |

---

## 🖼️ How It Works

1. User sends any message ➜ Bot replies with greeting and instructions.
2. User sends an image of the MCQ ➜
3. Bot extracts the question using OCR ➜
4. Bot sends question to GPT and returns the correct option (A/B/C/D) ✅

---

## 📦 Installation (For Local Testing)

> Clone the repo and install dependencies

```bash
git clone https://github.com/sakshi8586/telegram-mcq-solver-bot.git
cd telegram-mcq-solver-bot
pip install -r requirements.txt
