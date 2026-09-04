dailyminutes_text = input("计划每日学习多少分钟？")
dailyminutes = int(dailyminutes_text)
totalminutes = 0
for day in range (1,8):
    totalminutes = totalminutes + dailyminutes
    print(f"第 {day} 天，累计学习{totalminutes}分钟。")
print(f"未来 7 天计划学习总时长：{totalminutes}分钟。")