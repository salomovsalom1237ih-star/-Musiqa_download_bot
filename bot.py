import telebot
import yt_dlp
import os

TOKEN = "8400235178:AAFVGy3M4uLuZcbCpzYu7F-rA7CeEwpzt4Q"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "🎧 Qo‘shiq nomini yoz")

def download(q):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'song.%(ext)s',
        'noplaylist': True,
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch1:{q}", download=True)
        file = ydl.prepare_filename(info['entries'][0])
        return file

@bot.message_handler(func=lambda m: True)
def handler(m):
    try:
        bot.send_message(m.chat.id, "⏳ Yuklanmoqda...")
        file = download(m.text)

        with open(file, "rb") as f:
            bot.send_audio(m.chat.id, f)

        os.remove(file)

    except:
        bot.send_message(m.chat.id, "❌ Xatolik")

print("Bot ishga tushdi")
bot.infinity_polling()
