letter_point = {
    1: ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
    2 : ['Д', 'К', 'Л', 'М', 'П', 'У'],
    3 : ['Б', 'Г', 'Ё', 'Ь', 'Я'],
    4 : ['Й', 'Ы'],
    5 : ['Ж', 'З', 'Х', 'Ц', 'Ч'],
    8 : ['Ш', 'Э', 'Ю' ],
    10 : ['Ф', 'Щ', 'Ъ']
}

def point():
    let_num = 0
    word = input("Введите слово: ").upper()
    for i in word:
        for num, let in letter_point.items():
            if i in let:
                let_num += num
    return let_num

print(point())