try:
    print(5 / 0)
except ZeroDivisionError:
    # 如果未对异常进行处理，程序会停止并显示traceback
    print("you can't divide by zero!")
else:
    print("got answer")

# 让用户看到traceback不是个好主意
# 怀有恶意的用户会通过traceback获悉你不想让他知道的代码，例如程序文件的名称，以及部分不能正确运行的代码
# 训练有素的攻击者就能根据这些信息判断出可对你的代码发起什么样的攻击。

# FileNotFoundError / ValueError

# 静默失败 pass

