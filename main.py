# Список 
books = [
    {'title': 'Таинственный сад', 'author': 'Фрэнсис Бернетт', 'year': '1911'},
    {'title': 'Ночь в Лиссабоне', 'author': 'Эрих Мария Ремарк', 'year': '1961'},
    {'title': 'Дневник Анны Франк', 'author': 'Анна Франк', 'year': '1947'},
    {'title': 'Гарри Поттер и философский камень', 'author': 'Дж. К. Роулинг', 'year': '1987'},
    {'title': 'Спеши любить', 'author': 'Николас Спаркс', 'year': '1999'},
]

# Цикл преребора 
for index in range(len(books)):
    print(f"*****Книга {index + 1}*****")
    print(f"Название: {books[index]['title']}, Автор: {books[index]['author']}")
    print(f"***** {books[index]['year']}*****")
    print()