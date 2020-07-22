"""
days10 课后作业
杨俊
2020/07/08
"""
#1烤羊肉串
"""初始羊肉串是生的，烧烤时间是0
0-3分钟 生的
3-6分钟 半生不熟
6-9分钟 熟了
大于9分钟 烤焦了
打印羊肉串对象，输出烤的时间是xxx，状态是xxx
"""


# class Kebab:
#     """羊肉串类型"""
#     def __init__(self, burn_time):
#         """初始化"""
#         self.times = 0
#         self.burn_time = burn_time
#
#     def burn(self):
#         """烧烤"""
#         if self.burn_time < 3:
#             print(f"羊肉串烤了{self.burn_time}还是生的")
#         elif 3 <= self.burn_time < 6:
#             print(f"羊肉串烤了{self.burn_time}分钟，烤的半生不熟")
#         elif 6 <= self.burn_time < 9:
#             print(f"羊肉串烤了{self.burn_time}分钟，已经烤熟了")
#         elif self.burn_time > 9:
#             print(f"羊肉串烤了{self.burn_time}分钟，已经烤焦了")
#
#
# burn_time = int(input("请输入你的羊肉串烤的时间（分钟）："))
# ke =Kebab(burn_time)
# ke.burn()


#2. 面向对象中 属性的练习
"""
邓超 体重 75.0 公斤
邓超每次 奔跑 会减肥 0.1 公斤
邓超每次 吃东西 体重增加 0.5 公斤
打印对象会显示姓名体重
调用奔跑方法，会减肥 0.1 公斤
调用吃东西方法，体重增加 0.5 公斤
"""

class Person:
    """人的类型"""
    def __init__(self, name, weight):
        """初始化人的属性"""
        self.name = name
        self.weight = weight

    def __str__(self):
        """打印的方法"""
        return f"{self.name}的当前体重是{self.weight}kg"

    def run(self):
        """跑步的方法"""
        self.weight -= 0.1
        print(f"{self.name}跑了一次步，体重减少了0.1kg,当前体重是{self.weight}kg")

    def eat(self):
        """吃东西的方法"""
        self.weight += 0.5
        print(f"{self.name}吃了一次东西，体重增长了了0.5kg,当前体重是{self.weight}kg")


person = Person("邓超", 75)
print(person)
person.run()
person.eat()
print(person)