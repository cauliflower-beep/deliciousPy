cars = ['bmw', 'audi', 'toyota', 'subaru', 'benz', 'honda']
# 不应该在for循环中修改列表，会导致python难以跟踪其中的元素。可改为while循环，遍历的同时进行修改
for car in cars:
    print(car)

# “差一行为” 结果不包含6
for value in range(1, 6, 2):
    print(value)

