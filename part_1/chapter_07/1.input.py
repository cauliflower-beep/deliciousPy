# 大多数程序旨在解决最终用户的问题，为此通常需要从用户那边获取一些信息
# 有时候提示可能超过一行，我们可以先将提示赋值给一个变量，再传递给input
prompt = "if you tell us who you are, we can personalize the message you see."
prompt += "\nplease enter your name:"
name = input(prompt)  # 输入的内容，python会将其解读为字符串
print(f"welcome,{name}")
