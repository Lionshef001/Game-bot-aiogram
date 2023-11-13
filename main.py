from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from asyncio import sleep

bot = Bot(token="")
dp = Dispatcher(bot=bot)

games_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Football ⚽️"),
            KeyboardButton(text="Basketball 🏀"),
            KeyboardButton(text="Bouling  🎳")
        ],
        [   KeyboardButton(text="Dice 🎲"),
            KeyboardButton(text="Fats 🎯"),
            KeyboardButton(text="Kazino 🎰")

        ]
    ], resize_keyboard=True
)

@dp.message_handler(text="/start")
async def command_start(message: types.Message):
    print(message)
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}\n"
                         f"game botga xush kelibsiz!", reply_markup=games_kb)



@dp.message_handler(text="Dice 🎲")
async def game_dice(message: types.Message):
    await message.answer("Narda o'yinini boshlaymiz\n"
                         "Oldin men yuraman, keyin sen!")
    await sleep(2)
    await message.answer("Men yuryapman!")
    bot_data = await message.answer_dice()
    bot_data = bot_data['dice']['value']
    await sleep(5)
    await message.answer("Endi sizni o'rningzga tashlayman!")
    await sleep(1)
    user_data = await message.answer_dice()
    user_data = user_data['dice']['value']
    await sleep(5)
    if user_data > bot_data:
        await message.answer("Siz yutdingiz!🥇\nTabriklayman")
    elif user_data == bot_data:
        await message.answer("Durrang!🏆")
    else:
        await message.answer("MAN YUTDIM!🤖💪")

@dp.message_handler(text="Football ⚽️")
async def game_football(message: types.Message):
    await message.answer("Futbol oyini boshladik!\n"
                         "Man birinchi bo'lib tepaman")
    await sleep(1)

    bot_data = await message.answer_dice('⚽️')
    bot_data = bot_data['dice']['value']
    await sleep(5)
    await message.answer("Endi sizni o'rningzga tepaman!")
    await sleep(1)
    user_data = await message.answer_dice('⚽️')
    user_data = user_data['dice']['value']
    await sleep(5)
    if user_data > bot_data:
        await message.answer("Siz yutdingiz!🥇\nTabriklayman")
    elif user_data == bot_data:
        await message.answer("Durrang!🏆")
    else:
        await message.answer("MAN YUTDIM!🤖💪")

@dp.message_handler(text="Fats 🎯")
async def game_football(message: types.Message):
    await message.answer("Fats oyini boshladik!\n"
                         "Man birinchi bo'lib otaman")
    await sleep(1)

    bot_data = await message.answer_dice('🎯')
    bot_data = bot_data['dice']['value']
    await sleep(5)
    await message.answer("Endi sizni o'rningzga otaman!")
    await sleep(1)
    user_data = await message.answer_dice('🎯')
    user_data = user_data['dice']['value']
    await sleep(5)
    if user_data > bot_data:
        await message.answer("Siz yutdingiz!🥇\nTabriklayman")
    elif user_data == bot_data:
        await message.answer("Durrang!🏆")
    else:
        await message.answer("MAN YUTDIM!🤖💪")



@dp.message_handler(text="Basketball 🏀")
async def game_football(message: types.Message):
    await message.answer("Basketboll oyini boshladik!\n"
                         "Man birinchi bo'lib otaman")
    await sleep(1)

    bot_data = await message.answer_dice('🏀')
    bot_data = bot_data['dice']['value']
    await sleep(5)
    await message.answer("Endi sizni o'rningzga otaman!")
    await sleep(1)
    user_data = await message.answer_dice('🏀')
    user_data = user_data['dice']['value']
    await sleep(5)
    if user_data > bot_data:
        await message.answer("Siz yutdingiz!🥇\nTabriklayman")
    elif user_data == bot_data:
        await message.answer("Durrang!🏆")
    else:
        await message.answer("MAN YUTDIM!🤖💪")



@dp.message_handler(text="Bouling  🎳")
async def game_football(message: types.Message):
    await message.answer("Bouling oyini boshladik!\n"
                         "Man birinchi bo'lib otaman")
    await sleep(1)
    bot_data = await message.answer_dice('🎳')
    bot_data = bot_data['dice']['value']
    await sleep(5)
    await message.answer("Endi sizni o'rningzga otaman!")
    await sleep(1)
    user_data = await message.answer_dice('🎳')
    user_data = user_data['dice']['value']
    await sleep(5)
    if user_data > bot_data:
        await message.answer("Siz yutdingiz!🥇\nTabriklayman")
    elif user_data == bot_data:
        await message.answer("Durrang!🏆")
    else:
        await message.answer("MAN YUTDIM!🤖💪")


@dp.message_handler(text="Kazino 🎰")
async def game_football(message: types.Message):
    await message.answer("Kazinoni boshladik!\n"
                         "Man birinchiman!")
    await sleep(1)

    bot_data = await message.answer_dice('🎰')
    bot_data = bot_data['dice']['value']
    await sleep(5)
    await message.answer("Endi sizni o'rningzga yuraman!")
    await sleep(1)
    user_data = await message.answer_dice('🎰')
    user_data = user_data['dice']['value']
    await sleep(5)
    if user_data > bot_data:
        await message.answer("Siz yutdingiz!🥇\nTabriklayman")
    elif user_data == bot_data:
        await message.answer("Durrang!🏆")
    else:
        await message.answer("MAN YUTDIM!🤖💪")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
