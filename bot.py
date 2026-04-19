import time
import telebot
from telebot import apihelper
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден! Проверь файл .env")

bot = telebot.TeleBot(TOKEN)

def create_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        KeyboardButton("🛡️ Профилактика укусов"),
        KeyboardButton("⚠️ Действия при укусе"),
        KeyboardButton("ℹ️ Общая информация"),
        KeyboardButton("🔗 Полезные ссылки")
    ]
    markup.add(*buttons)
    return markup

@bot.message_handler(commands=['start'])
def start_command(message):
    welcome_text = (
        "👋 Привет! Я бот о защите от клещей.\n\n"
        "Выберите тему из кнопок ниже или напишите свой вопрос.\n"
        "Я дам полезные советы и инструкции!"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=create_keyboard())

@bot.message_handler(func=lambda m: True)
def handle_messages(message):
    text = message.text.strip()

    if text == "🛡️ Профилактика укусов":
        photo_path = 'images/prevention.jpg'  # положите картинку профилактики в папку images
        response = (
            "🕷 *Профилактика укусов клещей:*\n\n"
            "1️⃣ Носите светлую закрытую одежду\n"
            "2️⃣ Используйте репелленты на одежду и кожу\n"
            "3️⃣ Обязательно осматривайте себя и домашних животных после прогулки\n"
            "4️⃣ Избегайте высоких трав, кустов и лесных троп\n"
            "5️⃣ Закрывайте щели в обуви и манжеты"
        )
        bot.send_photo(message.chat.id, photo=open(photo_path, 'rb'), caption=response, parse_mode='Markdown')

    elif text == "⚠️ Действия при укусе":
        photo_path = 'images/after_bite.png'  # картинка действий после укуса
        response = (
            "⚠️ *Если вас укусил клещ — как безопасно удалить:*\n\n"
            "1️⃣ *Пинцет*\n\n"  
            "- Используйте тонкий пинцет, захватите клеща как можно ближе к коже.\n"  
            "- Тяните медленно и прямо вверх, не скручивая.\n"  
            "- После удаления обработайте место антисептиком.\n\n"

            "2️⃣ *Нить*\n\n"  
            "- Оберните тонкую нить вокруг головы клеща.\n"  
            "- Аккуратно подтягивайте, пока клещ не освободится.\n"  
            "- Не раздавливайте тело клеща.\n\n"

            "3️⃣ *Ручка-лассо*\n\n"
            "- Специальное устройство для захвата клеща.\n"  
            "- Наденьте «лассо» на клеща и медленно потяните.\n"  
            "- Это уменьшает риск раздавливания и заражения.\n\n"

            "4️⃣ *Клещевер*\n\n"  
            "- Вставьте инструмент под клеща, зацепив голову.\n"  
            "- Поверните или потяните согласно инструкции прибора.\n"  
            "- Обработайте место укуса антисептиком и вымойте руки.\n\n"

            "💡 *Совет:* сохраняйте клеща для анализа, если появятся симптомы (сыпь, температура, слабость).\n"  
            "🩺 При любых сомнениях — сразу обращайтесь к врачу!\n"

        )
        bot.send_photo(message.chat.id, photo=open(photo_path, 'rb'), caption=response, parse_mode='Markdown')

    elif text == "ℹ️ Общая информация":
        photo_path = 'images/info.jpeg'  # общая информация
        response = (
            "ℹ️ *Общая информация о клещах:*\n\n"

            "• Клещи — это мелкие паразиты, которые питаются кровью животных и человека.\n"
            "• Опасны тем, что могут переносить болезни:\n"  
            "- *Клещевой боррелиоз (болезнь Лайма)*\n"  
            "- *Клещевой вирусный энцефалит* \n" 
            "• Наиболее активны в весенне-летний период, особенно в мае–июне.\n"  
            "• Часто встречаются в лесу, парках, садах и высокой траве.\n"  
            "• Любая высокая трава, кусты и тёмные влажные участки повышают риск укуса.\n"  
            "• На домашних животных (собаках, кошках) клещи тоже нападают — проверяйте питомцев после прогулки.\n\n"  
            
            "⚠️ *Признаки заражения после укуса:*\n\n"  
            "- Сыпь или покраснение вокруг места укуса\n"  
            "- Повышенная температура, головная боль, слабость\n"  
            "- Симптомы появляются через несколько дней или недель\n"  

            "🩺 *Важно:* при появлении любых симптомов после укуса — сразу обратитесь к врачу!"
        )
        bot.send_photo(message.chat.id, photo=open(photo_path, 'rb'), caption=response, parse_mode='Markdown')

    elif text == "🔗 Полезные ссылки":
        response = (
            "🔗 *Полезные ресурсы:*\n\n"
            "• [Роспотребнадзор — клещи](https://www.rospotrebnadzor.ru/activities/recommendations/details.php?ELEMENT_ID=222)\n"
            "• [Вирусный энцефалит — рекомендации](https://diseases.medelement.com/disease/клещевой-вирусный-энцефалит-у-взрослых-кп-рф-2025/19001)\n"
            "• [Как правильно удалять клеща](https://71.rospotrebnadzor.ru/content/612/110623/)"
        )
        bot.send_message(message.chat.id, response, parse_mode='Markdown', reply_markup=create_keyboard())

    else:
        response = "Я пока знаю только про профилактику и укусы клещей. Выберите тему из кнопок 👇"
        bot.send_message(message.chat.id, response, parse_mode='Markdown', reply_markup=create_keyboard())

if __name__ == "__main__":
    print("🚀 Бот запущен! Ctrl+C для остановки")
    while True:
        try:
            bot.polling(non_stop=True)
        except apihelper.ApiException as e:
            print("⚠️ Ошибка Telegram API:", e)
            time.sleep(5)
        except Exception as e:
            print("❌ Другая ошибка:", e)
            time.sleep(5)
