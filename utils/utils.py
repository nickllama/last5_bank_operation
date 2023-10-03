
def filter_and_sorting(data: list):
    "Сортировка по дате"
    items = [item for item in data if item.get('state') == "EXECUTED"]

    items.sort(key=lambda x: x.get('date'), reverse=True)
    return items

def get_date(date: str):
    "Получение верного формата даты"
    date_num = date[0:10].split('-')
    return date_num[2] + '.' + date_num[1] + '.' + date_num[0]


def mask_prepare_message_number(message):
    "Определение Карта/счёт"
    if message is None:
        return 'Личный счет'

    message_split = message.split(' ')
    if message_split[0] == 'Счет':
        hidden_number = mask_account_number(message_split[-1])
    else:
        hidden_number = mask_card_number(message_split[-1])

    return ' '.join(message_split[:-1]) + ' ' + hidden_number

def mask_card_number(number: str):
    "Возвращение номера карты, в нужном формате."
    if number.isdigit() and len(number) == 16:
        return number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]
    else:
        print('отсутствует номер карты')

def mask_account_number(number: str):
    "Возвращение номера счёта, в нужном формате."
    if number.isdigit() and len(number) >= 4:
        return "**"+number[-4:]
    else:
        print('отсутствует номер счета')






def prepare_user_message(item: dict):
    "Подготовка Сообщения с операцией в нужном формате"
    date = get_date(item.get('date'))
    desc = item.get('description')
    from_ = mask_prepare_message_number(item.get('from'))
    to_ = mask_prepare_message_number(item.get('to'))
    amount = item.get('operationAmount').get('amount')
    curr = item.get('operationAmount').get('currency').get('name')

    return  f'{date} {desc}\n{from_} -> {to_}\n{amount} {curr}\n'

