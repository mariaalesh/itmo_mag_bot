import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from config import TELEGRAM_TOKEN

# Загружаем учебные планы
with open('plans/ai.json', encoding='utf-8') as f:
    ai_plan = json.load(f)
with open('plans/ai_product.json', encoding='utf-8') as f:
    aip_plan = json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я помогу выбрать между магистратурами ITMO: Artificial Intelligence и AI: Product Approach.\n"
        "Задайте вопрос или расскажите о вашем бэкграунде."
    )

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if 'разница' in text or 'отличие' in text:
        await update.message.reply_text(
            "Artificial Intelligence — про алгоритмы, исследования и глубокий ИИ.\n"
            "AI: Product Approach — про применение ИИ в продуктах, управление проектами и вывод на рынок."
        )
    elif 'дисциплины' in text and 'product' in text:
        await update.message.reply_text(
            "Элективы на AI Product:\n" + "\n".join(aip_plan['electives'])
        )
    elif 'дисциплины' in text and 'ai' in text:
        await update.message.reply_text(
            "Элективы на AI:\n" + "\n".join(ai_plan['electives'])
        )
    elif 'рекомендац' in text or 'посоветуй' in text:
        bg = text
        # Простая логика рекомендации
        if any(word in bg for word in ['матем', 'data', 'ds', 'программ']):
            await update.message.reply_text(
                "Вам могут подойти продвинутые курсы по ML/AI, например:\n" + "\n".join([e for e in ai_plan['electives'] if 'advanced' in e.lower() or 'machine' in e.lower()])
            )
        else:
            await update.message.reply_text(
                "Советуем начать с элективов по введению в Data Science и управлению продуктами."
            )
    else:
        await update.message.reply_text(
            "Я могу отвечать только на вопросы по учебным планам и дисциплинам программ AI и AI Product в ИТМО."
        )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, answer))
    print("Бот запущен")
    app.run_polling()
