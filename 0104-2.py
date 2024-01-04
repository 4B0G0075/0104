class Employee:
    def __init__(self, name, position, years_of_service, hourly_rate):
        self.name = name
        self.position = position
        self.years_of_service = years_of_service
        self.hourly_rate = hourly_rate

    def display_info(self):
        return f"員工姓名：{self.name}\n職位：{self.position}\n年資：{self.years_of_service} 年\n時薪：${self.hourly_rate}"

    def get_name(self):
        return f"員工姓名：{self.name}"

class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        return f"飲料名稱：{self.name}\n價格：${self.price}"

# 創建三個員工實例
employee1 = Employee(name="小明", position="店長", years_of_service=5, hourly_rate=20)
employee2 = Employee(name="小華", position="櫃檯人員", years_of_service=2, hourly_rate=15)
employee3 = Employee(name="小美", position="調酒師", years_of_service=3, hourly_rate=18)

# 創建兩種飲料實例
beverage1 = Beverage(name="綠茶", price=30)
beverage2 = Beverage(name="奶茶", price=35)

# 查詢員工名字
print("員工名字查詢：")
print(employee1.get_name())
print(employee2.get_name())
print(employee3.get_name())
