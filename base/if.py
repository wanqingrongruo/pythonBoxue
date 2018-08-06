# if
num = 2
if num < 10:
    content = "{0} is less than 10".format(num)
    print(content)
elif 10 < num < 20:
    print("between 10 and 20")
elif not num == 20: # !=
    print("grater than 20")
else:
    print("grater than or equal to 20")

# and or 

notK = num not in [10, 20]
print(notK)

# 一切有空语义的值被认定为 false => (), [], None, ""
if __name__ == "__main__":
    print("作用: 执行一些当脚本被独立执行时才执行的代码")
