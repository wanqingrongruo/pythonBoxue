stringInDoubleQuotes = "Hello Python!"
stringInSingleQuotes = 'Hello Python!'
stringInTripleQuotes = """Hello Python!
This might be a long string
going through multiple lines
"""
aNumber = 123
aString = str(aNumber)
# 字符串只读, 创建后不可修改
# python3 unicode, python asii
action = "Hello "
name = "roni!"
welcome = action + name
print(welcome)
print(welcome.upper())
print(welcome.lower())
print(action.strip()) #去除首尾空格
#print(dir(name)) # 输出支持的方法
#print(help(action.count)) # 方法签名
print(action[0:3]) # 切片
print("My name is %s" % name) # 以 % 做分隔符，不同于 c 的 ，
print("%s%s" % (action, name))
print("PI: %.3f" % 3.1415926)

# 新式模板
nWelcome = {"action": action, "name": name}
print("%(action)s%(name)s" % nWelcome)
print("{action} {name}".format(**nWelcome))