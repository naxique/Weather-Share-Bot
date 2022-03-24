"""
    by naxique 25.03.2022
    WEATHER SHARE BOT
        Как использовать: 
            Конфигурация:
                в config.ini введите два api-ключа, первый - от бота в телеграме, второй с https://openweathermap.org/
            В телеграме: Ввод: @bot Город Вывод: user via @bot: Город +16 пасмурно
                    Либо просто отправьте боту город, он ответит вам, какая там погода :)
"""

import hashlib, logging, configparser

from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle, Message
from getWeather import Weather

# Configure logging
logging.basicConfig(level=logging.INFO)

#Reading API keys from config file
config = configparser.ConfigParser()
config.read('config.ini')
BOT_APIKEY = config['MAIN']['bot_apikey']
WEATHER_APIKEY = config['MAIN']['weather_apikey']

#Initializing bot
bot = Bot(token=BOT_APIKEY)
dispatcher = Dispatcher(bot)
weatherApi = Weather(WEATHER_APIKEY)

#Handle inline output
@dispatcher.inline_handler()
async def inlineEcho(inlineQuery: InlineQuery):
    #Get inline query
    input = inlineQuery.query or '---'
    inputContent = InputTextMessageContent(input)

    #Send request for weather
    result = weatherApi.getWeather(inputContent.message_text)

    #Generate unqiue message id
    resultId: str = hashlib.md5(result.encode()).hexdigest()

    #Gathering results together
    resultContent = InputTextMessageContent(result)
    item = InlineQueryResultArticle(
        id = resultId,
        title = result,
        input_message_content = resultContent
    )

    #And seding them out
    await bot.answer_inline_query(inlineQuery.id, results=[item], cache_time=1)

#Handle regular message output
@dispatcher.message_handler()
async def regularEcho(message: Message):
    result = weatherApi.getWeather(message.text)
    await message.answer(result)

#Starting bot
if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)