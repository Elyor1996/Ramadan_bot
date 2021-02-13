from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,  ConversationHandler, MessageHandler, Filter
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ConversationHandler, MessageHandler, Filter

BNT_TODAY, BNT_TOMORROW, BNT_MONTH, BNT_REGION, BNT_DUA = ('⏳Bugun','⏳Ertaga', '🗓To`liq taqvim','📍Mintaqa','🤲Duo')

main_buttons = ReplyKeyboardMarkup([
    ['⏳Bugun'], ['⏳Ertaga', '🗓To`liq taqvim'], ['📍Mintaqa'], ['🤲Duo']], resize_keyboard=True)

STATE_REGION = 1
STATE_CALENDAR = 2

def start(update, context):
    user = update.message.from_user
    buttons = [
        [
            InlineKeyboardButton('Toshkent', callback_data='region_1'),
            InlineKeyboardButton('Andijon', callback_data='region_2'),
        ]
    ]

    update.message.reply_html('Assalomu alaykum <b>{}!</b>\n \n<b>Razmazon oyi muborak bo`lsin</b>\n \nSiz yashaydigan mintaqani tanlang'.format(user.first_name), reply_markup=InlineKeyboardMarkup(buttons))

def inline_callback(update, context):
    try:
        query = update.callback_query
        query.message.delete()
        query.message.reply_html(text='<b>Ramazon Taqvimi</b> 2️⃣0️⃣2️⃣1️⃣\n \n Quydagilardan birini tanlang', reply_markup=main_buttons)
    except Exception as e:
        print('error', str(e))

def calendar_today(update, context):
    update.messange.reply_text('Bugun belgilandi')
def calendar_tomorrow(update, context):
    update.messange.reply_text('Erta belgilandi')
def calendar_month(update, context):
    update.messange.reply_text('To`liq taqvim belgilandi')
def sellect_region(update, context):
    update.messange.reply_text('Mintaqa tanlandi')

def main():
    #Updaterni o`rnatib olamiz
    updater = Updater('1632930191:AAEE_V4G8slR2yS0TuMtSbt4CEGZLgtv8SI', use_context=True)

    #dispatcher eventlarni aniqlash uchun 
    dispatcher = updater.dispatcher

    #start kommandasini ushlab qolish
    dispatcher.add_handler(CommandHandler('start', start))

    #inline button query
    dispatcher.add_handler(CallbackQueryHandler(inline_callback))

    conv_hendler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states={
            STATE_REGION: [CallbackQueryHandler(inline_callback)],
            STATE_CALENDAR: [
                    MessageHandler(Filter.regex('^('+BNT_TODAY+')$'),)

            ]
        }
    )

    updater.start_polling()
    updater.idle()

main()

