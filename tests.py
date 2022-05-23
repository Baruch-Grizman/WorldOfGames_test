

def save_and_read_name():
    new_name = input('please enter your name: ')
    with open('Scores.txt', 'a+', encoding='utf-8') as file:
        file.write(f'{new_name}')
    with open('Scores.txt', encoding='utf-8') as read:
        for line in read.readlines():
            print(line, end='')

save_and_read_name()
