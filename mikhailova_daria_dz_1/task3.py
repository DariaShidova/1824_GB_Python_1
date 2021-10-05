word_list = ['процент', 'процента', 'процентов']
number_list_1 = [1, 21, 31, 41, 51, 61, 71, 81, 91]
number_list_2 = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93,
                 94]
number = 1
percentage = 'word'
while number <= 100:
    if number in number_list_1:
        percentage = word_list[0]
    elif number in number_list_2:
        percentage = word_list[1]
    else:
        percentage = word_list[2]
    print(number, percentage)
    number = number + 1
