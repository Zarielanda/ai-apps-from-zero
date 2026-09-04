records = []
total_minutes = 0
while True:
    content = input("今天学习了什么内容？")
    minutes_text = input("学了多少分钟？")
    minutes = int(minutes_text)
    record = {"content": content, "minutes": minutes}
    records.append(record)
    whether_continue = input("补充其他内容，输入“y”。")
    total_minutes = total_minutes + minutes
    if whether_continue != "y":
        break
print("\n今日学习内容：")
for record in records:
    print(f"\n- {record['content']}：{record['minutes']}分钟")
if total_minutes == 0:
    print(f"\n今天学习未开始。")
elif total_minutes < 120:
    print(f"\n今天学习总时长:{total_minutes}分钟，未达标。")
elif total_minutes == 120:
    print(f"\n今天学习总时长:{total_minutes}分钟，达标。")
else:
    print(f"\n今天学习总时长:{total_minutes}分钟，超额完成。")