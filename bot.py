import os
import telebot

# استدعاء التوكن من إعدادات الموقع بأمان
TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(bot_instance, message):
    bot_instance.reply_to(message, "أهلاً بكِ يا دكتورة مي! أنا بوت التمريض الخاص بكِ جاهز لاستقبال ملفاتك وتحويلها لكويزات وأسئلة تمريضية ممتازة.")

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    bot.reply_to(message, "تم استقبال الملف بنجاح! جارٍ تحضير الأسئلة وتنسيق الشرح والتصحيح الفوري...")

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
        
