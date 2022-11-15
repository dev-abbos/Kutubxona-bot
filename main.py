from config import dp
from aiogram import executor
from keyboard import *
import logging
from aiogram.types import Message
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start(message: Message):
    await message.reply('🇺🇿 Virtual kutubxonaga hush kelibsiz!\n'
                        '🇷🇺 Добро пожаловать в виртуальную библиотеку!\n'
                        '🇺🇸 Welcome to virtual library!', reply_markup=menu)

@dp.message_handler(text='⏪')
async def back(message: Message):
    await message.answer('🇺🇿 Tilni tanlang.\n'
                         '🇷🇺 Выберите язык.\n'
                         '🇺🇸 Choose language.', reply_markup=menu)

@dp.message_handler(text='⏪ Orqaga')
async def back(message: Message):
    await message.answer('Janrni tanlang', reply_markup=uzmenu)

@dp.message_handler(text='⏪ Назад')
async def back(message: Message):
    await message.answer('Выберите жанр', reply_markup=rumenu)

@dp.message_handler(text='⏪ Back')
async def back(message: Message):
    await message.answer('Choose genre', reply_markup=enmenu)

# UZ
@dp.message_handler(text='🇺🇿 Uz')
async def uz(message: Message):
    await message.answer('Janrni tanlang', reply_markup=uzmenu)

@dp.message_handler(text='📚 Badiiy')
async def uz(message: Message):
    await message.answer('Kitobni tanlang', reply_markup=badiiy)

@dp.message_handler(text='Jannatga taklifnoma')
async def b(message: Message):
    kitob = open('kitoblar/Jannatga taklifnoma.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Yo‘qolgan dunyo')
async def b(message: Message):
    kitob = open('kitoblar/Yo‘qolgan dunyo.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Yarim asr daftari')
async def b(message: Message):
    kitob = open('kitoblar/Yarim asr daftari.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Uilyam Folkner. Qora musiqa')
async def b(message: Message):
    kitob = open('kitoblar/Uilyam Folkner. Qora musiqa.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Seni jannatda kutaman')
async def b(message: Message):
    kitob = open('kitoblar/Seni jannatda kutaman.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Yevgeniy Onegin')
async def b(message: Message):
    kitob = open('kitoblar/Yevgeniy Onegin.pdf', 'rb')
    await message.answer_document(kitob)


@dp.message_handler(text='📚 Fantastika')
async def uz(message: Message):
    await message.answer('Kitobni tanlang', reply_markup=fantastika)

@dp.message_handler(text='Gulliverning sayohatlar')
async def b(message: Message):
    kitob = open('kitoblar/Gulliverning sayohatlar.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Iblis va Prim xonim')
async def b(message: Message):
    kitob = open('kitoblar/Iblis va Prim xonim.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Qiyofa o‘g‘risi')
async def b(message: Message):
    kitob = open('kitoblar/Qiyofa o‘g‘risi.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Mixail Bulgakov. Ityurak')
async def b(message: Message):
    kitob = open('kitoblar/Mixail Bulgakov. Ityurak.pdf', 'rb')
    await message.answer_document(kitob)


@dp.message_handler(text='📚 Mistika')
async def uz(message: Message):
    await message.answer('Kitobni tanlang', reply_markup=mistika)

@dp.message_handler(text='O‘z-o‘zini gipnozlash')
async def b(message: Message):
    kitob = open('kitoblar/O‘z-o‘zini gipnozlash.PDF', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Ruh sirlari')
async def b(message: Message):
    kitob = open('kitoblar/Ruh sirlari.pdf', 'rb')
    await message.answer_document(kitob)


@dp.message_handler(text='📚 Biznes')
async def uz(message: Message):
    await message.answer('Kitobni tanlang', reply_markup=biznes)

@dp.message_handler(text='Menejment nazariyasi')
async def b(message: Message):
    kitob = open('kitoblar/Menejment nazariyasi.PDF', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Milliy va jahon iqtisodiyoti')
async def b(message: Message):
    kitob = open('kitoblar/Milliy va jahon iqtisodiyoti.PDF', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Koronavirus va biznes')
async def b(message: Message):
    kitob = open('kitoblar/Menejment nazariyasi.PDF', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Biznes reja tuzish qo‘llanmasi')
async def b(message: Message):
    kitob = open('kitoblar/Milliy va jahon iqtisodiyoti.PDF', 'rb')
    await message.answer_document(kitob)


@dp.message_handler(text='📚 Fan')
async def uz(message: Message):
    await message.answer('Kitobni tanlang', reply_markup=fan)

@dp.message_handler(text='Husnixat - Arab alifbosi')
async def b(message: Message):
    kitob = open('kitoblar/Husnixat - Arab alifbosi.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Anorganik Kimyo')
async def b(message: Message):
    kitob = open('kitoblar/Anorganik Kimyo.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Fanlar majmuasi')
async def b(message: Message):
    kitob = open('kitoblar/Fanlar majmuasi-2021.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Falsafa va fan metodologiyasi')
async def b(message: Message):
    kitob = open('kitoblar/Falsafa va fan metodologiyasi.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Elementar matematika qo\'llanma')
async def b(message: Message):
    kitob = open("kitoblar/Elementar matematika qo'llanma.pdf", 'rb')
    await message.answer_document(kitob)


@dp.message_handler(text='📚 Diniy')
async def uz(message: Message):
    await message.answer('Kitobni tanlang', reply_markup=diniy)

@dp.message_handler(text='Imom G‘azzoliy. Qirq hadisi qudsiy')
async def b(message: Message):
    kitob = open('kitoblar/Imom G‘azzoliy. Qirq hadisi qudsiy.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Keng rizq va baraka omillari')
async def b(message: Message):
    kitob = open('kitoblar/Keng rizq va baraka omillari.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Tajvid qoidalari')
async def b(message: Message):
    kitob = open('kitoblar/Tajvid qoidalari.PDF', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Ilm olish sirlari')
async def b(message: Message):
    kitob = open('kitoblar/Ilm olish sirlari.pdf', 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Ulamolar nazdida vaqtning qadri')
async def b(message: Message):
    kitob = open("kitoblar/Ulamolar nazdida vaqtning qadri.PDF", 'rb')
    await message.answer_document(kitob)

# RU
@dp.message_handler(text='🇷🇺 Ru')
async def ru(message: Message):
    await message.answer('Выберите жанр', reply_markup=rumenu)

@dp.message_handler(text='📚 Художественное')
async def c(message: Message):
    await message.answer('Выберите книгу', reply_markup=xudojestvennoe)


@dp.message_handler(text='Под Куполом')
async def c(message: Message):
    kitob = open("kitoblar/ru/Под Куполом.fb2", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Побег из лагеря смерти')
async def c(message: Message):
    kitob = open("kitoblar/ru/Побег из лагеря смерти.epub", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Александр Дюма. Железная маска')
async def c(message: Message):
    kitob = open("kitoblar/ru/Дюма Александр. Железная маска.epub", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Что сказал покойник')
async def c(message: Message):
    kitob = open("kitoblar/ru/Что сказал покойник.pdf", 'rb')
    await message.answer_document(kitob)


@dp.message_handler(text='📚 Мистика')
async def c(message: Message):
    await message.answer('Выберите книгу', reply_markup=misticheskoe)

@dp.message_handler(text='Осознаное сновидение')
async def c(message: Message):
    kitob = open("kitoblar/ru/Осознаное сновидение.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Черная и белая магия')
async def c(message: Message):
    kitob = open("kitoblar/ru/Черная и белая магия.pdf", 'rb')
    await message.answer_document(kitob)


@dp.message_handler(text='📚 Фантастика')
async def c(message: Message):
    await message.answer('Выберите книгу', reply_markup=fantasticheskoe)

@dp.message_handler(text='Белая чума')
async def c(message: Message):
    kitob = open("kitoblar/ru/Белая чума.fb2", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Игра престолов')
async def c(message: Message):
    kitob = open("kitoblar/ru/Игра престолов.fb2", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Инвиктус')
async def c(message: Message):
    kitob = open("kitoblar/ru/Инвиктус.fb2", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Полный газ')
async def c(message: Message):
    kitob = open("kitoblar/ru/Полный газ.fb2", 'rb')
    await message.answer_document(kitob)


@dp.message_handler(text='📚 Бизнес')
async def c(message: Message):
    await message.answer('Выберите книгу', reply_markup=biznesSs)

@dp.message_handler(text='Артем Сенаторов. Бизнес в Instagram')
async def c(message: Message):
    kitob = open("kitoblar/ru/Артем_Сенаторов_Бизнес_в_Instagram.fb2", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Яндекс. Книга')
async def c(message: Message):
    kitob = open("kitoblar/ru/Яндекс. Книга.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Психология трейдинга')
async def c(message: Message):
    kitob = open("kitoblar/ru/Психология трейдинга.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Разумный инвестор')
async def c(message: Message):
    kitob = open("kitoblar/ru/Разумный инвестор.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Марина Могилко. Как стать блогером')
async def c(message: Message):
    kitob = open("kitoblar/ru/Марина_Могилко_Как_стать_блогером.pdf", 'rb')
    await message.answer_document(kitob)


@dp.message_handler(text='📚 Наука')
async def c(message: Message):
    await message.answer('Выберите книгу', reply_markup=nauka)

@dp.message_handler(text='Астрономия')
async def c(message: Message):
    kitob = open("kitoblar/ru/астрономия.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Квантовая случайность')
async def c(message: Message):
    kitob = open("kitoblar/ru/Квантовая случайность.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Удивительная солнечная система')
async def c(message: Message):
    kitob = open("kitoblar/ru/удивительная солнечная система.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Одиноки ли мы во вселенной')
async def c(message: Message):
    kitob = open("kitoblar/ru/одиноки ли мы во вселенной.pdf", 'rb')
    await message.answer_document(kitob)


@dp.message_handler(text='📚 Религия')
async def c(message: Message):
    await message.answer('Выберите книгу', reply_markup=religiya)

@dp.message_handler(text='Ежедневные сунны')
async def c(message: Message):
    kitob = open("kitoblar/ru/Ежедневные сунны.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Аль-Кабаир')
async def c(message: Message):
    kitob = open("kitoblar/ru/Аль-Кабаир.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Ученные в Исламе')
async def c(message: Message):
    kitob = open("kitoblar/ru/Ученные в Исламе.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Собрания в месяц Рамадан')
async def c(message: Message):
    kitob = open("kitoblar/ru/Собрания в месяц Рамадан.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Рассказы о пророках')
async def c(message: Message):
    kitob = open("kitoblar/ru/Рассказы о пророках.pdf", 'rb')
    await message.answer_document(kitob)


# EN
@dp.message_handler(text='🇺🇸 En')
async def en(message: Message):
    await message.answer('Choose genre', reply_markup=enmenu)

@dp.message_handler(text='📚 Contemporary')
async def d(message: Message):
    await message.answer('Choose a book', reply_markup=contemporary)

@dp.message_handler(text='The labors of Hercules')
async def c(message: Message):
    kitob = open("kitoblar/en/Agatha_Christie_-_The_Labors_Of_Hercules.epub", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='The butterfly project')
async def c(message: Message):
    kitob = open("kitoblar/en/Emma_Scott_-_The_Butterfly_Project.epub", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Lost Girl')
async def c(message: Message):
    kitob = open("kitoblar/en/Lost_Girl_-_Adam_Nevill.epub", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Paranoid')
async def c(message: Message):
    kitob = open("kitoblar/en/Paranoid_-_Lisa_Jackson.epub", 'rb')
    await message.answer_document(kitob)


@dp.message_handler(text='📚 Politician')
async def d(message: Message):
    await message.answer('Choose a book', reply_markup=politician)

@dp.message_handler(text='International Political Economy')
async def c(message: Message):
    kitob = open("kitoblar/en/International Political Economy.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='How the world works')
async def c(message: Message):
    kitob = open("kitoblar/en/noam-chomsky-2011-how-the-world-works.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Understanding third world politics')
async def c(message: Message):
    kitob = open("kitoblar/en/understanding third world politics.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text='Capitalism, Socialism and Democracy')
async def c(message: Message):
    kitob = open("kitoblar/en/Capitalism, Socialism and Democracy ( PDFDrive ).pdf", 'rb')
    await message.answer_document(kitob)


@dp.message_handler(text='📚 History')
async def d(message: Message):
    await message.answer('Choose a book', reply_markup=history)

@dp.message_handler(text="Israel's history")
async def c(message: Message):
    kitob = open("kitoblar/en/Israel-s-History-and-the-History-of-Israel.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text="From third world to the first")
async def c(message: Message):
    kitob = open("kitoblar/en/From Third World to First The Singapore Story ( PDFDrive ).pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text="Foundation of Jewish state")
async def c(message: Message):
    kitob = open("kitoblar/en/Herzl’s Vision_ Theodor Herzl and the Foundation of the Jewish State ( PDFDrive ).pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text="Central Asia in world history")
async def c(message: Message):
    kitob = open("kitoblar/en/Central Asia in world history ( PDFDrive ).pdf", 'rb')
    await message.answer_document(kitob)


@dp.message_handler(text='📚 Business')
async def d(message: Message):
    await message.answer('Choose a book', reply_markup=business)

@dp.message_handler(text="Leaders eat last")
async def c(message: Message):
    kitob = open("kitoblar/en/Leaders_Eat_Last__Why_Some_Teams.pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text="100 Great business ideas")
async def c(message: Message):
    kitob = open("kitoblar/en/100 Great Business Ideas ( PDFDrive ).pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text="201 great business ideas for small business")
async def c(message: Message):
    kitob = open("kitoblar/en/201 great ideas for your small business ( PDFDrive ).pdf", 'rb')
    await message.answer_document(kitob)

@dp.message_handler(text="Great Innovator")
async def c(message: Message):
    kitob = open("kitoblar/en/Great_Innovator book boxed set Steve_Jobs, Benjamin Franklin.pdf", 'rb')
    await message.answer_document(kitob)



if __name__ == '__main__':
    executor.start_polling(dp)
