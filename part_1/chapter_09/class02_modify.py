# 修改类属性值的两种方法： 1.直接修改 2.通过方法修改
class Car:
    def __init__(self, make, model, year):
        self.make = make  # 制造商
        self.model = model  # 型号
        self.year = year  # 生产年份
        self.odometer_reading = 0  # 里程 不通过形参定义，而是指定一个初始默认值

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        """打印指出汽车里程消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 1.直接修改属性值
my_new_car.odometer_reading = 34
my_new_car.read_odometer()

# 2.通过方法修改类属性值
my_new_car.update_odometer(53)
my_new_car.read_odometer()

my_new_car.update_odometer(48)
