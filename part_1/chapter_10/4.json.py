import json

fileName = 'nums.json'

# 写入
# nums = [2,3,4,5,6]
# with open(fileName,'w') as f:
#     json.dump(nums,f)

# 加载到内存
with open(fileName) as f:
    nums = json.load(f)
print(nums)

# json文件是一种在程序之间共享数据的简单方式

# 此外，将数据写入json还可以保护和读取用户生成的数据，否则程序数据会在程序停止运行时丢失