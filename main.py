import json
from utils.utils import filter_and_sorting
from utils.utils import prepare_user_message




with open('operations.json') as file:
    data = json.load(file)

items = filter_and_sorting(data)

for i in range(5):
    print(prepare_user_message(items[i]))