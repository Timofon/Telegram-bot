import random

from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = ''

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Имя, id стикера
data_for_harry_potter = [['Гарри Поттер', 'CAACAgIAAxkBAAEG3RRjndRcOaj4IBLk0mxQab_4R0_T7gAC7AIAAs9fiweW49WBOm8LJywE'],
                         ['Рон Уизли', 'CAACAgIAAxkBAAEG3RZjndSCDjIvRx8q6ndA0V0pRl6LqwAC3QIAAs9fiwfP1fFCxpmbNywE'],
                         ['Вол-де-морт', 'CAACAgIAAxkBAAEG3RpjndSkDxV14wIdFO5xCcIwXDhqAAO0AgACz1-LB00sWdWLQ9DjLAQ'],
                         ['Плакса Миртл', 'CAACAgIAAxkBAAEG3RxjndVjWrXncwL3PswCjb1946yDZQAC7gIAAs9fiwe6obimIRuNhSwE'],
                         ['Северус Снейп', 'CAACAgIAAxkBAAEG3R5jndWIkd5AztE0rpVZcvOfNHsoOAACuQIAAs9fiwdyWbnBlWWmGSwE'],
                         ['Альбус Дамблор', 'CAACAgIAAxkBAAEG3TFjndcWnR3Kw4pTGiNMIRJpj6-aFgACvQIAAs9fiweuhbmwQU1NZCwE'],
                         ['Сова', 'CAACAgIAAxkBAAEG3TNjnddktANx6j9FvNtQZNa95AAB9F4AAuoCAALPX4sHqlGYoMsffEUsBA']]

raw = '''* Джанго освобождённый
* Бешеные псы
* Помни
* Брат
* Брат 2
* Большой куш
* Крестный отец
* Лето
* Борат
* Люди в черном
* Остров проклятых
* Бегущий по лезвию 2049
* День сурка
* Ирландец
* Дюна
* Шоу Трумана
* Не грози южному централу, попивая сок у себя в квартале
* Социальная сеть
* Убийство в восточном экспрессе
* Острые козырьки
* Гражданин Кейн
* The business of drugs (документалка)
* Полночное небо
* Рик и Морти
* Убийство на яхте
* Игры разума
* Зелёная книга
* Жизнь прекрасна
* Человек с бульвара Капуцинов
* Паразиты
* Человек дождя
* 1+1
* Облачный атлас
* Место встречи изменить нельзя
* Джобс. Империя соблазна
* Плохой. Хороший. Злой
* Пацаны
* Укрощение строптивого
* Игра на понижение
* Twin Peaks
* Рок волна
* Ещё по одной
* Красотка
* Отель Гранд Будапешт
* Drive
* Бумажный дом
* Знакомство с родителями
* Собачье сердце
* Трасса 60
* Достучаться до небес
* Ван Хельсинг
* Bridgerton
* Я - легенда
* Одержимость
* Что-то из Хичкока
* Револьвер
* Молчание ягнят
* Рок-н-ролльщик
* Sex education
* Что-нибудь из Дейвида Финчера
* Stranger things
* Catch me if you can
* Запах женщины
* Игры разума
* JoJo rabbit
* Игра
* Унесенные ветром
* О чем говорят мужчины 3
* Margin call
* Big short
* Заводной апельсин
* Майор Гром
* Мир дикого запада
* Мне 20 лет
* Россия, которую мы потеряли
* Особенности национальной охоты
* Шерлок
* Космическая одиссея 2001
* Завтрак у Тиффани
'''

data_for_movies = raw.split('*')[1:]
for i in range(len(data_for_movies)):
    data_for_movies[i] = data_for_movies[i][:-1]
    data_for_movies[i] = data_for_movies[i][1:]

button_whoami = KeyboardButton('Кто я из Гарри Поттера?')
button_movie = KeyboardButton('Какой фильм мне посмотреть?')
button_help = KeyboardButton('Что ты умеешь?')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_whoami)
greet_kb.add(button_movie)
greet_kb.add(button_help)


@dp.message_handler(commands=['start'])
async def hello_message(message):
    await message.reply("Wazzup, это приятный бот для приятных людей", reply_markup=greet_kb)
    await bot.send_message(message.chat.id,
                           "Функции:"
                           "\n Узнать кто я из Гарри Поттера\n "
                           "Получить рекомендацию по фильму\n "
                           "Показать все функции")


@dp.message_handler(text='Кто я из Гарри Поттера?')
async def whoami_message(message: types.Message):
    pair = random.choice(data_for_harry_potter)
    await message.reply("Из Гарри Поттера ты " + pair[0])
    await bot.send_sticker(message.chat.id, pair[1])
    if pair[0] == 'Северус Снейп':
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEG3Tljndh0F62DopZBh2t9pOmVnkotjgACjBMAAm14yUs0SD5PPsFchywE')


@dp.message_handler(text='Что ты умеешь?')
async def help_message(message: types.Message):
    await message.reply("Функции:"
                        "\n Узнать кто я из Гарри Поттера\n "
                        "Получить рекомендацию по фильму\n "
                        "Показать все функции")


@dp.message_handler(text='Какой фильм мне посмотреть?')
async def movie_message(message):
    movie = '"' + random.choice(data_for_movies) + '"'
    await message.reply('Тебе стоит посмотреть фильм ' + movie)


@dp.message_handler()
async def invalid_message(msg: types.Message):
    await msg.reply("Изпользуй изначальные кнопки")


executor.start_polling(dp)
