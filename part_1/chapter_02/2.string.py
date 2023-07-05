# string
name = "ada lovelace"
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
