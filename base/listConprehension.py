numbers = [i for i in range(1, 10) if i % 2 == 0]
print(numbers)
strings = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
flatten= [int(i) for items in strings for i in items]
print(flatten)
numberSet = {i for i in range(1, 6)}
print(numberSet)
user = {"name": "roni", "age": 26}
userDic = {value: key for key, value in user.items()}
print(userDic)