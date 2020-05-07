import telebot
import requests

from telebot import types

# Токен
bot = telebot.TeleBot('928630982:AAEewJgBYT1W1lI11wt5p4KcsGUrgpP5Wyc')


# Обновление бота
def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


# Помощь
@bot.message_handler(commands=['help'])
def help(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Тебе нужно выбрать исполнителя и перейти по ссылке")


# Старт
@bot.message_handler(commands=['start'])
def welcome(message):
    # Создание кнопок на панели
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎧 Выбрать жанр")

    markup.add(item1)

    # Приветствие
    bot.send_message(message.chat.id,
                     "Хей, {0.first_name}!\nНажимай на кнопку снизу и погнали!".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


# Ответы на кнопки
@bot.message_handler(content_types=['text'])
def repeat(message):
    if message.chat.type == 'private':
        if message.text == '🎧 Выбрать жанр':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item100 = types.InlineKeyboardButton("RAP 🎤", callback_data='rap')

            markup.add(item100)

            bot.send_message(message.chat.id, ' Выберите жанр:', reply_markup=markup)

        else:
            bot.send_message(message.chat.id,
                             'Я не понял что ты имел ввиду,\nесли нужна помощь то можешь написать /help')


# Кнопки с ссылками
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'rap':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item102 = types.InlineKeyboardButton("RUS 🇷🇺", callback_data='rus')
                item103 = types.InlineKeyboardButton("USA 🇺🇸", callback_data='usa')

                markup.add(item102, item103)

                bot.send_message(call.message.chat.id, 'Вот полный список:', reply_markup=markup)

            if call.message:
                if call.data == 'rus':
                    # Создание кнопок с альбомами
                    markup = types.InlineKeyboardMarkup(row_width=3)
                    item2 = types.InlineKeyboardButton("GONE.Fludd", callback_data='fludd')
                    item3 = types.InlineKeyboardButton("GOODY", callback_data='goody')
                    item6 = types.InlineKeyboardButton("Morgenstern", callback_data='morgen')
                    item15 = types.InlineKeyboardButton("Boulevard Depo", callback_data='depo')
                    item12 = types.InlineKeyboardButton("ПЛАТИНА", callback_data='plat')
                    item14 = types.InlineKeyboardButton("OG BUDA", callback_data='buda')
                    item4 = types.InlineKeyboardButton("LiL Krystalll", callback_data='krystall')
                    item17 = types.InlineKeyboardButton("CAKEBOY", callback_data='cakeboy')
                    item18 = types.InlineKeyboardButton("Элджей", callback_data='ld')
                    item19 = types.InlineKeyboardButton("GSPD", callback_data='gspd')
                    item20 = types.InlineKeyboardButton("JABO", callback_data='jabo')
                    item21 = types.InlineKeyboardButton("VTORNIK", callback_data='vtornik')
                    item22 = types.InlineKeyboardButton("JOSODO", callback_data='joso')
                    item23 = types.InlineKeyboardButton("MANNY", callback_data='manny')
                    item26 = types.InlineKeyboardButton("Big Baby Tape", callback_data='bbt')
                    item27 = types.InlineKeyboardButton("Blago white", callback_data='blago')
                    item28 = types.InlineKeyboardButton("FACE", callback_data='face')
                    item33 = types.InlineKeyboardButton("LIZER", callback_data='lizer')
                    item34 = types.InlineKeyboardButton("KIZARU", callback_data='kizar')
                    item35 = types.InlineKeyboardButton("PHARAOH", callback_data='phara')
                    item42 = types.InlineKeyboardButton("Скриптонит", callback_data='script')

                    markup.add(item2, item3, item6, item15, item4, item12, item14, item17, item18, item19, item20,
                               item21, item22, item23, item26, item27, item28, item33, item34, item35, item42)

                    bot.send_message(call.message.chat.id, 'Вот полный список:', reply_markup=markup)

                if call.message:
                    if call.data == 'fludd':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками GONE.Fludd 👇\nhttps://t.me/gonefluddmusichart')
                if call.message:
                    if call.data == 'goody':
                        bot.send_message(call.message.chat.id, 'Это канал с треками GOODY 👇\nhttps://t.me/goody_sound')
                if call.message:
                    if call.data == 'morgen':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками Моргенштерна 👇\nhttps://t.me/morgenstern_music')
                if call.message:
                    if call.data == 'depo':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками Бульвара Депо 👇\nhttps://t.me/boulevard_depo_music_chart')
                if call.message:
                    if call.data == 'plat':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками ПЛАТИНЫ 👇\nhttps://t.me/platina_music')
                if call.message:
                    if call.data == 'buda':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками OG BUDA 👇\nhttps://t.me/og_buda_music')
                if call.message:
                    if call.data == 'krystall':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками LiL Krystalll 👇\nhttps://t.me/lil_krystalll_music')
                if call.message:
                    if call.data == 'cakeboy':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками CAKEBOY 👇\nhttps://t.me/cakeboy_music_chart')
                if call.message:
                    if call.data == 'ld':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками Элджея 👇\nhttps://t.me/eljay_music')
                if call.message:
                    if call.data == 'gspd':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками GSPD 👇\nhttps://t.me/gspd_music_chart')
                if call.message:
                    if call.data == 'jabo':
                        bot.send_message(call.message.chat.id, 'Это канал с треками JABO 👇\nhttps://t.me/jabo_music')
                if call.message:
                    if call.data == 'vtornik':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками VTORNIK 👇\nhttps://t.me/vtornik_music')
                if call.message:
                    if call.data == 'joso':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками JOSODO 👇\nhttps://t.me/josodo_music')
                if call.message:
                    if call.data == 'manny':
                        bot.send_message(call.message.chat.id, 'Это канал с треками MANNY 👇\nhttps://t.me/manny_music')
                if call.message:
                    if call.data == 'bbt':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками Big Baby Tape 👇\nhttps://t.me/big_baby_tape_music')
                if call.message:
                    if call.data == 'blago':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками Blago White 👇\nhttps://t.me/blago_white')
                if call.message:
                    if call.data == 'face':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками FACE 👇\nhttps://t.me/face_music_trap')
                if call.message:
                    if call.data == 'lizer':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками LIZER 👇\nhttps://t.me/lizer_music_rap')
                if call.message:
                    if call.data == 'kizar':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками KIZARU 👇\nhttps://t.me/kizaru_music_rap')
                if call.message:
                    if call.data == 'phara':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками PHARAOH 👇\nhttps://t.me/pharaoh_music_rap')
                if call.message:
                    if call.data == 'scrit':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками Скриптонита 👇\nhttps://t.me/scriptonit')

            if call.message:
                if call.data == 'usa':
                    markup = types.InlineKeyboardMarkup(row_width=2)
                    item7 = types.InlineKeyboardButton("Lil Peep", callback_data='peep')
                    item16 = types.InlineKeyboardButton("Lil Tecca", callback_data='tecca')
                    item24 = types.InlineKeyboardButton("Trippie Redd", callback_data='trip')
                    item25 = types.InlineKeyboardButton("Post Malone", callback_data='post')
                    item29 = types.InlineKeyboardButton("Scarlxrd", callback_data='scar')
                    item30 = types.InlineKeyboardButton("Joji", callback_data='joji')
                    item31 = types.InlineKeyboardButton("Xxxtentacion", callback_data='xxx')
                    item32 = types.InlineKeyboardButton("Drake", callback_data='drake')
                    item36 = types.InlineKeyboardButton("Lil Uzi Vert", callback_data='uzi')
                    item43 = types.InlineKeyboardButton("The Weeknd", callback_data='week')
                    markup.add(item7, item16, item24, item25, item29, item30, item31, item32, item36, item43)

                    bot.send_message(call.message.chat.id, 'Вот полный список:', reply_markup=markup)

                if call.message:
                    if call.data == 'peep':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками LiL Peepa 👇\nhttps://t.me/lil_peep_music_chart')
                if call.message:
                    if call.data == 'tecca':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками LiL Krystalll 👇\nhttps://t.me/lil_tecca_music')
                if call.message:
                    if call.data == 'trip':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками Trippie Redd 👇\nhttps://t.me/trippie_redd_music_chart')
                if call.message:
                    if call.data == 'post':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками Post Malone 👇\nhttps://t.me/Post_Malone_music')
                if call.message:
                    if call.data == 'scar':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками Post Scarlxrd 👇\nhttps://t.me/Scarlxrd_music_chart')
                if call.message:
                    if call.data == 'joji':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками Joji 👇\nhttps://t.me/joji_music_chart')
                if call.message:
                    if call.data == 'xxx':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками Xxxtentacion 👇\nhttps://t.me/tentacion_music')
                if call.message:
                    if call.data == 'drake':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками Drake 👇\nhttps://t.me/drake_music_rap')
                if call.message:
                    if call.data == 'uzi':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками Lil Uzi Vert 👇\nhttps://t.me/wehieee')
                if call.message:
                    if call.data == 'week':
                        bot.send_message(call.message.chat.id,
                                         'Это канал с треками The Weeknd 👇\nhttps://t.me/Weeknd_music_chart')


    except Exception as e:
        print(repr(e))


# Запуск
bot.polling(none_stop=True)
