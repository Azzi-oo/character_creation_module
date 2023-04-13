from random import randint


def attack(char_name: str, char_class: str) -> str:
    """Simulate an attack action for a character.
     Args:
         char_name (str): The name of the character performing the attack.
         char_class (str): The class of the character performing the attack.
    Returns:
         A string representing the outcome of the attack action.
    """
    if char_class == 'warrior':
        return (f'{char_name} {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name}{5 + randint(-3, -1)}')


def defence(char_name: str, char_class: str) -> str:
    """Simulate a defence action for a character.
    Args:
        char_name (str): The name of the character performing the defence.
        char_class (str): The class of the character performing the defence.
    Returns:
        A string representing the outcome of the defence action.
    """
    if char_class == 'warrior':
        return (f'{char_name}{10 + randint(5, 10)}')
    if char_class == 'mage':
        return (f'{char_name}{10 + randint(-2, 2)}')
    if char_class == 'healer':
        return (f'{char_name}{10 + randint(2, 5)}')


def special(char_name: str, char_class: str) -> str:
    """Simulate a special action for a character.
    Args:
        char_name (str): The name of the  special action.
        char_class (str): The class character performing the special action.
    Returns:
        A string representing the outcome of the special action.
    """
    if char_class == 'warrior':
        return (f'{char_name}{80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name}{5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name}{10 + 30}»')


def start_training(char_name: str, char_class: str) -> str:
    """Perform character training.
    Args:
        char_name (str): The name of the character being trained.
        char_class (str): The class of the character being trained.
    Returns:
        A string indicating that the training is complete.
    """
    if char_class == 'warrior':
        print(f'{char_name}')
    if char_class == 'mage':
        print(f'{char_name}')
    if char_class == 'healer':
        print(f'{char_name}')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Выбор персонажа.
    Args:
        char_name (str): имя персонажа.
        char_class (str): класс тренировки персонажа.
    Returns:
        Строка указывающее что выбор завершен.
    """
    approve_choice: str = ''
    char_class: str = ''
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
