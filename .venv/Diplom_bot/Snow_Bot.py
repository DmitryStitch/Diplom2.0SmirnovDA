import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

from Diplom_bot.Keyboards import *
from Diplom_bot import text
from Diplom_bot.Price import *
from Diplom_bot.Image import *
from Diplom_bot.Config import API
from Diplom_bot.Sklad import *


logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    size_foot = State()
    growth = State()
    weight = State()

    size_foot_mu = State()
    growth_mu = State()
    weight_mu = State()

    size_foot_mfs = State()
    growth_mfs = State()
    weight_mfs = State()

    size_foot_mfr = State()
    growth_mfr = State()
    weight_mfr = State()

    size_foot_prouniv = State()
    growth_prouniv = State()
    weight_prouniv = State()

    size_foot_profs = State()
    growth_profs = State()
    weight_profs = State()

    size_foot_profr = State()
    growth_profr = State()
    weight_profr = State()


@dp.message_handler(commands = ["start"])
async def start(message):
    await message.answer(f"Привет, {message.from_user.username}" + text.start, reply_markup = start_kb)

@dp.message_handler(text = "О нас")
async def inform(message):
    with open('Imeges/Сноубордист.jpg', 'rb') as img:
        await message.answer_photo(img, text.about, reply_markup = start_kb)

@dp.message_handler(text = "Подбор")
async def podbor(message):
    await message.answer("Выберите Ваш уровень катания", reply_markup = podbor_kb)

@dp.callback_query_handler(state=UserState, text=["Новичок", "Прогрессирующий", "Профессионал"])
async def process_level(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(level=call.data)
    if call.data == "Новичок":
        await call.message.answer("Введите Ваш размер ноги (в мм):")
        await UserState.size_foot.set()
    elif call.data == "Прогрессирующий":
        await call.message.answer("Выберите стиль катания:", reply_markup= progress_kb)
    elif call.data == "Профессионал":
        await call.message.answer("Выберите стиль катания:", reply_markup= profy_kb)


@dp.callback_query_handler(text='New')
async def size_foot(call):
    await call.message.answer("Введите Ваш размер ноги (в мм):")
    await UserState.size_foot.set()

@dp.message_handler(state = UserState.size_foot)
async def set_growth(message: types.Message, state: FSMContext):
        size_foot = int(message.text)
        await state.update_data(size_foot = size_foot)
        prod_bot = get_product(ModelNBot)
        prod_kr = get_product(ModelNKr)
        with open(prod_bot['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_bot['opisanie'], reply_markup = buy_kb)
        await message.answer("Под эти ботинки прекрасно подойдет следующая модель креплений:")
        with open(prod_kr['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_kr['opisanie'], reply_markup = buy_kb)
        await message.answer("Введите свой рост (в см):")
        await UserState.next()

@dp.message_handler(state=UserState.growth)
async def set_weight(message:types.Message, state: FSMContext):
        growth = int(message.text)
        await state.update_data(growth=growth)
        await message.answer("Введите свой вес (в кг):")
        await UserState.next()

@dp.message_handler(state=UserState.weight)
async def send_calories(message:types.Message, state: FSMContext):
        weight = int(message.text)
        await state.update_data(weight=weight)
        data = await state.get_data()
        size_foot = data.get('size_foot')
        growth = data.get('growth')
        weight = data.get('weight')
        prod_Snow = get_product(ModelNSnow)
        with open(prod_Snow['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_Snow['opisanie'], reply_markup=buy_kb)
        new = ModelNBot, ModelNKr, ModelNSnow
        fin_price = priceNBot + priceNKr + priceNSnow
        await message.answer(f"Поздравляем, вы собрали комплект для начинающего: {new}, общая стоимость комплекта {fin_price} рублей.", reply_markup=buy_kb)
        await state.finish()

@dp.callback_query_handler(text = 'Medium')
async def style(call):
    await call.message.answer("Выберите ваш стиль катания:", reply_markup = progress_kb)

@dp.callback_query_handler(text = 'Universal')
async def size_foot_mu(call):
    await call.message.answer("Введите Ваш размер ноги (в мм):")
    await UserState.size_foot_mu.set()

@dp.message_handler(state = UserState.size_foot_mu)
async def set_growth_mu(message: types.Message, state: FSMContext):
        size_foot_mu = int(message.text)
        await state.update_data(size_foot_mu = size_foot_mu)
        prod_botmu = get_product(ModelMBot_Park)
        prod_krmu = get_product(ModelMKr_Park)
        with open(prod_botmu['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_botmu['opisanie'], reply_markup=buy_kb)
        await message.answer("Под эти ботинки прекрасно подойдет следующая модель креплений:")
        with open(prod_krmu['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_krmu['opisanie'], reply_markup=buy_kb)
        await message.answer("Введите свой рост (в см):")
        await UserState.next()

@dp.message_handler(state=UserState.growth_mu)
async def set_weight_mu(message:types.Message, state: FSMContext):
        growth_mu = int(message.text)
        await state.update_data(growth=growth_mu)
        await message.answer("Введите свой вес (в кг):")
        await UserState.next()

@dp.message_handler(state=UserState.weight_mu)
async def send_complekt_mu(message:types.Message, state: FSMContext):
        weight_mu = int(message.text)
        await state.update_data(weight_mu = weight_mu)
        data = await state.get_data()
        size_foot_mu = data.get('size_foot_mu')
        growth_mu = data.get('growth_mu')
        weight_mu = data.get('weight_mu')
        prod_Snowmu = get_product(ModelMSnow_Park)
        with open(prod_Snowmu['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_Snowmu['opisanie'], reply_markup=buy_kb)
        new_mu = ModelMBot_Park, ModelMKr_Park, ModelMSnow_Park
        fin_price_mu = priceMBot_Park + priceMKr_Park + priceMSnow_Park
        await message.answer(f"Поздравляем, вы собрали свой универсальный комплект : {new_mu}, общая стоимость комплекта {fin_price_mu} рублей.", reply_markup=buy_kb)
        await state.finish()

@dp.callback_query_handler(text = 'Freestyle')
async def size_foot_mfs(call):
    await call.message.answer("Введите Ваш размер ноги (в мм):")
    await UserState.size_foot_mfs.set()

@dp.message_handler(state = UserState.size_foot_mfs)
async def set_growth_mfs(message: types.Message, state: FSMContext):
        size_foot_mfs = int(message.text)
        await state.update_data(size_foot_mfs = size_foot_mfs)
        prod_botmfs = get_product(ModelMBot_Freestyle)
        prod_krmfs = get_product(ModelMKr_Freestyle)
        with open(prod_botmfs['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_botmfs['opisanie'], reply_markup=buy_kb)
        await message.answer("Под эти ботинки прекрасно подойдет следующая модель креплений:")
        with open(prod_krmfs['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_krmfs['opisanie'], reply_markup=buy_kb)
        await message.answer("Введите свой рост (в см):")
        await UserState.next()

@dp.message_handler(state=UserState.growth_mfs)
async def set_weight_mfs(message:types.Message, state: FSMContext):
        growth_mfs = int(message.text)
        await state.update_data(growth_mfs=growth_mfs)
        await message.answer("Введите свой вес (в кг):")
        await UserState.next()

@dp.message_handler(state=UserState.weight_mfs)
async def send_complekt_mfs(message:types.Message, state: FSMContext):
        weight_mfs = int(message.text)
        await state.update_data(weight_mfs = weight_mfs)
        data = await state.get_data()
        size_foot_mfs = data.get('size_foot_mfs')
        growth_mfs = data.get('growth_mfs')
        weight_mfs = data.get('weight_mfs')
        prod_Snowmfs = get_product(ModelMSnow_Freestyle)
        with open(prod_Snowmfs['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_Snowmfs['opisanie'], reply_markup=buy_kb)
        new_mfs = ModelMBot_Freestyle, ModelMKr_Freestyle, ModelMSnow_Freestyle
        fin_price_mfs = priceMBot_Freestyle + priceMKr_Freestyle + priceMSnow_Freestyle
        await message.answer(f"Поздравляем, вы собрали свой комплект для Фристайла : {new_mfs}, общая стоимость комплекта {fin_price_mfs} рублей.", reply_markup=buy_kb)
        await state.finish()

@dp.callback_query_handler(text = 'Freeride')
async def size_foot_mfr(call):
    await call.message.answer("Введите Ваш размер ноги (в мм):")
    await UserState.size_foot_mfr.set()

@dp.message_handler(state = UserState.size_foot_mfr)
async def set_growth_mfr(message: types.Message, state: FSMContext):
        size_foot_mfr = int(message.text)
        await state.update_data(size_foot_mfr = size_foot_mfr)
        prod_botmfr = get_product(ModelMBot_Freeride)
        prod_krmfr = get_product(ModelMKr_Freeride)
        with open(prod_botmfr['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_botmfr['opisanie'], reply_markup=buy_kb)
        await message.answer("Под эти ботинки прекрасно подойдет следующая модель креплений:")
        with open(prod_krmfr['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_krmfr['opisanie'], reply_markup=buy_kb)
        await message.answer("Введите свой рост (в см):")
        await UserState.next()

@dp.message_handler(state = UserState.growth_mfr)
async def set_weight_mfr(message:types.Message, state: FSMContext):
        growth_mfr = int(message.text)
        await state.update_data(growth_mfr = growth_mfr)
        await message.answer("Введите свой вес (в кг):")
        await UserState.next()

@dp.message_handler(state = UserState.weight_mfr)
async def send_complekt_mfr(message:types.Message, state: FSMContext):
        weight_mfr = int(message.text)
        await state.update_data(weight_mfr = weight_mfr)
        data = await state.get_data()
        size_foot_mfr = data.get('size_foot_mfr')
        growth_mfr = data.get('growth_mfr')
        weight_mfr = data.get('weight_mfr')
        prod_Snowmfr = get_product(ModelMSnow_Freeride)
        with open(prod_Snowmfr['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_Snowmfr['opisanie'], reply_markup=buy_kb)
        new_mfr = ModelMBot_Freeride, ModelMKr_Freeride, ModelMSnow_Freeride
        fin_price_mfr = priceMBot_Freeride + priceMKr_Freeride + priceMSnow_Freeride
        await message.answer(f"Поздравляем, вы собрали свой комплект для Фрирайда : {new_mfr}, общая стоимость комплекта {fin_price_mfr} рублей.", reply_markup=buy_kb)
        await state.finish()

@dp.callback_query_handler(text = 'Pro')
async def style(call):
    await call.message.answer("Выберите ваш стиль катания:", reply_markup = profy_kb)

@dp.callback_query_handler(text = 'ProUniversal')
async def size_foot_prouniv(call):
    await call.message.answer("Введите Ваш размер ноги (в мм):")
    await UserState.size_foot_prouniv.set()

@dp.message_handler(state = UserState.size_foot_prouniv)
async def set_growth_prouniv(message: types.Message, state: FSMContext):
        size_foot_prouniv = int(message.text)
        await state.update_data(size_foot_pro_univ = size_foot_prouniv)
        prod_botprouniv = get_product(ModelProBot_Park)
        prod_krprouniv = get_product(ModelProKr_Park)
        with open(prod_botprouniv['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_botprouniv['opisanie'], reply_markup=buy_kb)
        await message.answer("Под эти ботинки прекрасно подойдет следующая модель креплений:")
        with open(prod_krprouniv['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_krprouniv['opisanie'], reply_markup=buy_kb)
        await message.answer("Введите свой рост (в см):")
        await UserState.next()

@dp.message_handler(state=UserState.growth_prouniv)
async def set_weight_prouniv(message:types.Message, state: FSMContext):
        growth_prouniv = int(message.text)
        await state.update_data(growth_prouniv=growth_prouniv)
        await message.answer("Введите свой вес (в кг):")
        await UserState.next()

@dp.message_handler(state=UserState.weight_prouniv)
async def send_complekt_prouniv(message:types.Message, state: FSMContext):
        weight_prouniv = int(message.text)
        await state.update_data(weight_prouniv = weight_prouniv)
        data = await state.get_data()
        size_foot_prouniv = data.get('size_foot_prouniv')
        growth_prouniv = data.get('growth_prouniv')
        weight_prouniv = data.get('weight_prouniv')
        prod_Snowprouniv = get_product(ModelProSnow_Park)
        with open(prod_Snowprouniv['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_Snowprouniv['opisanie'], reply_markup=buy_kb)
        new_pu = ModelProBot_Park, ModelProKr_Park, ModelProSnow_Park
        fin_price_pu = priceProBot_Park + priceProKr_Park + priceProSnow_Park
        await message.answer(f"Поздравляем, вы собрали свой универсальный комплект : {new_pu}, общая стоимость комплекта {fin_price_pu} рублей.", reply_markup=buy_kb)
        await state.finish()

@dp.callback_query_handler(text = 'ProFreestyle')
async def size_foot_profs(call):
    await call.message.answer("Введите Ваш размер ноги (в мм):")
    await UserState.size_foot_profs.set()

@dp.message_handler(state = UserState.size_foot_profs)
async def set_growth_profs(message: types.Message, state: FSMContext):
        size_foot_profs = int(message.text)
        await state.update_data(size_foot_profs = size_foot_profs)
        prod_botprofs = get_product(ModelProBot_Freestyle)
        prod_krprofs = get_product(ModelProKr_Freestyle)
        with open(prod_botprofs['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_botprofs['opisanie'], reply_markup=buy_kb)
        await message.answer("Под эти ботинки прекрасно подойдет следующая модель креплений:")
        with open(prod_krprofs['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_krprofs['opisanie'], reply_markup=buy_kb)
        await message.answer("Введите свой рост (в см):")
        await UserState.next()

@dp.message_handler(state=UserState.growth_profs)
async def set_weight_profs(message:types.Message, state: FSMContext):
        growth_profs = int(message.text)
        await state.update_data(growth_pro_fs=growth_profs)
        await message.answer("Введите свой вес (в кг):")
        await UserState.next()

@dp.message_handler(state=UserState.weight_profs)
async def send_complekt_pro_fs(message:types.Message, state: FSMContext):
        weight_pro_fs = int(message.text)
        await state.update_data(weight_pfs = weight_pro_fs)
        data = await state.get_data()
        size_foot_pro_fs = data.get('size_foot_pro_fs')
        growth_pro_fs = data.get('growth_pro_fs')
        weight_pro_fs = data.get('weight_pro_fs')
        prod_Snowprofs = get_product(ModelProSnow_Freestyle)
        with open(prod_Snowprofs['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_Snowprofs['opisanie'], reply_markup=buy_kb)
        new_pfs = ModelProBot_Freestyle, ModelProKr_Freestyle, ModelProSnow_Freestyle
        fin_price_pfs = priceProBot_Freestyle + priceProKr_Freestyle + priceProSnow_Freestyle
        await message.answer(f"Поздравляем, вы собрали свой комплект для Фристайла : {new_pfs}, общая стоимость комплекта {fin_price_pfs} рублей.", reply_markup=buy_kb)
        await state.finish()

@dp.callback_query_handler(text = 'ProFreeride')
async def size_foot_profr(call):
    await call.message.answer("Введите Ваш размер ноги (в мм):")
    await UserState.size_foot_profr.set()

@dp.message_handler(state = UserState.size_foot_profr)
async def set_growth_profr(message: types.Message, state: FSMContext):
        size_foot_profr = int(message.text)
        await state.update_data(size_foot_profr = size_foot_profr)
        prod_botprofr = get_product(ModelProBot_Freeride)
        prod_krprofr = get_product(ModelProKr_Freeride)
        with open(prod_botprofr['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_botprofr['opisanie'], reply_markup=buy_kb)
        await message.answer("Под эти ботинки прекрасно подойдет следующая модель креплений:")
        with open(prod_krprofr['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_krprofr['opisanie'], reply_markup=buy_kb)
        await message.answer("Введите свой рост (в см):")
        await UserState.next()

@dp.message_handler(state = UserState.growth_profr)
async def set_weight_profr(message:types.Message, state: FSMContext):
        growth_profr = int(message.text)
        await state.update_data(growth_profr = growth_profr)
        await message.answer("Введите свой вес (в кг):")
        await UserState.next()

@dp.message_handler(state = UserState.weight_profr)
async def send_complekt_profr(message:types.Message, state: FSMContext):
        weight_profr = int(message.text)
        await state.update_data(weight_profr = weight_profr)
        data = await state.get_data()
        size_foot_profr = data.get('size_foot_profr')
        growth_profr = data.get('growth_profr')
        weight_profr = data.get('weight_profr')
        prod_Snowprofr = get_product(ModelProSnow_Freeride)
        with open(prod_Snowprofr['image_path'], 'rb') as img:
            await message.answer_photo(img, prod_Snowprofr['opisanie'], reply_markup=buy_kb)
        new_pfr = ModelProBot_Freeride, ModelProKr_Freeride, ModelProSnow_Freeride
        fin_price_pfr = priceProBot_Freeride + priceProKr_Freeride + priceProSnow_Freeride
        await message.answer(f"Поздравляем, вы собрали свой комплект для Фрирайда : {new_pfr}, общая стоимость комплекта {fin_price_pfr} рублей.", reply_markup=buy_kb)
        await state.finish()

@dp.callback_query_handler(text="other")
async def buy_other(call):
    await call.message.answer(text.other)
    await call.answer()

@dp.callback_query_handler(text="back_to_cataloge")
async def back(call):
    await call.message.answer("Выберите Ваш уровень катания", reply_markup = podbor_kb)
    await call.answer()

@dp.message_handler(state=None)
async def all_massages(message: types.Message):
    await message.reply("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        logging.exception(e)


