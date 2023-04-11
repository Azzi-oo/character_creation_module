from random import randint


def attack(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name}{5 + randint(-3, -1)}')


def defence(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name}{10 + randint(5, 10)}')
    if char_class == 'mage':
        return (f'{char_name}{10 + randint(-2, 2)}')
    if char_class == 'healer':
        return (f'{char_name}{10 + randint(2, 5)}')


def special(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name}{80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name}{5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name}{10 + 30}»')


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}')
    if char_class == 'mage':
        print(f'{char_name}')
    if char_class == 'healer':
        print(f'{char_name}')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа')
        if char_class == 'warrior':
            print('Воитель — дер')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор ').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()

    print(start_training(char_name, char_class))


main()
