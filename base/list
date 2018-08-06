list01 = []
list02 = list01
list01 = [1, 2, 3, "one"] # 无法指定 list 中的类型
mixList = [list01]
print("list01 = %s, mixList = %s" % (list01, mixList))
list02 = [10, 11, 12]
print(list01 + list02)
print(mixList.extend(list02)) # 修改原 list # O(n), 逐个元素添加
print(mixList)
mixList.append(list02) # O(1)
print(mixList)
