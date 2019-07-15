START = "<b>Вас приветствует магазин - 🗼 LeParis</b>\n\n" \
        "Удачных покупок!\n\n" \
        "Для получения помощи нажмите 👉 /help\n" \
        "Для просмотра последнего заказа нажмите 👉 /lastorder\n\n" \
        "Выберите город:\n➖➖➖➖➖➖➖➖➖➖\n" \
        "🏠 <b>Белгород</b>\n[ Нажмите 👉/city1 ]\n➖➖➖➖➖➖➖➖➖➖\n" \

HELP = '''➖➖➖➖➖➖➖➖➖➖
Добро пожаловать в наш магазин.
Уважаемый клиент, будьте внимательны при оплате и выборе товара.
Перед покупкой товара, бот предложит Вам город, товар и удобный для Вас район, 
после чего, выдаст реквизиты для оплаты.
Внимательно перед покупкой проверяйте товар и выбранный район. Обязательно 
записывайте реквизиты для оплаты (номер кошелька и комментарий).

При оплате, Вам необходимо обязательно указать  комментарий, который выдал Вам 
бот, иначе оплата не будет засчитана в автоматическом режиме и Вы не получите 
адрес.
Всегда записывайте номер заказа и комментарий, с помощью них, вы сможете узнать 
статус заказа (получить адрес) в любой момент и с любого устройства. Сохраняйте 
чек до тех пор, пока не получили адрес. Присутствует возможность производить 
несколько платежей с одним комментарием. Платежи суммируются и в случае, если 
сумма полная - Вы получаете свой адрес.
Будьте внимательны, кошелек, комментарий и сумма должны быть точными. Если 
возникли какие-либо проблемы - обращайтесь к оператору.

После внесения оплаты, нажмите кнопку проверки платежа и если Ваша оплата будет 
найдена - Вы получите адрес в автоматическом режиме.
Так же для Вашего удобства реализована возможность просмотра Вашего последнего 
заказа, для этого необходимо нажать /lastorder
А для того, чтобы вернуться на стартовую страницу к выбору городов, просто 
нажмите /start или напишите любое сообщение.

Приятных покупок!
➖➖➖➖➖➖➖➖➖➖'''

LASTORDER = '''У вас нет заказов.
Нажмите 👉 /start для того, чтобы вернуться к выбору города.'''

CHECK = 'К сожалению, платеж не найден.\n' \
    'Если вы произвели оплату, но видите это сообщение,\n' \
    'подождите 5 минут и проверьте оплату еще раз,\n' \
    'нажав 👉 /check\n\n' \
    'Для того, чтобы вернуться к выбору городов нажмите\n' \
    '👉 /start.'

PAY1 = '</b>\n➖➖➖➖➖➖➖➖➖➖\nВнимание! Обязательно укажите этот ' \
    'комментарий\nпри оплате, иначе оплата не будет засчитана в ' \
    'автоматическом режиме.\n\n<b>Заказ №' \

PAY2 = '</b> запомните его. По номеру заказа и комментарию вы сможете ' \
       'узнать статус заказа (получить адрес) в любой момент и с любого ' \
       'устройства\n\n' \
       'После оплаты нажмите 👉 /check, чтобы получить ' \
       'адрес. Чтобы отказаться от заказа, нажмите 👉 /start\n\n' \

CITY1 = '🏠<b>Белгород</b>\n\nВыберите товар:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🎁 <b>СК кристаллы 0.3г</b>\n' \
    '💰 Цена: <b>1000 руб.</b>\n' \
    '[ Для покупки нажмите 👉/buy1 ]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🎁 <b>СК кристаллы 0.5г</b>\n' \
    '💰 Цена: <b>1500 руб.</b>\n' \
    '[ Для покупки нажмите 👉/buy2 ]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот город, нажмите 👉/start для того, чтобы ' \
    'вернуться назад и выбрать нужный город.'

BUY1 = '🏠 <b>Белгород</b>\n\n' \
    '🎁 <b>СК кристаллы 0.3г</b>\n' \
    '💰 Цена: <b>1000 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Центр</b>\n[Для выбора нажмите 👉 /buy1_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city1\nдля того, чтобы вернуться назад в город <b>Белгород' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY1_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>СК кристаллы 0.3г</b>\n' \
    '💰 <b>1000 руб.</b>\n' \
    '🏠 город <b>Белгород</b>\n' \
    '🏃 район <b>Центр</b>\n(для смены района нажмите\n' \
    '👉 /buy2)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1000 рублей</b> на номер QIWI:\n' \
    '<b>+79582666387</b>\nкомментарий к платежу:\n<b>'

BUY2 = '🏠 <b>Белгород</b>\n\n' \
    '🎁 <b>СК кристаллы 0.5г</b>\n' \
    '💰 Цена: <b>1500 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Гора</b>\n[Для выбора нажмите 👉 /buy2_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city1\nдля того, чтобы вернуться назад в город <b>Белгород' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY2_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>СК кристаллы 0.5г</b>\n' \
    '💰 <b>1500 руб.</b>\n' \
    '🏠 город <b>Белгород</b>\n' \
    '🏃 район <b>Гора</b>\n(для смены района нажмите\n' \
    '👉 /buy2)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1500 рублей</b> на номер QIWI:\n' \
    '<b>+79582666387</b>\nкомментарий к платежу:\n<b>'

BUY3 = '🏠 <b>Белгород</b>\n\n' \
    '🎁 <b>СК кристаллы 1г</b>\n' \
    '💰 Цена: <b>2500 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Гора</b>\n[Для выбора нажмите 👉 /buy3_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city1\nдля того, чтобы вернуться назад в город <b>Белгород' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY3_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>СК кристаллы 1г</b>\n' \
    '💰 <b>2500 руб.</b>\n' \
    '🏠 город <b>Белгород</b>\n' \
    '🏃 район <b>Гора</b>\n(для смены района нажмите\n' \
    '👉 /buy3)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>2500 рублей</b> на номер QIWI:\n' \
    '<b>+79582666387</b>\nкомментарий к платежу:\n<b>'

BUY6 = '🏠 <b>Белгород</b>\n\n' \
    '🎁 <b>Мефедрон 0.7г</b>\n' \
    '💰 Цена: <b>1800 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Гора</b>\n[Для выбора нажмите 👉 /buy6_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city1\nдля того, чтобы вернуться назад в город <b>Белгород' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY6_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Мефедрон 0.7г</b>\n' \
    '💰 <b>1800 руб.</b>\n' \
    '🏠 город <b>Белгород</b>\n' \
    '🏃 район <b>Гора</b>\n(для смены района нажмите\n' \
    '👉 /buy6)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1800 рублей</b> на номер QIWI:\n' \
    '<b>+79582666387</b>\nкомментарий к платежу:\n<b>'
