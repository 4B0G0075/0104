class FriedChicken:
    # constructer
    def __init__(self, flavor, size, crispy_level, marination_time):
        self.flavor = flavor
        self.size = size
        self.crispy_level = crispy_level
        self.marination_time = marination_time
        self.is_cooked = False

    def marinate(self, marinade):
        print(f"正在將{self.size} {self.flavor}雞肉浸泡在{marinade}中，浸泡時間{self.marination_time}小時。")

    def fry(self):
        if not self.is_cooked:
            print(f"將{self.size} {self.flavor}雞肉炸至酥脆。")
            self.is_cooked = True
        else:
            print("這塊雞肉已經炸過了！")

    def serve(self):
        if self.is_cooked:
            print(f"上菜：美味的{self.size} {self.flavor}炸雞！")
        else:
            print("你需要先炸這塊雞肉。")

# 創建四個不同口味的炸雞物件，每個物件都有不同的 marination_time
chicken_spicy = FriedChicken(flavor="辣味", size="大份", crispy_level="超酥脆", marination_time=2)
chicken_original = FriedChicken(flavor="原味", size="中份", crispy_level="酥脆", marination_time=1)
chicken_honey_mustard = FriedChicken(flavor="蜜芥末", size="小份", crispy_level="超級酥脆", marination_time=3)
chicken_lemon_pepper = FriedChicken(flavor="檸檬胡椒", size="特大份", crispy_level="特級酥脆", marination_time=4)

# 共同呼叫的副函式
print("\n炸雞1:")
chicken_spicy.marinate("辣椒醬")
chicken_spicy.fry()
chicken_spicy.serve()

print("\n炸雞2:")
chicken_original.marinate("原味調味料")
chicken_original.fry()
chicken_original.serve()

print("\n炸雞3:")
chicken_honey_mustard.marinate("蜜芥末醬")
chicken_honey_mustard.fry()
chicken_honey_mustard.serve()

print("\n炸雞4:")
chicken_lemon_pepper.marinate("檸檬胡椒調味料")
chicken_lemon_pepper.fry()
chicken_lemon_pepper.serve()
