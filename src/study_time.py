minutes_text = input("今天学习了多少分钟？")
minutes = int(minutes_text)
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"你今天学习了{hours}小时{remaining_minutes}分钟。")

# 计算 24 周的理论学习时长
daily_hours_text = input("你每天计划学习多少小时？")
daily_hours = float(daily_hours_text)
total_hours = daily_hours * 6 * 24
print(f"按每天学习{daily_hours}小时、每周学习 6 天计算，24 周理论学习总时长是{total_hours}小时。")
