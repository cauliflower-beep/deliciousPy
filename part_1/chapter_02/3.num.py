# int + - * / **  空格不影响表达式计算
print(2 ** 2)
print(4 / 2)  # 即使两个整数相除，结果也会被python表示为浮点数

# float 包含的小数位数可能是不确定的，这是由于浮点数表示的精度问题导致的。暂时忽略多余的小数位数即可
print(0.2 + 0.1)
print(3 * 0.1)

# 书写很大的数时，可使用下划线将其中的数字进行分组
universe_age = 14_000_000_000
print(universe_age, type(universe_age))

