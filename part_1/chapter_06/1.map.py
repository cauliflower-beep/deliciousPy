alien_0 = {"color": "green", "point": "5"}
print(alien_0["color"])

# python3.7中 字段元素的排列顺序与定义时相同
for k in alien_0:
    print(k, alien_0[k])

del alien_0["color"]

# 直接访问一个字典中不存在的键，python会报错
# 但可以通过get方法的第二个参数指定一个返回值，当键不存在时，则返回这个值，不会报错
color_value = alien_0.get('color', 'no color value assigned.')
print(color_value)

alien_0["height"] = "5"
# 字典的遍历
for k, v in alien_0.items():
    print(k, v)

# 按特定顺序遍历字典中的所有键
for k in sorted(alien_0.keys()):
    print(k)

# 遍历字典所有的值并去重 集合set中的每个元素都必须师独一无二的
for v in set(alien_0.values()):
    print(v)

# 花括号{}可以直接创建集合，注意与字典的区别 倒是可以用字典实现集合的效果，因为字典的k也是不能重复的
language = {"python", "golang", "java", "golang"}
print(language)

# 列表元素可以是字典，字典的v也可以是列表
# 虽然python没有要求某些字典具有相同的结构，但建议这样做，例如表示某几个用户信息的map，他们的结构应该相同，否则会使for循环遍历时候的复杂度增加
