list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count = len(list_players)
size = count // 2
command_one = list_players[:size]
command_two = list_players[size:]
print(command_one)
print(command_two)