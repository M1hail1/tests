# TODO Напишите функцию find_common_participants
def find_common_participants(s1, s2, r=','):
    participants1 = set(s1.split(r))
    participants2 = set(s2.split(r))
    common_participants = sorted(list(participants1.intersection(participants2)))
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, '|'))
