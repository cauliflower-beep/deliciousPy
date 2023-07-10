# 如果有多个事件会导致循环退出，可以指定标志位
# 例如玩家失去所有飞船、时间耗尽、保护的城市被摧毁
prompt = "tell me something, and i will repeat it back to you:"
prompt += "\nenter 'quit' to end the program."
flag = True
while flag:
    msg = input(prompt)
    if msg == 'quit':
        flag = False
    else:
        print(msg)

# while循环可以在遍历列表的同时修改列表元素
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)
while "cat" in pets:
    pets.remove("cat")
print(pets)
