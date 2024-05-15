import asyncio
import os
from aiogram import F, Bot, types, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery
from aiogram.enums import ParseMode
from keyboards import get_callback_btns

bot = Bot(token=os.getenv('TOKEN'))

router = Router()

class Reg(StatesGroup):
    receive = State()
    subscription = State()
    subscribed = State()
    answer_yes = State()
    answer_no = State()
    Form = State()

@router.message(CommandStart())
async def start_cmd(message: types.Message, state: FSMContext):
    await state.set_state(Reg.receive)
    await message.answer(
        f'<b>👋Приветствую тебя, я - Vlad VseOtec Американского Ютуба</b>\n'
        f'Давай я коротко расскажу, что тебя здесь ждет!\n\n'
        f'😋У меня есть <b>ПОШАГОВАЯ</b> инструкция, которая поможет тебе зайти на Американский Ютуб и начать на нем конечно-же зарабатывать\n\n'
        f'🧐<b>Почему Американский Ютуб?</b> Давай расскажу:\n'
        f'Американский Ютуб дает тебе не только свободу, так как вся работа происходит с ноутбука/пк/телефона на которую ты тратишь всего пару часов в день, но еще и обеспечивает тебя реально достойным заработком.\n\n'
        f'👌Чтобы было понятней, скажу так, с одного Американского канала можно зарабатывать <b>в среднем 300-1000$</b>, а таких каналов у тебя может быть несколько:)\n'
        f'<b>P.S Это называется <u>сетка каналов</u></b>. Ну вот, один термин ты уже знаешь, всё не так сложно, как может показаться!\n\n'
        f'❌И кстати, в отличии от "<b>российского</b>" Ютуба, на <b>Американском</b> Ютубе <b>НЕ</b> нужно снимать себя на камеру, записывать свой голос, придумывать часами какой-то сложный сценарий к видео и заниматься подобной фигней!\n\n'
        f'✅Именно благодаря этим плюсам, я, моя команда и мои ученики - выбрали Американский Ютуб и активно в нем развиваемся!\n\n'
        f'🔥Если тебе интересен Американский Ютуб и ты хочешь начать в нём развиваться и зарабатывать\n\n'
        f'🎁Смело нажимай на кнопку ниже и и получай мой первый подарок для тебя👇\n\n',
    parse_mode=ParseMode.HTML,
    reply_markup=get_callback_btns(btns={
    f'🎁Получить подарок': 'receive_{gift}'}))


@router.callback_query(Reg.receive, F.data.startswith('receive_'))
async def handle_callback(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(callback_query='receive_')
    await state.set_state(Reg.subscription)
    await callback_query.answer()
    await callback_query.message.answer(
        f'Перед тем как забрать подарок, подпишись на мой https://t.me/vlad_vseotec 👈\n\n'
        f'Там я постоянно провожу созвоны с подписчиками, отвечаю на их вопросы, помогаю и рассказываю еще больше <b>РЕАЛЬНО</b> годной инфы про Америкаский ютуб!\n\n'
        f'Подписывайся, а потом жми на кнопку снизу👇\n\n'
        f'https://t.me/chanel323b3ew \n\n',
        #disable_web_page_preview=True,
    parse_mode=ParseMode.HTML,
    reply_markup=get_callback_btns(btns={
    '✅Подписался': 'subscribed_{subscribe}'}))

@router.callback_query(F.data.startswith('start_subscription'))
async def handle_start_subscription_callback(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(
        f'❌Ты ещё <b>не подписался</b>. Подпишись на https://t.me/vlad_vseotec канал и нажимай на кнопку снизу👇\n\n',
        #disable_web_page_preview=True,
    parse_mode=ParseMode.HTML,
    reply_markup=get_callback_btns(btns={
    '✅Подписался': 'subscribed_{channel_id}'}))

@router.callback_query(Reg.subscription, F.data.startswith('subscribed_'))
async def handle_subscribed_callback(callback_query: CallbackQuery, state: FSMContext):
    result = await bot.get_chat_member(chat_id='-1001967695255', user_id=callback_query.from_user.id)
    if result.status == 'creator' or result.status == 'administrator' or result.status =='member': 
        await state.update_data(callback_query='subscribed_')
        await state.set_state(Reg.subscribed)
        await callback_query.answer()
        await callback_query.message.answer(
            f'<b>🙏Спасибо за подписку!</b>\n\n'
            f'🎁А теперь лови https://www.youtube.com/watch?v=2Kuzip-zukY где ты узнаешь, как получить мой подарок, а также ещё больше погрузишься в мир американского YouTube.\n\n'
            f'Длительность <b>всего минута</b>. Нажимай на кнопку и слушай видео <b>внимательно</b>👇\n\n',
            disable_web_page_preview=True,
        parse_mode=ParseMode.HTML,
        reply_markup=get_callback_btns(btns={
        '▶️Смотреть видео': 'https://www.youtube.com/watch?v=2Kuzip-zukY' }))
        await asyncio.sleep(190)
        await callback_query.message.answer(
            f'✅Как и обещал, вот <b>ПОШАГОВАЯ</b> инструкция <b>«Как выйти на доход в 1.000$ с помощью Американского Ютуба за 2 недели🤯»</b>\n\n'
            f'👌В этой инструкции, которую можно прочитать <b>за 5 минут</b>, ты получишь конкретный план действий, и сможешь <b>УЖЕ СЕГОДНЯ</b>, сделать свой первый шаг на Американском Ютубе!\n\n'
            f'❔Хочешь узнать, как сделать YouTube своим <b>основным</b> источником дохода, уделяя этому всего лишь <b>пару часов</b> в день?\n\n'
            f'<b>Читай инструкцию</b> и ты всё поймешь👇\n\n',
        parse_mode=ParseMode.HTML,
        reply_markup=get_callback_btns(btns={
        'Читать инструкцию🔥': 'https://telegra.ph/POSHAGOVAYA-instrukciya-kak-nachat-zarabatyvat-ot-500-na-Amerikanskom-YouTube-v-pervyj-mesyac-05-05-3'}))
        await asyncio.sleep(397)
        await callback_query.message.answer(
            f'<b>Тебе мало инструкции и ты хочешь еще больше топовой информации о Американском ютубе?</b>\n\n'
            f'<b>Хм</b>…хочешь попасть на ЛЕГЕНДАРНОЕ наставничество лично со мной, на котором мои ученики добиваются максимальных результатов за кратчайшие сроки?\n\n'
            f'Ну что, готов раз и навсегда изменить свою жизнь?👇\n\n',
        parse_mode=ParseMode.HTML,
        reply_markup=get_callback_btns(btns={
        '✅ДА': 'yes_{yes}', '❌НЕТ': 'no_{no}'}))
    else:
        await handle_start_subscription_callback(callback_query)

@router.callback_query(Reg.subscribed, F.data.startswith('no_'))
async def handle_no_callback(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(callback_query='no_')
    await state.set_state(Reg.answer_no)
    await callback_query.answer()
    await callback_query.message.answer(
        f'❌<b>Ты совершаешь большую ошибку</b>\n\n'
        f'🙏В начале своего пути, я также как и ты боялся и избегал Американского ютуба\n\n'
        f'❗️Но произошел один важный момент в моей жизни, после которого я поборол свой страх и просто начал действовать\n\n'
        f'В этом видео я рассказал, что мне помогло побороть свой страх и сделать первый шаг👇\n\n'
        f'https://www.youtube.com/watch?v=Y8AM9h6f7XE',
        parse_mode=ParseMode.HTML)
    await asyncio.sleep(120)
    await callback_query.answer()
    await callback_query.message.answer(
        f'😌<b>Скажи честно, узнал себя в этом видео?</b>\n\n'
        f'☝️Да, именно после осознания этих вещей я принял для себя забить на всё и просто погрузиться в Американский ютуб с головой!\n\n'
        f'🙏Это действительно то, чем я хочу заниматься, и чему хочу обучать людей, окружая себя единомышленниками с такими же целями как и у меня\n\n'
        f'💪<b>Ты готов пройти этот путь вместе со мной?</b>\n'
        f'Забить на все страхи и сомнения, и просто сделать инвестицию в себя, в своё будущее\n\n',
        parse_mode=ParseMode.HTML,
        reply_markup=get_callback_btns(btns={
        '🔥Да, я готов': 'yesready_{ready}'}))
    
@router.callback_query(Reg.answer_no, F.data.startswith('yesready_'))
async def handle_no_callback(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(callback_query='yesready_')
    await state.set_state(Reg.Form)
    await callback_query.answer()
    await callback_query.message.answer(
        f'✅<b>Ты сделал правильный выбор, за который скажешь себе «спасибо»</b>\n\n'
        f'👌Заполни анкету пред. записи и получи личный созвон со мной!\n\n'
        f'🔥На созвоне мы разберем конкретно твою ситуацию, а также я расскажу о фишках на Американском ютубе, которые взорвут твой мозг!\n\n'
        f'<b>Заполняй анкету и я с тобой свяжусь</b>👇\n\n',
        parse_mode=ParseMode.HTML,
        reply_markup=get_callback_btns(btns={
        '✅Заполнить анкету':'https://docs.google.com/forms/d/e/1FAIpQLSdgb4a_ACp0k5TGe5__r1HV3XloF6NFE579jfdM12LnMZm8tw/viewform?usp=sf_link'}))
    
@router.callback_query(Reg.subscribed, F.data.startswith('yes_'))
async def handle_yes_callback(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(callback_query='yes_')
    await state.set_state(Reg.Form)
    await callback_query.answer()
    await callback_query.message.answer(
        f'✅<b>Ты сделал правильный выбор, за который скажешь себе «спасибо»</b>\n\n'
        f'👌Заполни анкету пред. записи и получи личный созвон со мной!\n\n'
        f'🔥На созвоне мы разберем конкретно твою ситуацию, а также я расскажу о фишках на Американском ютубе, которые взорвут твой мозг!\n\n'
        f'<b>Заполняй анкету и я с тобой свяжусь</b>👇\n\n',
        parse_mode=ParseMode.HTML,
        reply_markup=get_callback_btns(btns={
        '✅Заполнить анкету':'https://docs.google.com/forms/d/e/1FAIpQLSdgb4a_ACp0k5TGe5__r1HV3XloF6NFE579jfdM12LnMZm8tw/viewform?usp=sf_link'}))
    
