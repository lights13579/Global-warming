import telebot

bot = telebot.TeleBot("7520051631:AAEiG2XylbDYD000vH1Y3UT7B_jWTrqCpNE")

questions = [
    {
        "q": "1. Что такое глобальное потепление?\nа) Увеличение осадков\nб) Повышение средней температуры\nв) Похолодание\nг) Увеличение солнечной активности",
        "a": "б"
    },
    {
        "q": "2. Что сильнее всего влияет на глобальное потепление?\nа) Рыбалка\nб) Сжигание угля и нефти\nв) Сбор урожая\nг) Спорт",
        "a": "б"
    },
    {
        "q": "3. Почему таяние ледников опасно?\nа) Вызывает землетрясения\nб) Повышает уровень воды\nв) Делает океан соленым\nг) Создает пустыни",
        "a": "б"
    }
]

# Словари для отслеживания состояния пользователей
user_answers = {}
current_question_index = {}

# Команда /start
@bot.message_handler(commands=['start'])
def start_quiz(message):
    chat_id = message.chat.id
    user_answers[chat_id] = []
    current_question_index[chat_id] = 0
    bot.send_message(chat_id, "Hello! This is quiz about Global warming")
    send_question(chat_id)

# Отправка следующего вопроса
def send_question(chat_id):
    index = current_question_index[chat_id]
    if index < len(questions):
        bot.send_message(chat_id, questions[index]["q"])
    else:
        score = sum(1 for i, answer in enumerate(user_answers[chat_id]) if answer == questions[i]["a"])
        bot.send_message(chat_id, f"Викторина завершена! Ваш результат: {score} из {len(questions)}")

# Ответ пользователя
@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    chat_id = message.chat.id
    if chat_id in current_question_index:
        answer = message.text.strip().lower()
        user_answers[chat_id].append(answer)
        current_question_index[chat_id] += 1
        send_question(chat_id)
    else:
        bot.send_message(chat_id, "Напишите /start чтобы начать викторину")

if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)