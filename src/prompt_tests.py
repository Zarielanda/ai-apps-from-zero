prompt_tests = [
    {"task": "文章摘要", "model": "模型A", "score": 85, "passed": True},
    {"task": "情感分类", "model": "模型 A", "score": 72, "passed": True},
    {"task": "问答准确性", "model": "模型 B", "score": 58, "passed": False},
]
total_score = 0
passed_count = 0
for test in prompt_tests:
    total_score = total_score + test["score"]
    if test["passed"]:
        passed_count = passed_count + 1
        status = "通过"
    else:
        status = "未通过"
    print(f"{test['task']}模型为{test['model']}，分数为{test['score']}，{status}。")
print(f"测试总分为{total_score}，平均分为{total_score / len(prompt_tests)}，通过次数为{passed_count}次。")