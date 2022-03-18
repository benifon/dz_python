# 1 задание)


user_answer = int(input('Put time in seconds - '))

sec = user_answer % 3600
min = user_answer // 60
hour = user_answer // 3600
day = user_answer // 86400
week = user_answer // 604800
month = user_answer // 2629743
year = user_answer // 31556926

if user_answer <= 0:
    print("Enter a positive number!")

duration = [sec, min, hour, day, week, month, year]
print(list(reversed(duration)))


# задание 2)


numbers = [number ** 3 for number in range(1, 1001, 2)]
print(numbers)


def my_filter(numbers, function, extra_num=0):
    result = []
    for number in numbers:
        input(number)
        if function(number + extra_num):
            result.append(number + extra_num)
    return sum(result)

def is_even(number):
    return number % 7 == 0

def check_number(number):
    check_number = 0
    for num in str(number):
        check_number += int(num)
    return check_number % 7 == 0


# 3)


for i in range(1, 101):
    if i % 100 in (11, 12, 13, 14, 15) or i % 10 in (5, 6, 7, 8, 9, 0):
        print(f'{i} процентов')
    elif 1 < i % 10 < 5:
        print(f'{i} процента')
    elif i % 10 == 1:
        print(f'{i} процент')
