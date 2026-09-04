weekly_tasks = [
    {"name":"学习Python基础", "estimated_minutes":150, "completed":True},
    {"name":"完成循环练习", "estimated_minutes":45, "completed":True},
    {"name":"预习列表和字典", "estimated_minutes":30, "completed":False},
]
total_minutes = 0
for task in weekly_tasks:
    total_minutes = total_minutes + task["estimated_minutes"]
    if task["completed"]:
        status = "已完成"
    else:
       status = "未完成"
    print(f"{task['name']}:预计学习{task['estimated_minutes']}分钟，{status}。")
print(f"本周预计总学习时长：{total_minutes}")