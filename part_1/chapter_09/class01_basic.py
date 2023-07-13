# python中约定首字母大写的是类
class Dog:
    """一个小狗类"""

    def __init__(self, name, color):
        """初始化属性name和color"""
        self.name = name
        self.color = color

    def sit(self):
        """收到命令就坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """收到命令时打滚"""
        print(f"{self.name} rolled over!")

my_dog = Dog("willie","yellow")
your_dog = Dog("lucy","white")

print(f"my dog's name is {my_dog.name}")
print(f"my dog's color is {my_dog.color}")
my_dog.sit()
my_dog.roll_over()

print(f"your dog's name is {your_dog.name}")
print(f"your dog's color is {your_dog.color}")
your_dog.sit()
your_dog.roll_over()
