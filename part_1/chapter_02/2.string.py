"""
牢记两个命令：
1.dir(obj)——查看一个对象拥有的所有属性和方法，入参为具体对象；`__`开头和结尾的是特殊方法，用于实现对象的一些基本行为，重点关注没有双下划线的方法
2.help(str)——获取对象或方法的详细信息，入参为某个类型；不知道某个变量的类型，可以用type(obj)查看；
熟练使用内置方法，可以省去很多重复的工作
"""

# string
name = "ada lovelace"
print(dir(name))
print(help(str))

print(name.title())
print(name.upper())
print(name.lower())

# f python3.6以上
first_name = "kevin"
last_name = "stacy"
full_name = f"{first_name}·{last_name}"
print(full_name)

# format python3.5以下
full_name = "{}·{}".format(first_name, last_name)
print(full_name)

# \t \n
print("\thello world!")

# rstrip lstrip strip 最常用于在存储用户输入前对其清理
language = "  golang   "
print(language, len(language))
print(language.rstrip(), len(language.rstrip()))
print(language.lstrip(), len(language.lstrip()))
print(language.strip(), len(language.strip()))
