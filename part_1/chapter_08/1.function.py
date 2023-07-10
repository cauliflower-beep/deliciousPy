# 基于实参顺序的关联方式，称为位置实参
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"my {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')

# 直接在实参中将名称和值关联起来的方式，称为关键字实参
# 这种方式不需要关心函数调用中的实参顺序，还清楚的指出了函数调用中各个值得作用
describe_pet(pet_name='peter', animal_type='spider')


# 传递任意数量的实参-元组
def make_pizza(*toppings):  # *使python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')


# 传递任意数量的实参-字典
def build_profile(first, last, **user_info):# ** 使python创建一个名为user_info的空字典，并将所有收到的键值对存入字典中
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
