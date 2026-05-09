import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN, MCP_URL

async def pods(update: Update, context: ContextTypes.DEFAULT_TYPE):
    res = requests.get(f"{MCP_URL}/pods")
    await update.message.reply_text(res.text[:4000])

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pod = context.args[0]
    res = requests.get(f"{MCP_URL}/analyze/{pod}")
    await update.message.reply_text(res.json()["analysis"][:4000])

async def analyze_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    res = requests.get(f"{MCP_URL}/analyze-all")
    await update.message.reply_text(res.json()["analysis"][:4000])

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("pods", pods))
    app.add_handler(CommandHandler("analyze", analyze))
    app.add_handler(CommandHandler("analyze_all", analyze_all))

    app.run_polling()

if __name__ == "__main__":
    main()