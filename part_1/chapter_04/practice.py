import time

# 数到20
# for i in range(1,21):
#     time.sleep(1)
#     print(i)

# 创建一个包含数1~1_000_000的列表，再使用一个for循环将这些数打印出来
num_list = list(range(1,1_000_001))
# print(len(num_list))
# for i in num_list:
#     time.sleep(1)
#     print(i)

# 创建一个包含数1~1_000_000的列表，在使用min()和max()核实该列表确实是从1开始、到1_000_000结束的
# 另外，对这个列表调用sum()，看看python将100w个数相加需要多长时间
print("min:",min(num_list))
print("max:",max(num_list))
print("sum:",sum(num_list))


