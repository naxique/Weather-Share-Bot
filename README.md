# Weather Share Bot
 Простой бот для телеграма, который позволяет делиться погодой из разных уголков Земли.

# Как использовать
## Setup
Для того, чтобы запустить бота, вам как минимум понадобится 2 API-ключа
Первый от бота в телеграме, его можно получить, создав бота у @BotFather 
    (не забудьте включить в настройках бота inline-режим с помощью команды /setinline)
Второй нужно получить на сайте https://openweathermap.org/
    Зарегистрируйтесь, зайдите в личный кабинет и создайте api-ключ
Оба этих ключа нужно записать в config.ini
    От бота в телеграме - в строку bot_apikey, с сайта, который предоставляет информацию о погоде - в строку weather_apikey

## Использование
У бота два режима, inline-режим, с помощью которого вы можете поделиться с кем-то погодой в конкретной локации
    (для этого нужно обратиться к боту и написать город, например @bot Ванкувер)

И обычный режим, в котором вы можете просто написать боту, и узнать, какая сейчас погода в каком-либо городе.

## Зависимости
Библиотека для работы с API Telegram - aiogram