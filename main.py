import matplotlib.pyplot as plt

RED = '\u001b[41m'#Блок констант
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
BLACK = '\u001b[40m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
BLUE = '\u001b[44m'
file_name = 'sequence.txt'

def draw_flag_netherlands(): #Блок функций
    print(f'{"Вариант 3 "}{"№1 Cтранa: Нидерланды"}{END}')
    print(f'{RED}{"  " * (16)}{END}')
    print(f'{WHITE}{"  " * (16)}{END}')
    print(f'{BLUE}{"  " * (16)}{END}')
    print(f'  ')

def draw_pattern():
    for i in range (2):
        print(f'{WHITE}{"  " * (i)}{BLACK}{"  " * (1)}{WHITE}{"  " * (3-i*2)}{BLACK}{"  " * (1)}{WHITE}{"  " * (i)}{WHITE}{"  " * (i)}{BLACK}{"  " * (1)}{WHITE}{"  " * (3-i*2)}{BLACK}{"  " * (1)}{WHITE}{"  " * (i)}{END}')
    print(f'{WHITE}{" " * (4)}{BLACK}{" " * (2)}{WHITE}{" " * (8)}{BLACK}{" " * (2)}{WHITE}{" " * (4)}{END}')
    for i in range (2):
        print(f'{WHITE}{"  " * (1-i)}{BLACK}{"  " * (1)}{WHITE}{"  " * (i*2+1)}{BLACK}{"  " * (1)}{WHITE}{"  " * (1-i)}{WHITE}{"  " * (1-i)}{BLACK}{"  " * (1)}{WHITE}{"  " * (i*2+1)}{BLACK}{"  " * (1)}{WHITE}{"  " * (1-i)}{END}')

def draw_chart():
    print(f'')
    for i in range (10):
        print(f'{18-2*i}{" "* (1+2-(len(str(18-2*i))))}{WHITE}{"  " * (18-2*i)}{BLACK}{"  " * (2)}{WHITE}{"  " * (2*i)}{END}')
    print(f'{"   "}{" -- " * 10}')
    print(f'{"     0   1   2   3   4   5   6   7   8   9 "}')

def sum_even_odd_lines(filename):
    with open(filename, 'r') as file:
        even_sum = 0
        odd_sum = 0
        for i, line in enumerate(file):
            numbers = map(float, line.split())
            if i % 2 == 0:
                even_sum += abs(sum(numbers))
            else:
                odd_sum += abs(sum(numbers))
    return even_sum, odd_sum

def draw_diagram(classes, elements):

    # Создаем фигуру и оси
    fig, ax = plt.subplots()

    # Строим круговую диаграмму
    ax.pie(elements, labels=classes, autopct='%1.1f%%')

    # Оформляем диаграмму
    ax.axis('equal')
    plt.title("Круговая диаграмма по файлу с числовой последовательностью")

    # Показываем диаграмму
    plt.show()

if __name__ == '__main__':

    draw_flag_netherlands()#Выполнение первого задания

    draw_pattern()#Выполнение второго задания

    draw_chart()#Выполнение третьего задания

    even_sum, odd_sum = sum_even_odd_lines(file_name)#Выполнение четвертого заадния
    print(f'Сумма чисел на четных строках: {even_sum}')
    print(f'Сумма чисел на нечетных строках: {odd_sum}')

    classes = ['Сумма чисел по модулю на четных строках', 'Сумма чисел по модулю на нечетных строках']
    elements = [even_sum, odd_sum]
    draw_diagram(classes, elements)