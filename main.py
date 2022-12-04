import telebot
from telebot import types
import math

bot = telebot.TeleBot('5609595965:AAF7qmW9JpzgaCj2Knr5Jh4yhlWfP09aVM4')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>, помогу тебе решить и разобраться с квадратными уравнениями. Найду площадь и периметр разных фигур'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    plosh = types.KeyboardButton('Найти площадь')
    perim = types.KeyboardButton('Найти периметр')
    quadr = types.KeyboardButton('Решение квадратных уравнений')
    markup.add(plosh, perim, quadr)
    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='html')
    func.back = -1


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Решение квадратных уравнений':
        dele = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Образец квадратного уравнения: <b>a</b> * x^2 + <b>b</b> * x + <b>c</b> = 0', parse_mode='html')
        bot.send_message(message.chat.id, 'Введите первый коэффицент (коэффицент <b>a</b>), деситичные дроби вводите через точку', parse_mode='html',
                         reply_markup=dele)
        bot.register_next_step_handler(message, get_a)

    elif message.text == 'Найти площадь':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        treug = types.KeyboardButton('Треугольник')
        pryam = types.KeyboardButton('Прямоугольник')
        paral = types.KeyboardButton('Паралелограмм')
        krug = types.KeyboardButton('Окружность')
        back = types.KeyboardButton('Назад')
        markup.add(treug, pryam, paral, krug, back)
        bot.send_message(message.chat.id, 'Площадь какой фигуры вам нужно найти?', reply_markup=markup,
                         parse_mode='html')
        func.back = 1

    elif message.text == 'Найти периметр':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        treug = types.KeyboardButton('Треугoльник')
        pryam = types.KeyboardButton('Прямоугoльник')
        paral = types.KeyboardButton('Паралелoграмм')
        krug = types.KeyboardButton('Окружнoсть')
        back = types.KeyboardButton('Назад')
        markup.add(treug, pryam, paral, krug, back)
        bot.send_message(message.chat.id, 'Периметр какой фигуры вам нужно найти?', reply_markup=markup,
                         parse_mode='html')
        func.back = 1



    elif message.text == 'Окружнoсть':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        treug = types.KeyboardButton('1. Радиус окружности')
        pryam1 = types.KeyboardButton('2. Диагональ вписанного прямоугольника в оружности или диаметр')
        back = types.KeyboardButton('Назад')
        markup.add(treug, pryam1, back)
        bot.send_message(message.chat.id,
                         'Что вам известно?\n<b>1. Радиус окружности</b>\n<b>2. Диагональ вписанного прямоугольника в оружности или диаметр</b>',
                         reply_markup=markup, parse_mode='html')
        func.back = 2

    elif message.text == 'Назад' and func.back == 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        treug = types.KeyboardButton('Треугoльник')
        pryam = types.KeyboardButton('Прямоугoльник')
        paral = types.KeyboardButton('Паралелoграмм')
        krug = types.KeyboardButton('Окружнoсть')
        back = types.KeyboardButton('Назад')
        markup.add(treug, pryam, paral, krug, back)
        bot.send_message(message.chat.id, 'Периметр какой фигуры вам нужно найти?', reply_markup=markup,
                         parse_mode='html')
        func.back = 1


    elif message.text == '1. Радиус окружности':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-26_18-20-35.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'r — радиус окружности')
        bot.send_message(message.chat.id, 'Введите значение <b>радиуса окржности</b> (отрезок r)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a45)

    elif message.text == '2. Диагональ вписанного прямоугольника в оружности или диаметр':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-26_18-27-48.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'd — диагональ прямоугольника')
        bot.send_message(message.chat.id, 'Введите значение <b>диагонали вписанного прямоугольника в окржности или диаметра</b> (отрезок d)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a46)

    elif message.text == 'Прямоугoльник':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-26_17-56-07.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, ' a, b — соседние стороны прямоугольника')
        bot.send_message(message.chat.id, 'Введите значение <b>одна сторона прямоугольника</b> (сторона a)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a41)
        func.back = 2

    elif message.text == 'Паралелoграмм':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-26_18-11-46.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, ' a, b — соседние стороны паралелограмма')
        bot.send_message(message.chat.id, 'Введите значение <b>одна сторона паралелограмма</b> (сторона a)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a43)
        func.back = 2

    elif message.text == 'Треугoльник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        pryam = types.KeyboardButton('Прямоугoльный')
        ravnost = types.KeyboardButton('Равнoсторонний')
        ravnobedr = types.KeyboardButton('Равнoбедренный')
        luboy = types.KeyboardButton('Любoго вида')
        back = types.KeyboardButton('Назад')
        markup.add(pryam, ravnost, ravnobedr, luboy, back)
        bot.send_message(message.chat.id, 'Какого вида ваш треугольник?', reply_markup=markup, parse_mode='html')
        func.back = 2

    elif message.text == 'Прямоугoльный':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        treug = types.KeyboardButton('1. Катеты треугольника')
        pryam1 = types.KeyboardButton('2. Высoта и боковая сторона')
        back = types.KeyboardButton('Назад')
        markup.add(treug, pryam1, back)
        bot.send_message(message.chat.id,
                         'Что вам известно?\n<b>1. Катеты треугольника</b>\n<b>2. Высота и боковая сторона</b>',
                         reply_markup=markup, parse_mode='html')

    elif message.text == 'Любoго вида':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        treug = types.KeyboardButton('1. Три стороны')
        pryam1 = types.KeyboardButton('2. Площадь и радиус вписанной окружности')
        back = types.KeyboardButton('Назад')
        markup.add(treug, pryam1, back)
        bot.send_message(message.chat.id,
                         'Что вам известно?\n<b>1. Три стороны</b>\n<b>2. Площадь и радиус вписанной окружности</b>',
                         reply_markup=markup, parse_mode='html')

    elif message.text == '1. Катеты треугольника':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-26_12-01-51.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, ' a, b — 2 катета треугольника')
        bot.send_message(message.chat.id, 'Введите значение <b>первый катет треугольника</b> (сторона a)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a37)

    elif message.text == '2. Высoта и боковая сторона':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-26_12-10-43.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, ' a — любой катет треугольника\nc — гипотенуза')
        bot.send_message(message.chat.id, 'Введите значение <b катета треугольника</b> (сторона a)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a39)

    elif message.text == 'Равнoбедренный':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        treug = types.KeyboardButton('1. Бoковая сторона и основание')
        pryam1 = types.KeyboardButton('2. Высoта и боковая сторона')
        back = types.KeyboardButton('Назад')
        markup.add(treug, pryam1, back)
        bot.send_message(message.chat.id,
                         'Что вам известно?\n<b>1. Боковая сторона и основание</b>\n<b>2. Высота и боковая сторона</b>',
                         reply_markup=markup, parse_mode='html')

    elif message.text == '1. Бoковая сторона и основание':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-26_11-27-53.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, ' b — боковая сторона треугольника\na — основание треугольника')
        bot.send_message(message.chat.id, 'Введите значение <b>боковой стороны треугольника</b> (сторона b)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a33)

    elif message.text == '2. Высoта и боковая сторона':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-26_11-40-57.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, ' a — боковая сторона треугольника\nh — основание треугольника')
        bot.send_message(message.chat.id, 'Введите значение <b>боковой стороны треугольника</b> (сторона a)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a35)

    elif message.text == '1. Три стороны':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-26_10-46-31.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, ' a, b, c — длина стороны')
        bot.send_message(message.chat.id, 'Введите значение <b>одной стороны треугольника</b> (сторона a)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a27)

    elif message.text == '2. Площадь и радиус вписанной окружности':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image 2333.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, ' S — площадь\nr — радиус вписанной окружности')
        bot.send_message(message.chat.id, 'Введите значение <b>площади треугольника</b> (величины S)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a30)

    elif message.text == 'Равнoсторонний':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-26_11-19-33.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, ' a - сторона треугольника')
        bot.send_message(message.chat.id, 'Введите значение <b>сторона треугольника</b> (отрезок а)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a32)

    elif message.text == 'Прямоугольник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        treug = types.KeyboardButton('1. Длина и ширина')
        pryam1 = types.KeyboardButton('2. Диагонали и угол меджду ними')
        pryam = types.KeyboardButton('3. Сторона и диагональ')
        back = types.KeyboardButton('Назад')
        markup.add(treug, pryam1, pryam, back)
        bot.send_message(message.chat.id,
                         'Что вам известно?\n<b>1. Длина и ширина</b>\n<b>2. Диагонали и угол меджду ними</b>\n<b>3. Сторона и диагональ</b>',
                         reply_markup=markup, parse_mode='html')
        func.back = 0

    elif message.text == '1. Длина и ширина':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_13-08-25.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, ' a, b — длина и ширина')
        bot.send_message(message.chat.id, 'Введите значение <b>одной стороны прямоугольника</b> (сторона a)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a10)

    elif message.text == '2. Диагонали и угол меджду ними':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_13-18-25.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, ' d — диагональ\nα - угол между диагоналями')
        bot.send_message(message.chat.id, 'Введите значение <b>диагонали прямоугольника</b> (отрезок d)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a12)

    elif message.text == '3. Сторона и диагональ':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_13-27-19.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, ' d — диагональ\na - длина прямоугольника')
        bot.send_message(message.chat.id, 'Введите значение <b>диагонали</b> (отрезок d)', parse_mode='html',
                         reply_markup=dele)
        bot.register_next_step_handler(message, get_a14)

    elif message.text == 'Паралелограмм':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        treug = types.KeyboardButton('1. Основание и высоту')
        pryam1 = types.KeyboardButton('2. Стороны и угол между ними')
        pryam = types.KeyboardButton('3. Диагонали и угол между ними')
        back = types.KeyboardButton('Назад')
        markup.add(treug, pryam1, pryam, back)
        bot.send_message(message.chat.id,
                         'Что вам известно?\n<b>1. Основание и высоту</b>\n<b>2. Стороны и угол между ними</b>\n<b>3. Диагонали и угол между ними</b>',
                         reply_markup=markup, parse_mode='html')
        func.back = 0

    elif message.text == '1. Основание и высоту':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_14-27-19.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, ' a — основание параллелограмма\nh — его высота, проведенная к основанию')
        bot.send_message(message.chat.id, 'Введите значение <b>основания прямоугольника</b> (сторона a)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a16)

    elif message.text == '2. Стороны и угол между ними':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_14-34-37.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'a и b — стороны параллелограмма\nα — угол между сторонами')
        bot.send_message(message.chat.id, 'Введите значение <b>основание прямоугольика</b> (сторона a)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a18)

    elif message.text == '3. Диагонали и угол между ними':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_14-40-35.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'd1 и d2 — диагонали параллелограмма\nα — угол между сторонами')
        bot.send_message(message.chat.id, 'Введите значение <b>одна диагональ</b> (отрезок d1)', parse_mode='html',
                         reply_markup=dele)
        bot.register_next_step_handler(message, get_a21)

    elif message.text == 'Окружность':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        treug = types.KeyboardButton('1. Радиус')
        pryam1 = types.KeyboardButton('2. Диаметр')
        pryam = types.KeyboardButton('3. Длина')
        back = types.KeyboardButton('Назад')
        markup.add(treug, pryam1, pryam, back)
        bot.send_message(message.chat.id,
                         'Что вам известно?\n<b>1. Радиус</b>\n<b>2. Диаметр</b>\n<b>3. Длина</b>',
                         reply_markup=markup, parse_mode='html')
        func.back = 0

    elif message.text == '1. Радиус':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_15-04-40.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'r - радиус окржуности')
        bot.send_message(message.chat.id, 'Введите значение <b>радиуса окржуности</b> (отрезок r)', parse_mode='html',
                         reply_markup=dele)
        bot.register_next_step_handler(message, get_a24)

    elif message.text == '2. Диаметр':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_15-11-45.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'd - диаметр окржуности')
        bot.send_message(message.chat.id, 'Введите значение <b>диамтера окржуности</b> (отрезок d)', parse_mode='html',
                         reply_markup=dele)
        bot.register_next_step_handler(message, get_a25)

    elif message.text == '3. Длина':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_15-16-23.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'L - длина окржуности')
        bot.send_message(message.chat.id, 'Введите значение <b>длины окржуности</b> (L)', parse_mode='html',
                         reply_markup=dele)
        bot.register_next_step_handler(message, get_a26)

    elif message.text == 'Назад' and func.back == 0:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        treug = types.KeyboardButton('Треугольник')
        pryam = types.KeyboardButton('Прямоугольник')
        paral = types.KeyboardButton('Паралелограмм')
        krug = types.KeyboardButton('Окружность')
        back = types.KeyboardButton('Назад')
        markup.add(treug, pryam, paral, krug, back)
        bot.send_message(message.chat.id, 'Площадь какой фигуры вам нужно найти?', reply_markup=markup,
                         parse_mode='html')
        func.back = 1

    elif message.text == 'Треугольник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        pryam = types.KeyboardButton('Прямоугольный')
        ravnost = types.KeyboardButton('Равносторонний')
        ravnobedr = types.KeyboardButton('Равнобедренный')
        luboy = types.KeyboardButton('Любого вида')
        back = types.KeyboardButton('Назад')
        markup.add(pryam, ravnost, ravnobedr, luboy, back)
        bot.send_message(message.chat.id, 'Какого вида ваш треугольник?', reply_markup=markup, parse_mode='html')
        func.back = 0

    elif message.text == 'Назад' and func.back == 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, "Что вам нужно найти?", reply_markup=markup)



    elif message.text == 'Прямоугольный':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        treug = types.KeyboardButton('1. Гипотенуза и высота')
        pryam1 = types.KeyboardButton('2. Два катета')
        pryam = types.KeyboardButton('3. Радиус вписанной окружности и гипотинуза')
        back = types.KeyboardButton('Назад')
        markup.add(treug, pryam1, pryam, back)
        bot.send_message(message.chat.id,
                         'Что вам известно?\n<b>1.Гипотенуза и высота</b>\n<b>2. Два катета</b>\n<b>3. Радиус вписанной окружности и гипотинуза</b>',
                         reply_markup=markup, parse_mode='html')

    elif message.text == 'Любого вида':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        treug = types.KeyboardButton('4. Две стороны треугольника и угол между ними')
        pryam1 = types.KeyboardButton('5. Основание треугольника и высота треугольника')
        pryam2 = types.KeyboardButton('1. Все 3 стороны')
        pryam3 = types.KeyboardButton('2. Все 3 стороны и радиус описанной окружности')
        pryam = types.KeyboardButton('3. Все 3 стороны и радиус вписанной окружности')
        back = types.KeyboardButton('Назад')
        markup.add(pryam2, pryam3, pryam, treug, pryam1, back)
        bot.send_message(message.chat.id,
                         'Что вам известно?\n<b>1. Все 3 стороны</b>\n<b>2. Все 3 стороны и радиус описанной окружности</b>\n<b>3. Все 3 стороны и радиус вписанной окружности</b>\n<b>4. Две стороны треугольника и угол между ними</b>\n<b>5. Основание треугольника и высота треугольника</b>',
                         reply_markup=markup, parse_mode='html')

    elif message.text == '4. Две стороны треугольника и угол между ними':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_03-43-35.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, ' a, b — стороны треугольника\nα — угол между ними')
        bot.send_message(message.chat.id, 'Введите значение <b>одной стороны треугольника</b> (сторона a)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_t)

    elif message.text == '5. Основание треугольника и высота треугольника':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_03-43-50.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'a — основание треугольника\nh — высота треугольника')
        bot.send_message(message.chat.id, 'Введите значение <b>основания треугольника </b> (сторона a)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_w)

    elif message.text == '2. Все 3 стороны и радиус описанной окружности':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_03-44-15.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'a, b, c — стороны треугольника\nR — радиус описанной окружности')
        bot.send_message(message.chat.id, 'Введите значение <b>первой стороны треугольника </b> (сторона b)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_y)

    elif message.text == '3. Все 3 стороны и радиус вписанной окружности':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_03-44-29.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'a, b, c — стороны треугольника\nr — радиус вписанной окружности')
        bot.send_message(message.chat.id, 'Введите значение <b>первой стороны треугольника </b> (сторона a)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a3)

    elif message.text == '1. Все 3 стороны':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_03-44-43.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'a, b, c — стороны треугольника')
        bot.send_message(message.chat.id, 'Введите значение <b>первой стороны треугольника</b> (сторона a)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_a7)

    elif message.text == 'Равнобедренный':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        treug = types.KeyboardButton('1. Основание треугольника и высота, проведенная к основанию')
        pryam1 = types.KeyboardButton('2. Боковая сторона и угол между боковыми сторонами')
        back = types.KeyboardButton('Назад')
        markup.add(treug, pryam1, back)
        bot.send_message(message.chat.id,
                         'Что вам известно?\n<b>1. Основание треугольника и высота, проведенная к основанию</b>\n<b>2. Боковая сторона и угол между боковыми сторонами</b>',
                         reply_markup=markup, parse_mode='html')

    elif message.text == 'Равносторонний':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        treug = types.KeyboardButton('1. Радиус описанной окружности')
        pryam1 = types.KeyboardButton('2. Радиус вписанной окружности')
        pryam = types.KeyboardButton('3. Сторона')
        pryam2 = types.KeyboardButton('4. Высота')
        back = types.KeyboardButton('Назад')
        markup.add(treug, pryam1, pryam, pryam2, back)
        bot.send_message(message.chat.id,
                         'Что вам известно?\n<b>1. Радиус описанной окружности</b>\n<b>2. Радиус вписанной окружности</b>\n<b>3. Сторона</b>\n<b>4. Высота</b>',
                         reply_markup=markup, parse_mode='html')


    elif message.text == '1. Основание треугольника и высота, проведенная к основанию':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_02-16-06.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'b - основание треугольника\nh - высота, проведенная к основанию')
        bot.send_message(message.chat.id, 'Введите значение <b>основание треугольника </b> (сторона b)',
                         parse_mode='html', reply_markup=dele)
        bot.register_next_step_handler(message, get_q)

    elif message.text == '2. Боковая сторона и угол между боковыми сторонами':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-13_02-16-14.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'b - боковая сторона треугольника\nα -  угол между боковыми сторонами')
        bot.send_message(message.chat.id, 'Введите значение <b>основания</b> (сторона b)', parse_mode='html',
                         reply_markup=dele)
        bot.register_next_step_handler(message, get_o)

    elif message.text == '1. Радиус описанной окружности':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-12_23-47-32.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'r - радиус описанной окружности')
        bot.send_message(message.chat.id, 'Введите значение <b>радиуса</b> (отрезок R)', parse_mode='html',
                         reply_markup=dele)
        bot.register_next_step_handler(message, get_j)

    elif message.text == '2. Радиус вписанной окружности':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-12_23-48-23.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'r - радиус вписанной окружности')
        bot.send_message(message.chat.id, 'Введите значение <b>радиуса</b> (отрезок r)', parse_mode='html',
                         reply_markup=dele)
        bot.register_next_step_handler(message, get_k)

    elif message.text == '3. Сторона':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-12_23-48-51.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'a - сторона треугольника')
        bot.send_message(message.chat.id, 'Введите значение <b>стороны треугольника</b> (сторону a)', parse_mode='html',
                         reply_markup=dele)
        bot.register_next_step_handler(message, get_l)

    elif message.text == '4. Высота':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-12_23-49-27.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'h - высота треугольника')
        bot.send_message(message.chat.id, 'Введите значение <b>высоту</b> (отрезок h)', parse_mode='html',
                         reply_markup=dele)
        bot.register_next_step_handler(message, get_m)

    elif message.text == '2. Два катета':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-12_22-32-38.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Введите значение <b>первого катета</b> (сторону CB)', parse_mode='html',
                         reply_markup=dele)
        bot.register_next_step_handler(message, get_d)

    elif message.text == '1. Гипотенуза и высота':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-12_22-57-24.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'a, b - 2 катета\nc - гипотенуза\nh - высота')
        bot.send_message(message.chat.id, 'Введите значение <b>гипотенузы</b> (сторону с)', parse_mode='html',
                         reply_markup=dele)
        bot.register_next_step_handler(message, get_f)

    elif message.text == '3. Радиус вписанной окружности и гипотинуза':
        dele = telebot.types.ReplyKeyboardRemove()
        photo = open('image_2022-11-12_23-11-39.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'r - радиус вписанной окружности\nc - гипотенуза треугольника')
        bot.send_message(message.chat.id, 'Введите значение <b>радиуса</b> (отрезок r)', parse_mode='html',
                         reply_markup=dele)
        bot.register_next_step_handler(message, get_h)


    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, 'Я вас не понимаю 🤯', reply_markup=markup, parse_mode='html')

def get_a46(message):
    try:
        global a46
        a46 = float(message.text)
        s = math.pi * a46
        bot.send_message(message.chat.id, 'Формула нахождения периметр окружности через диагональ окружности (диаметр окружности):')
        photo3 = open('image_2022-11-26_18-31-30.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: P = π * {a46}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Периметр вашей окружности равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению периметра окружности",
                                                url="https://mnogoformul.ru/dlina-okruzhnosti-ili-perimetr-kruga")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить нахождение периметра окружностей ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a46)

def get_a45(message):
    try:
        global a45
        a45 = float(message.text)
        s = 2 * math.pi * a45
        bot.send_message(message.chat.id, 'Формула нахождения периметр окружности через радиус:')
        photo3 = open('image_2022-11-26_18-29-43.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: P = 2 * π * {a45}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Периметр вашей окружности равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению периметра окружности",
                                                url="https://mnogoformul.ru/dlina-okruzhnosti-ili-perimetr-kruga")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить нахождение периметра окружностей ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a45)

def get_a44(message):
    try:
        global a44
        a44 = float(message.text)
        s = 2 * (a43 + a44)
        bot.send_message(message.chat.id, 'Формула нахождения периметра прямоугольника:')
        photo3 = open('image_2022-11-26_18-05-51.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: P = ({a43} + {a44}) * 2')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Периметр вашего паралелограмма равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению периметра паралелограмма",
                                                url="https://www.webmath.ru/poleznoe/formules_15_9.php")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить нахождение периметра паралелограммов ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a44)

def get_a43(message):
    try:
        global a43
        a43 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>второй стороны</b> (сторона b)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a44)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a43)

def get_a42(message):
    try:
        global a42
        a42 = float(message.text)
        s = 2 * (a41 + a42)
        bot.send_message(message.chat.id, 'Формула нахождения периметра прямоугольника:')
        photo3 = open('image_2022-11-26_18-05-51.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: P = ({a41} + {a42}) * 2')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Периметр вашего прямоугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению периметра прямоугольника",
                                                url="https://skysmart.ru/articles/mathematic/perimetr-pryamougolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить нахождение периметра прямоугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a42)

def get_a41(message):
    try:
        global a41
        a41 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>второй стороны</b> (сторона b)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a42)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a41)

def get_a39(message):
    try:
        global a39
        a39 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>гипотенузы треугольника</b> (сторона с)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a40)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a39)

def get_a40(message):
    try:
        global a40
        a40 = float(message.text)
        s = (a40**2 - a39**2)**0.5 + a39 + a40
        bot.send_message(message.chat.id, 'Формула для нахождения периметра прямоугольного треугольника через катети гипотенузу:')
        photo3 = open('image_2022-11-26_12-15-49.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: P = √({a40}² - {a39}²) + {a39} + {a40}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Периметр вашего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению периметра треугольника",
                                                url="https://skysmart.ru/articles/mathematic/perimetr-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить нахождение периметра треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a40)

def get_a37(message):
    try:
        global a37
        a37 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>второй катет треугольника</b> (сторона b)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a38)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a37)

def get_a38(message):
    try:
        global a38
        a38 = float(message.text)
        s = (a37**2 + a38**2)**0.5 + a37 + a38
        bot.send_message(message.chat.id, 'Формула для нахождения периметра прямоугольного треугольника через 2 катета:')
        photo3 = open('image_2022-11-26_12-07-50.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: P = √({a37}² + {a38}²) + {a37} + {a38}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Периметр вашего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению периметра треугольника",
                                                url="https://skysmart.ru/articles/mathematic/perimetr-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить нахождение периметра треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a38)

def get_a36(message):
    try:
        global a36
        a36 = float(message.text)
        s = 2 * (a35**2 - a36**2)**0.5 + 2 * a35
        bot.send_message(message.chat.id, 'Формула для нахождения периметра равнобедренного треугольника через высоту и боковую сторону:')
        photo3 = open('image_2022-11-26_11-44-56.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: P = 2 * √({a35}² - {a36}²) + 2 * {a35}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Периметр вашего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению периметра треугольника",
                                                url="https://skysmart.ru/articles/mathematic/perimetr-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить нахождение периметра треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a36)

def get_a35(message):
    try:
        global a35
        a35 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>высоты теругольника</b> (отрезок h)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a36)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a35)


def get_a34(message):
    try:
        global a34
        a34 = float(message.text)
        s = 2 * a33 + a34
        bot.send_message(message.chat.id, 'Формула для нахождения периметра равнобедренного треугольника через основание и боковую сторону:')
        photo3 = open('image_2022-11-26_11-36-19.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: P = {a34} + 2 * {a33}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Периметр вашего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению периметра треугольника",
                                                url="https://skysmart.ru/articles/mathematic/perimetr-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить нахождение периметра треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a34)

def get_a33(message):
    try:
        global a33
        a33 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>основания теругольника</b> (сторона a)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a34)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a33)

def get_a32(message):
    try:
        global a32
        a32 = float(message.text)
        s = 3 * a32
        bot.send_message(message.chat.id, 'Формула для нахождения периметра равностороннего треугольника:')
        photo3 = open('image_2022-11-26_11-22-45.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: P = 3 * {a32}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Периметр вашего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению периметра треугольника",
                                                url="https://skysmart.ru/articles/mathematic/perimetr-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить нахождение периметра треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a32)

def get_a31(message):
    try:
        global a31
        a31 = float(message.text)
        s = (2 * a30)/a31
        bot.send_message(message.chat.id, 'Формула для нахождения периметра треугольника через площадь и радиус вписанной окружности:')
        photo3 = open('image_2022-11-26_11-12-13.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: P = (2 * {a30}) / {a31}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Периметр вашего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению периметра треугольника",
                                                url="https://skysmart.ru/articles/mathematic/perimetr-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить нахождение периметра треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a31)

def get_a30(message):
    try:
        global a30
        a30 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>радиуса вписанной окружности</b>',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a31)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a30)


def get_a29(message):
    try:
        global a29
        a29 = float(message.text)
        s = a27 + a28 + a29
        bot.send_message(message.chat.id, 'Формула для нахождения периметра треугольника через длины сторон:')
        photo3 = open('image_2022-11-26_11-03-40.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: P = {a27} + {a28} + {a29}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Периметр вашего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению периметра треугольника",
                                                url="https://skysmart.ru/articles/mathematic/perimetr-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить нахождение периметра треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a29)


def get_a28(message):
    try:
        global a28
        a28 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>стороны с</b>',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a29)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a28)

def get_a27(message):
    try:
        global a27
        a27 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>стороны b</b>',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a28)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a27)


def get_a26(message):
    try:
        global a26
        a26 = float(message.text)
        s = a26 ** 2 / 4 * math.pi
        bot.send_message(message.chat.id, 'Формула площади круга через длину окружности:')
        photo3 = open('image_2022-11-13_15-16-36.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S =  {a26}^2 / 4*π')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Площадь вашей окружности равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади окружности",
                                                url="https://ktonanovenkogo.ru/voprosy-i-otvety/ploshchad-parallelogramma-kak-najti-formule.html")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади окружностей ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a26)

def get_a25(message):
    try:
        global a25
        a25 = float(message.text)
        s = math.pi * a25 ** 2 / 4
        bot.send_message(message.chat.id, 'Формула площади круга через диаметр:')
        photo3 = open('image_2022-11-13_15-14-40.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S = π * {a25}^2 / 4')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Площадь вашей окружности равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади окружности",
                                                url="https://ktonanovenkogo.ru/voprosy-i-otvety/ploshchad-parallelogramma-kak-najti-formule.html")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади окружностей ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a25)

def get_a24(message):
    try:
        global a24
        a24 = float(message.text)
        s = math.pi * a24 ** 2
        bot.send_message(message.chat.id, 'Формула площади круга через радиус:')
        photo3 = open('image_2022-11-13_15-10-02.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S = π * {a24}^2')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Площадь вашей окружности равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади окружности",
                                                url="https://ktonanovenkogo.ru/voprosy-i-otvety/ploshchad-parallelogramma-kak-najti-formule.html")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади окружностей ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a24)


def get_a23(message):
    try:
        global a23
        a23 = float(message.text)
        s = 0.5 * a21 * a22 * math.sin(math.radians(a23))
        bot.send_message(message.chat.id,
                         'Формула для нахождения площади параллелограмма через диагонали и угол между ними:')
        photo3 = open('image_2022-11-13_14-42-31.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S = 0.5 * {a21} * {a22} * sin({a23})')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего паралелограмма равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади паралелограмма",
                                                url="https://ktonanovenkogo.ru/voprosy-i-otvety/ploshchad-parallelogramma-kak-najti-formule.html")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади паралелограмма ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a23)

def get_a22(message):
    try:
        global a22
        a22 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>угла между диагоналями</b> (угол α)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a23)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a22)


def get_a21(message):
    try:
        global a21
        a21 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>другой диагонали</b> (отрезок d1)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a22)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a21)


def get_a20(message):
    try:
        global a20
        a20 = float(message.text)
        s = a18 * a19 * math.sin(math.radians(a20))
        bot.send_message(message.chat.id, 'Формула для нахождения площади параллелограмма через стороны и угол между ними')
        photo3 = open('image_2022-11-13_14-38-04.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S = {a18} * {a19} * sin({a20})')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего паралелограмма равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади паралелограмма",
                                                url="https://ktonanovenkogo.ru/voprosy-i-otvety/ploshchad-parallelogramma-kak-najti-formule.html")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади паралелограмма ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a20)


def get_a19(message):
    try:
        global a19
        a19 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>угол между сторонами</b> (угол α)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a20)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a19)


def get_a18(message):
    try:
        global a18
        a18 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>второй стороны прямоугольника</b> (сторона b)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a19)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a18)

def get_a16(message):
    try:
        global a16
        a16 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>высоты прямоугольника</b> (отрезок h)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a17)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a16)


def get_a17(message):
    try:
        global a17
        a17 = float(message.text)
        s = a17 * a16
        bot.send_message(message.chat.id, 'Формула для нахождения площади параллелограмма через основание и высоту:')
        photo3 = open('image_2022-11-13_14-30-52.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S = {a16} * {a17}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего паралелограмма равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади паралелограмма",
                                                url="https://ktonanovenkogo.ru/voprosy-i-otvety/ploshchad-parallelogramma-kak-najti-formule.html")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади паралелограмма ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a17)

def get_a14(message):
    try:
        global a14
        a14 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>известной стороны прямоугольника</b> (сторона a или b)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a15)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a14)

def get_a15(message):
    try:
        global a15
        a15 = float(message.text)
        s = a15 * (a14 ** 2 * a15 ** 2) ** 0.5
        bot.send_message(message.chat.id, 'Формула нахождения площади для прямоугольника по диагонали и известной стороне:')
        photo3 = open('image_2022-11-13_13-34-40.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S = {a15} * √({a14}^2 * {a15}^2)')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего прямоугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади прямоугольника",
                                                url="https://skysmart.ru/articles/mathematic/Kak-nayti-ploshchad'-pryamougol'nika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади прямоугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a15)

def get_a12(message):
    try:
        global a12
        a12 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>угла между диагоналями</b> (угол 𝑎)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a13)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a12)


def get_a13(message):
    try:
        global a13
        a13 = float(message.text)
        s = 0.5 * a12 ** 2 * math.sin(math.radians(a13))
        bot.send_message(message.chat.id,
                         'Формула нахождения площади для четырехугольников по диагоналям и углу между ними:')
        photo3 = open('image_2022-11-13_13-44-26.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S = 0.5 * {a12} * {a12} * sin({a13})')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего прямоугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади прямоугольника",
                                                url="https://skysmart.ru/articles/mathematic/Kak-nayti-ploshchad'-pryamougol'nika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади прямоугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a13)

def get_a10(message):
    try:
        global a10
        a10 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>второй стороны треугольника</b> (сторона b)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a11)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a10)


def get_a11(message):
    try:
        global a11
        a11 = float(message.text)
        s = a10 * a11
        bot.send_message(message.chat.id,
                         'Формула для нахождения площади прямоугольника через произведение его длины и ширины:')
        photo3 = open('image_2022-11-13_13-16-17.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S = {a10} * {a11}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего прямоугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади прямоугольника",
                                                url="https://skysmart.ru/articles/mathematic/Kak-nayti-ploshchad'-pryamougol'nika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади прямоугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a11)


def get_a9(message):
    try:
        global a9
        a9 = float(message.text)
        p = (a9 * a8 * a7) / 2
        s = (p * (p - a7) * (p - a8) * (p - a9)) ** 0.5
        bot.send_message(message.chat.id,
                         'Формула для нахождения площади треугольника через вписанную окружность и стороны:')
        photo3 = open('image_2022-11-13_03-57-41.png', 'rb')
        bot.send_message(message.chat.id,
                         'Вторая формула для нахождения полупериметра')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id,
                         f'Подставляем значения:p = ({a7} * {a8} * {a9}) / 2\nS = √({p} * ({p}-{a7}) * ({p}-{a8}) * ({p}-{a9}))')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади треугольника",
                                                url="https://skysmart.ru/articles/mathematic/ploshad-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a9)

def get_a8(message):
    try:
        global a8
        a8 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>третья сторона треугольника</b> (сторона c)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a9)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a8)

def get_a7(message):
    try:
        global a7
        a7 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>вторая сторона треугольника</b> (сторона b)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a8)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a7)


def get_a6(message):
    try:
        global a6
        a6 = float(message.text)
        s = a6 * (a3 * a4 * a5) / 2
        bot.send_message(message.chat.id,
                         'Формула для нахождения площади треугольника через вписанную окружность и стороны:')
        photo3 = open('image_2022-11-13_03-57-19.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S = {a6} * ({a3} * {a4} * {a5}) / 2 ')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади треугольника",
                                                url="https://skysmart.ru/articles/mathematic/ploshad-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a6)


def get_a5(message):
    try:
        global a5
        a5 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>радиус вписанной окружности</b> (отрезок r)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a6)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a5)


def get_a4(message):
    try:
        global a4
        a4 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>третья сторона треугольника</b> (сторона c)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a5)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a4)

def get_a3(message):
    try:
        global a3
        a3 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>вторая сторона треугольника</b> (сторона b)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a4)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a3)


def get_y(message):
    try:
        global y
        y = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>вторая сторона треугольника</b> (сторона a)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_z)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_y)

def get_z(message):
    try:
        global z
        z = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>третья сторона треугольника</b> (сторона c)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a1)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_z)


def get_a1(message):
    try:
        global a1
        a1 = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>радиус описанной окружности</b> (отрезок R)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_a2)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a1)


def get_a2(message):
    try:
        global a2
        a2 = float(message.text)
        s = (z * y * a1) / 4 * a2
        bot.send_message(message.chat.id,
                         'Формула для нахождения площади треугольника через описанную окружность и стороны:')
        photo3 = open('image_2022-11-13_03-57-08.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S =  ({z} * {y} * {a1}) / 4 * {a2}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади треугольника",
                                                url="https://skysmart.ru/articles/mathematic/ploshad-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_a2)

def get_w(message):
    try:
        global w
        w = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>высота треугольника</b> (отрезок h)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_x)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_w)


def get_x(message):
    try:
        global x
        x = float(message.text)
        s = 0.5 * w * x
        bot.send_message(message.chat.id, 'Формула для нахождения площади треугольника через основание и высоту:')
        photo3 = open('image_2022-11-13_03-56-55.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S =  0.5 * {w} * {x}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади треугольника",
                                                url="https://skysmart.ru/articles/mathematic/ploshad-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_x)


def get_t(message):
    try:
        global t
        t = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>второй стороны</b> (отрезок b)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_u)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_t)

def get_u(message):
    try:
        global u
        u = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>угол между ними</b> (угол α)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_v)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_u)

def get_v(message):
    try:
        global v
        v = float(message.text)
        s = 0.5 * t * u * math.sin(math.radians(v))
        bot.send_message(message.chat.id, 'Формула для нахождения площади треугольника через 2 стороны и угол:')
        photo3 = open('image_2022-11-13_03-56-41.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S =  0.5 * {t} * {u} * sin({v})')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади треугольника",
                                                url="https://skysmart.ru/articles/mathematic/ploshad-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_v)

def get_q(message):
    try:
        global q
        q = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>высоты</b> (отрезок h)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_r)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_q)

def get_r(message):
    try:
        global r
        r = float(message.text)
        s = 0.5 * q * r
        bot.send_message(message.chat.id, 'Формула площади равнобедренного треугольника через основание и высоту:')
        photo3 = open('image_2022-11-13_02-29-02.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S = 0.5 * {q} * {r}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего равнобедренного треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади треугольника",
                                                url="https://skysmart.ru/articles/mathematic/ploshad-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_r)

def get_o(message):
    try:
        global o
        o = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>угла</b> (угол α)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_p)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_o)

def get_p(message):
    try:
        global p
        p = float(message.text)
        s = 0.5 * o ** 2 * math.sin(math.radians(p))
        bot.send_message(message.chat.id,
                         'Формула площади равнобедренного треугольника через боковые стороны и угол между ними:')
        photo3 = open('image_2022-11-13_02-40-19.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S =  0.5 * {o}^2 * sin({p}°)')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего равнобедренного треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади треугольника",
                                                url="https://skysmart.ru/articles/mathematic/ploshad-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_p)

def get_m(message):
    try:
        global m
        m = float(message.text)
        s = m ** 2 / math.sqrt(3)
        bot.send_message(message.chat.id, 'Формула площади равностороннего треугольника через высоту:')
        photo3 = open('image_2022-11-13_00-13-11.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S =  {m}^2 / √3')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего равностороннего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади треугольника",
                                                url="https://skysmart.ru/articles/mathematic/ploshad-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_m)

def get_l(message):
    try:
        global l
        l = float(message.text)
        s = math.sqrt(3) * l ** 2 / 4
        bot.send_message(message.chat.id, 'Формула площади равностороннего треугольника через сторону:')
        photo3 = open('image_2022-11-13_00-12-43.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S = √3 * {l}^2 / 4')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего равностороннего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади треугольника",
                                                url="https://skysmart.ru/articles/mathematic/ploshad-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_l)

def get_k(message):
    try:
        global k
        k = float(message.text)
        s = 3 * math.sqrt(3) * k ** 2
        bot.send_message(message.chat.id, 'Формула площади равностороннего треугольника через радиус вписанной окружности:')
        photo3 = open('image_2022-11-13_00-02-09.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S = 3 * √3 * {k}^2')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего равностороннего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади треугольника",
                                                url="https://skysmart.ru/articles/mathematic/ploshad-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_k)


def get_j(message):
    try:
        global j
        j = float(message.text)
        s = (3 * math.sqrt(3) * j ** 2) / 4
        bot.send_message(message.chat.id, 'Формула площади равностороннего треугольника через радиус описанной окружности:')
        photo3 = open('image_2022-11-13_00-00-47.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S = 3 * √3 * {j}^2 / 4')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего равностороннего треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади треугольника",
                                                url="https://skysmart.ru/articles/mathematic/ploshad-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_j)

def get_h(message):
    try:
        global h
        h = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>гипотинузы</b> (сторону c)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_i)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_h)

def get_i(message):
    try:
        global i
        i = float(message.text)
        s = h * (h * i)
        bot.send_message(message.chat.id,
                         'Формула для нахождения площади прямоугольного треугольника по радиусу вписанной окружности и гипотенузе:')
        photo3 = open('image_2022-11-12_23-07-56.png', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f'Подставляем значения: S = {h} * ({h} * {i})')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего прямоугольного треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади треугольника",
                                                url="https://skysmart.ru/articles/mathematic/ploshad-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_i)


def get_f(message):
    try:
        global f
        f = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>высоты</b> (отрезок h)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_g)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (к примеру 3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_f)


def get_g(message):
    try:
        global g
        g = float(message.text)
        s = 0.5 * f * g
        bot.send_message(message.chat.id,
                         'Площадь прямоугольного треугольника равна половине произведения гипотенузы на высоту, проведенную к гипотенузе. Из этого выходит такая формула:')
        photo2 = open('image_2022-11-12_23-07-56.png', 'rb')
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, f'Подставляем значения: S = 0.5 * {f} * {g}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего прямоугольного треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади треугольника",
                                                url="https://skysmart.ru/articles/mathematic/ploshad-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (к примеру 3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_g)


def get_d(message):
    try:
        global d
        d = float(message.text)
        bot.send_message(message.chat.id, 'Введите значение <b>второго катета</b> (сторону AC)',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_e)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_d)


def get_e(message):
    try:
        global e
        e = float(message.text)
        s = 0.5 * d * e
        bot.send_message(message.chat.id,
                         'Площадь треугольника равна половине произведения основания на высоту, проведенную к этому основанию. Из этого выходит такая формула:')
        photo1 = open('image_2022-11-12_22-35-11.png', 'rb')
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, f'Подставляем значения: S = 0.5 * {d} * {e}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id,
                         f'Площадь вашего прямоугольного треугольника равна <b>{round(s, 2)}</b>🎀 (Ответ округлен до сотых)',
                         reply_markup=markup, parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по нахождению площади треугольника",
                                                url="https://skysmart.ru/articles/mathematic/ploshad-treugolnika")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить площади треугольников ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)
    except ValueError:
        mess = '<b>Можно вводить только простые числа или десятичные дроби через точку (3.6).</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите значение еще раз 🔁', parse_mode='html')
        bot.register_next_step_handler(message, get_e)


def get_a(message):
    try:
        global a
        a = float(message.text)
        bot.send_message(message.chat.id, 'Введите второй коэффицент вашего уравнения (коэффицент <b>b</b>), деситичные дроби вводите через точку',
                         parse_mode='html')
        bot.register_next_step_handler(message, get_b)
    except ValueError:
        mess = '<b>Можно вводить только числа, попробуйте ввести уравнение еще раз</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите первый коэффицент вашего уравнения (коэффицент <b>a</b>), деситичные дроби вводите через точку', parse_mode='html')
        bot.register_next_step_handler(message, get_a)



def get_b(message):
    try:
        global b
        b = float(message.text)
        bot.send_message(message.chat.id, 'Введите последний коэффицент (коэффицент <b>c</b>), деситичные дроби вводите через точку', parse_mode='html')
        bot.register_next_step_handler(message, get)
    except ValueError:
        mess = '<b>Можно вводить только числа, попробуйте ввести уравнение еще раз</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите второй коэффицент (коэффицент <b>b</b>), деситичные дроби вводите через точку', parse_mode='html')
        bot.register_next_step_handler(message, get_b)


def get(message):
    try:
        global n
        n = float(message.text)
        d = (b ** 2 - 4 * a * n)
        photo1 = open('image_2022-11-13_01-09-01.png', 'rb')
        bot.send_photo(message.chat.id, photo1)

        if d > 0:
            bot.send_message(message.from_user.id,
                             f'Подставляем значения: <b>D = {b}^2 - 4 * {a} * {n}</b> Дискриминант (D) будет равен <b>{d}</b>\n<b>Формула вычисления корней</b> выглядит так:',
                             parse_mode='html')
            photo1 = open('image_2022-11-13_01-18-50.png', 'rb')
            bot.send_photo(message.chat.id, photo1)
            x1 = (-b + math.sqrt(d)) / 2 * a
            x2 = (-b - math.sqrt(d)) / 2 * a
            mess = f'Подставляем значения:\nВычисляем первый корень: x1 = -{b} + √{d} / 2 * {a}\nВычисляем второй корень: x2 = -{b} - √{d} / 2 * {a}\nПервый корень {round(x1, 2)}, Второй корень {round(x2, 2)}'
        elif d == 0:
            bot.send_message(message.from_user.id,
                             f'Подставляем значения: <b>D = {b}^2 - 4 * {a} * {n}</b> Дискриминант (D) будет равен <b>{d}</b>\n<b>Формула вычисления корней</b> выглядит так:',
                             parse_mode='html')
            x = (-b) / 2 * a
            photo1 = open('image_2022-11-13_01-18-50.png', 'rb')
            bot.send_photo(message.chat.id, photo1)
            mess = f'Единственный корень {round(x, 2)}'
        elif d < 0:
            bot.send_message(message.from_user.id,
                             f'Подставляем значения: <b>D = {b}^2 - 4 * {a} * {n}</b> Дискриминант (D) будет равен <b>{d}</b>\nЗначит корней нет',
                             parse_mode='html')
            mess = 'Корней нет'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        plosh = types.KeyboardButton('Найти площадь')
        perim = types.KeyboardButton('Найти периметр')
        quadr = types.KeyboardButton('Решение квадратных уравнений')
        markup.add(plosh, perim, quadr)
        bot.send_message(message.chat.id, f'Ваш ответ: <b>{mess}</b>🎀 (Ответ округлен до сотых)', reply_markup=markup,
                         parse_mode='html')
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Подробный курс по квадратным уравнениям",
                                                url="https://skysmart.ru/articles/mathematic/kak-reshat-kvadratnye-uravneniya")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Подробнее изучить квадратные уравнения ты можешь нажав на кнопку ниже! 🤩",
                         reply_markup=keyboard)

    except ValueError:
        mess = '<b>Можно вводить только числа, попробуйте ввести уравнение еще раз</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, 'Введите последний коэффицент (коэффицент <b>c</b>), деситичные дроби вводите через точку', parse_mode='html')
        bot.register_next_step_handler(message, get)

# @bot.message_handler()
# def get_user_text(message):
#    if message.text == 'Теорема Пифагора':
#        bot.send_message(message.chat.id, '<b>a² + b² = c²</b>', parse_mode='html')
#        photo = open('image_2022-11-12_17-50-50.png', 'rb')
#        bot.send_photo(message.chat.id, photo)
#    elif message.text == 'id':
#        bot.send_message(message.chat.id, f'Твой id:{message.from_user.id}', parse_mode='html')
#    except ValueError:
#        bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')


bot.polling(non_stop=True)
