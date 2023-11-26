bot = telebot.TeleBot('6938849355:AAG3pB88polt47lRopmc_Fg_Tak0_3v3NHo')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="vay",
    )

cursor = mydb.cursor()



@bot.message_handler(commands=['start'])
def start(message):
    surname = f" {message.from_user.last_name}" if message.from_user.last_name else ''
    bot.send_message(message.chat.id, f"Доброго времени суток, {message.from_user.first_name}{surname}. Введите пожалуйста id вашей компании.")

@bot.message_handler(func=lambda message: True)
def get_other_column(message):
    cursor = mydb.cursor()
    user_id = message.text
    cursor.execute("SELECT УФПС FROM suffer WHERE id= %s", (user_id,))
    result = cursor.fetchone()
    if result:
        bot.send_message(message.chat.id, "Результат для ID " + user_id + ": " + str(result[0]))
    else:
        bot.send_message(message.chat.id, "ID " + user_id + " не найден в базе данных.")




bot.polling(none_stop = True)
