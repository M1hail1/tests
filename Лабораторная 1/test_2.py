# TODO Найдите количество книг, которое можно разместить на дискете
capacity = 1.44 * 1024 * 1024
symbol = 4
count_symbol = 25
count_str = 50
count_page = 100
book_count = symbol * count_symbol * count_page * count_str

print("Количество книг, помещающихся на дискету:", int(capacity // book_count))
