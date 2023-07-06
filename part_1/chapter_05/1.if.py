# if通常将一个变量的当前值同特定值进行比较
car = "audi"
if car == "audi":  # 如果需要忽略大小写，可以将其全部转为小写再比较
    print("yep, it's audi")
else:
    print("nop, it's not audi")

cars = []
if cars: # if 语句中将列表名用作条件表达式时，python将再列表至少包含一个元素时返回True 为空时返回false
    print("here's some car")
else:
    print("no, you don't even have a car!")
