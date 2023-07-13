# 使用文件第一步，一定是打开文件
# with在不再需要访问文件之后将其关闭
# 也可以显式的调用close方法，但是：1.可能因为程序bug未执行close；2.过早close可能等使用的时候发现文件已经关闭
with open('poem.txt', encoding='utf8') as file:
    # content = file.read()
    lines = file.readlines()
# print(content)

for line in lines:
    print(line.rstrip())  # 去除多余空行
