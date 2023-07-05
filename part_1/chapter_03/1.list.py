characters = ['goku', 'conan', 'naruto', 'lufy']
print(characters)
print(characters[3])
print(characters[-2])

# 大多数列表是动态的，随着程序的运行会进行增删元素
characters[3] = 'robin'
print(characters[3])

characters.append('spidy')
print(characters[-1])
characters.insert(2, 'flash')
print(characters)

# del 适用于需要删除元素并且不再以任何形式使用它
del characters[3]  # 需要知道待删除元素的索引
print(characters)
# pop 适用于需要删除元素，并且后续还要使用它
popped_character = characters.pop()  # 默认弹出列表最后一个元素
print(characters, "--->", popped_character)
popped_character = characters.pop(1)  # 也可以弹出指定位置处的元素
print(characters, "--->", popped_character)
# remove 适用于不清楚待删除元素在列表中的索引位置，只知道值的情况 且remove只会从列表中删除第一个值 如果要删除多个值，需要加上循环
characters.remove('flash')  # 删除不存在得元素会报错
print(characters)
