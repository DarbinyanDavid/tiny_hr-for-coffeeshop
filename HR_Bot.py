import telebot
from telebot import types

bot = telebot.TeleBot('6623685383:AAHYy__KYbE3murEZGn4QlqkeyeeksiJvps')

@bot.message_handler(commands=['start'])

def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name},для приглашения на очное интервью  необходимо ответить на несколько вопросов. '
                                      f'Не переживай это не займет много времени😉'
                                      )
    bot.send_message(message.chat.id,
                     f'1. Напиши свое ФИО и возраст \n'
                     f'2. Какое у тебя гражданство \n'
                     f'3. Семейное положение \n'
                     f'4. Какое у тебя образование \n'
                     f'5. Есть ли у тебя опыт работы? Если да то какой \n'
                     f'6. Желаемы уровень заработной платы \n'
                     f'7. Напиши номер по которому можно с тобой связаться \n'
                     f'8. Есть ли у тебя хобби?Напиши парочку) ')

@bot.message_handler()

def main(message):
    bot.send_message(message.chat.id, f'Вот и все,спасибо за уделенное время.'
                                      f'Мы пригласим тебя на очное интервью,после ознакомления с твоими ответами.'
                                      f'Но за вкусным кофе ты можешь зайти к нам в любое время😊 ')





    markup = types.InlineKeyboardButton






bot.polling(none_stop = True)