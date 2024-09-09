data_l = ['name', 'author', 'genre', 'count']

data = [
        ['Война и мир', 'Толстой', 'Романтика', 50],
        ['Алые паруса', 'Александр Грин', 'Комедия', 25],
        ['Ван-пис', 'Юитиро Ода', 'Романтика', 12],
        ['Властелин колец', 'Д. Толкин', 'Комедия', 10],
        ['Гарри Поттер', 'Д. Роуллинг', 'Романтика', 12],
        ['Белые ночи', 'Достоевский', 'Комедия', 0],
        ['Идиот', 'Достоевский', 'Романтика', 100]
    ]

def add_book():
    flag = True
    while(flag):
        print('Введите название: ')
        name = input()
        print('Введите автора: ')
        author = input()
        print('Введите жанррр: ')
        genre = input()
        print('Введите кол-во экземпляров: ')
        count = input()
        if int(count)>=0 and name.isalpha() and author.isalpha() and genre.isalpha():
            data.append([name, author, genre, count])
            flag =False
        else:
            print('Введите корректные данные!!! книгги любят уважение')

def count_book():
    summ =0
    for i in data:
        summ += i[3]
    print('количество книгг в библиотеке: ',summ)

def info():
    for i in data:
        print('Название: ', i[0], '; Автор: ',i[1], '; Жанр: ',i[2], '; Кол-во экземпляров: ',i[3] )

if __name__ == "__main__":
    while True:
        print("1. Добавить книггу")
        print("2. посччитать сколько книгг")
        print("3. Общая информация")
        print("4. Выход")
        action = input()
        match action:
            case '1':
                add_book()
            case '2':
                count_book()
            case '3':
                info()
            case '4':
                exit(0)