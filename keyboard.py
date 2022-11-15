from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🇺🇿 Uz'),
            KeyboardButton(text='🇷🇺 Ru'),
            KeyboardButton(text='🇺🇸 En')
        ]
    ],
    resize_keyboard=True
)

uzmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📚 Badiiy'),
            KeyboardButton(text='📚 Fantastika'),
            KeyboardButton(text='📚 Mistika'),
        ],
        [
            KeyboardButton(text='📚 Biznes'),
            KeyboardButton(text='📚 Fan'),
            KeyboardButton(text='📚 Diniy'),
        ],
        [
            KeyboardButton(text='⏪')
        ]
    ],
    resize_keyboard=True
)
badiiy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Jannatga taklifnoma'),
            KeyboardButton(text='Yo‘qolgan dunyo'),
        ],
        [
            KeyboardButton(text='Yarim asr daftari'),
            KeyboardButton(text='Uilyam Folkner. Qora musiqa'),
        ],
        [
            KeyboardButton(text='Seni jannatda kutaman'),
            KeyboardButton(text='Yevgeniy Onegin'),
        ],
        [
            KeyboardButton(text='⏪ Orqaga')
        ]
    ],
    resize_keyboard=True
)
fantastika = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Gulliverning sayohatlar'),
            KeyboardButton(text='Iblis va Prim xonim'),
        ],
        [
            KeyboardButton(text='Qiyofa o‘g‘risi'),
            KeyboardButton(text='Mixail Bulgakov. Ityurak'),
        ],
        [
            KeyboardButton(text='⏪ Orqaga')
        ]
    ],
    resize_keyboard=True
)
mistika = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='O‘z-o‘zini gipnozlash'),
            KeyboardButton(text='Ruh sirlari'),
        ],
        [
            KeyboardButton(text='⏪ Orqaga')
        ]
    ],
    resize_keyboard=True
)
biznes = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Menejment nazariyasi'),
            KeyboardButton(text='Milliy va jahon iqtisodiyoti'),
        ],
        [
            KeyboardButton(text='Koronavirus va biznes'),
            KeyboardButton(text='Biznes reja tuzish qo‘llanmasi'),
        ],
        [
            KeyboardButton(text='⏪ Orqaga')
        ]
    ],
    resize_keyboard=True
)
fan = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Husnixat - Arab alifbosi'),
            KeyboardButton(text='Anorganik Kimyo')
        ],
        [
            KeyboardButton(text='Fanlar majmuasi'),
            KeyboardButton(text='Falsafa va fan metodologiyasi'),
        ],
        [
            KeyboardButton(text='Elementar matematika qo\'llanma'),
        ],
        [
            KeyboardButton(text='⏪ Orqaga')
        ]
    ],
    resize_keyboard=True
)
diniy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Imom G‘azzoliy. Qirq hadisi qudsiy'),
            KeyboardButton(text='Keng rizq va baraka omillari')
        ],
        [
            KeyboardButton(text='Tajvid qoidalari'),
            KeyboardButton(text='Ilm olish sirlari'),
        ],
        [
            KeyboardButton(text='Ulamolar nazdida vaqtning qadri'),
        ],
        [
            KeyboardButton(text='⏪ Orqaga')
        ]
    ],
    resize_keyboard=True
)
rumenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📚 Художественное'),
            KeyboardButton(text='📚 Фантастика'),
            KeyboardButton(text='📚 Мистика'),
        ],
        [
            KeyboardButton(text='📚 Бизнес'),
            KeyboardButton(text='📚 Наука'),
            KeyboardButton(text='📚 Религия'),
        ],
        [
            KeyboardButton(text='⏪')
        ]
    ],
    resize_keyboard=True
)
xudojestvennoe = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Под Куполом'),
            KeyboardButton(text='Побег из лагеря смерти')
        ],
        [
            KeyboardButton(text='Александр Дюма. Железная маска'),
            KeyboardButton(text='Что сказал покойник'),
        ],
        [
            KeyboardButton(text='⏪ Назад')
        ]
    ],
    resize_keyboard=True
)
misticheskoe = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Осознаное сновидение'),
            KeyboardButton(text='Черная и белая магия')
        ],
        [
            KeyboardButton(text='⏪ Назад')
        ]
    ],
    resize_keyboard=True
)
fantasticheskoe = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Белая чума'),
            KeyboardButton(text='Игра престолов')
        ],
        [
            KeyboardButton(text='Инвиктус'),
            KeyboardButton(text='Полный газ')
        ],
        [
            KeyboardButton(text='⏪ Назад')
        ]
    ],
    resize_keyboard=True
)
biznesSs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Артем Сенаторов. Бизнес в Instagram'),
            KeyboardButton(text='Яндекс. Книга'),
        ],
        [
            KeyboardButton(text='Психология трейдинга'),
            KeyboardButton(text='Разумный инвестор')
        ],
        [
            KeyboardButton(text='Марина Могилко. Как стать блогером')
        ],
        [
            KeyboardButton(text='⏪ Назад')
        ]
    ],
    resize_keyboard=True
)
nauka = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Астрономия'),
            KeyboardButton(text='Квантовая случайность'),
        ],
        [
            KeyboardButton(text='Удивительная солнечная система'),
            KeyboardButton(text='Одиноки ли мы во вселенной')
        ],
        [
            KeyboardButton(text='⏪ Назад')
        ]
    ],
    resize_keyboard=True
)
religiya = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ежедневные сунны'),
            KeyboardButton(text='Аль-Кабаир'),
        ],
        [
            KeyboardButton(text='Ученные в Исламе'),
            KeyboardButton(text='Собрания в месяц Рамадан')
        ],
        [
            KeyboardButton(text='Рассказы о пророках')
        ],
        [
            KeyboardButton(text='⏪ Назад')
        ]
    ],
    resize_keyboard=True
)


enmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📚 Contemporary'),
            KeyboardButton(text='📚 Politician'),
            KeyboardButton(text='📚 History'),
            KeyboardButton(text='📚 Business')
        ],
        [
            KeyboardButton(text='⏪')
        ]
    ],
    resize_keyboard=True
)

contemporary = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='The labors of Hercules'),
            KeyboardButton(text='The butterfly project'),
        ],
        [
            KeyboardButton(text='Lost Girl'),
            KeyboardButton(text='Paranoid')
        ],
        [
            KeyboardButton(text='⏪ Back')
        ]
    ],
    resize_keyboard=True
)

politician = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='International Political Economy'),
            KeyboardButton(text='How the world works'),
        ],
        [
            KeyboardButton(text='Understanding third world politics'),
            KeyboardButton(text='Capitalism, Socialism and Democracy')
        ],
        [
            KeyboardButton(text='⏪ Back')
        ]
    ],
    resize_keyboard=True
)

history = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Israel's history"),
            KeyboardButton(text='From third world to the first'),
        ],
        [
            KeyboardButton(text='Foundation of Jewish state'),
            KeyboardButton(text='Central Asia in world history')
        ],
        [
            KeyboardButton(text='⏪ Back')
        ]
    ],
    resize_keyboard=True
)

business = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Leaders eat last'),
            KeyboardButton(text='100 Great business ideas')
        ],
        [
            KeyboardButton(text='201 great business ideas for small business'),
            KeyboardButton(text='Great Innovator'),
        ],
        [
            KeyboardButton(text='⏪ Back')
        ]
    ],
    resize_keyboard=True
)
