import random
num_of_attempts = 1
list_of_letters = 'АЕНОСТ'
word = random.sample(list_of_letters, 4)
word_str = ''.join(word)
first_letter = word_str[0]
second_letter = word_str[1]
third_letter = word_str[2]
fourth_letter = word_str[3]
self_place = 0
other_place = 0
spam = ''
print('Загадано четырехбуквенное слово из букв А,E,Н,О,С,Т.')
print('Отгадай!')
while num_of_attempts <= 10:
    attempt = input('Попытка № {}: '.format(num_of_attempts)).upper()
    if first_letter == attempt[0]:
        self_place += 1
    if second_letter == attempt[1]:
        self_place += 1
    if third_letter == attempt[2]:
        self_place += 1
    if fourth_letter == attempt[3]:
        self_place += 1
    for char in attempt:
        if char in word_str:
            if spam != char:
                other_place += 1
                spam += char
            else:
                spam = char
    print('На "своем месте": {}'.format(self_place))
    print('На "чужом месте": {}'.format(other_place - self_place))
    if self_place == 4:
        print('Вы выиграли!')
        break
    self_place = 0
    other_place = 0
    spam = ''
    num_of_attempts += 1
    if num_of_attempts > 10:
        print('Вы проиграли!')
