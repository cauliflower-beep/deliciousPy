# import导入一个模块时，python解释器会首先执行被导入模块中的代码
import class02_modify


# 父类（超类）必须位于子类之前
class ElectricCar(class02_modify.Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        # 初始化父类的属性
        super().__init__(make, model, year)  # supper是一个特殊函数，可以调用父类的方法

        # 再初始化电动汽车特有的属性
        self.battery_size = 75

    def describe_battery(self):
        """打印一条描述点评容量的消息。"""
        print(f"this car has a {self.battery_size}-kwh battery.")

    # 对于父类中不合符子类情况的行为，可以进行重写
    # 为此，可以在子类中定义一个与要重写的父类方法同名的方法
    def fill_gas_tank(self):
        """电动汽车没有油箱。"""
        print(f"{self.model} doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()
my_tesla.fill_gas_tank()

# 随着项目不断进行，类中添加的细节可能越来越多，属性和方法清单会越来越长
# 此时可能需要将类的一部分提取出来，作为一个独立的类 比如将上述栗子中的 battery 单独抽离成一个类
