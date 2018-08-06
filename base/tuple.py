# tuple
numbers = (1, 2, 3)
mix = (1, 2, "three")
tlist = tuple([1, 2, 3]) # tuple 关键字将 list 转化成 tuple
print(tlist)
combineTuple = numbers + tlist
print(combineTuple)
print(numbers * 2)
print(numbers[0:3:2])
#print(dir(numbers))

# dictionary

user = {"name": "roni", "age": 26}
print(user["name"]) # 访问不存的key不合法
user["age"] = 18
user["email"] = "devzheng@qq.com"
print(user)
del(user["name"])
print(user)
#user.clear()
#print(user)
# key 唯一且只读
print(user.keys())
print(user.values())
print("age" in user)


