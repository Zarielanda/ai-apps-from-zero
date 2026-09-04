minutes_text = input("今天学习了多少分钟？")
minutes = int(minutes_text)
target = 60
if minutes == 0:
    print("状态：未开始。")
elif minutes < target:
    print(f"状态：未达标，还差 {target - minutes} 分钟。")
elif minutes == target:
    print("状态：达标。")
else:
    print(f"状态：超额完成。超过 {minutes - target} 分钟。")