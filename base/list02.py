
# 新输出模式
welcome = {"action": "hello", "name":"roni"}
print("%(action)s %(name)s" % welcome)
print("{0} {1}".format("Hello", "roni"))
print("{action} {name}".format(**welcome))

# 列表: 类对象,引用类型
list = [4, 5, 3]
mixList = [1, 2, 3, "four"]
print(list + mixList)
nList = mixList
copyList = mixList.copy()
mixList.extend(list)
print(mixList)
mixList.append(list)
print(mixList)
# 引用类型
print("nList: %s, copyList: %s" % (nList, copyList))
list.sort()
print("list sort: %s" % list)
print(list[0:-1])
mixList.insert(1, 9) # 插入索引超过最大长度,会插在列表末尾
print(mixList)
print(mixList.pop(0)) # 删除第0个元素, 没有报错
print(mixList)
print(mixList.remove(3))  # 第一个3, 没有报错
print(mixList)
del(mixList[0:5:2]) # del 全局删除, 参数是切片
print(mixList)
print(dir(mixList))
print(len(mixList))


