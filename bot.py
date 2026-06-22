import telebot
from telebot import types

TOKEN = "8720001305:AAGQevoAF046Pltq54wSZxkSF6aTRnp1QWE"

bot = telebot.TeleBot(TOKEN)

voices = {
"qondaye": "AwACAgQAAxkBAAIBR2o4R75h3VJdMFyBgKNGwpSkQvxAALzCQACaPSEUoHqz6uoyqGPAQ",
"reyboy": "AwACAgQAAxkBAAIBSWo4SKeX-n3Zj_RAv0K5A89dwBXRAAIZCQACI"
}

@bot.inline_handler(func=lambda query: True)
def inline(query):

results = []

for name, fileid in voices.items():

    results.append(
        types.InlineQueryResultCachedVoice(
            id=name,
            voice_file_id=fileid,
            title=name
        )
    )

try:
    bot.answer_inline_query(
        query.id,
        results,
        cache_time=1
    )
except Exception as e:
    print(e)

print("Inline bot ishga tushdi...")

bot.infinity_polling(skip_pending=True)