# sort 也可以对字符串列表按字母顺序排序 永久性，无法复原
nums = [3, 2, 6, 3, 7, 5, 8, 4, 9, 10, 1]
nums.sort()  # 默认升序排序
print(nums)
nums.sort(reverse=True)  # 降序排序
print(nums)

# sorted 临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru', 'benz', 'honda']
print(cars)
print(sorted(cars))
print(sorted(cars, reverse=True))
print(cars)

# reverse 翻转列表元素 不涉及排序 永久性 但可以通过再次reverse来复原
cars.reverse()
print(cars)
print(len(cars))
