cars = ['bmw', 'audi', 'toyota', 'subaru', 'benz', 'honda']
print(cars[:3])
print(cars[-3:-1])

# 切片复制列表，复制的是副本，更改新列表不会影响原列表
cars02 = cars[:]
cars02.append("tesla")
print(cars02)
print(cars)

# 直接将列表赋值给另外一个变量，则新变量也指向原列表， 修改变量值，原列表也会受到影响
cars03 = cars
cars03.append("ford")
print(cars03)
print(cars)
