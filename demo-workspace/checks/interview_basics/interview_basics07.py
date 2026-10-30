src = open("exercises/interview_basics/interview_basics07.py", encoding="utf-8").read()
assert "[x * 2 for" not in src, "改成生成器表达式（去掉方括号）"
assert "省内存" in answer, "核心优势是按需产出、省内存"
assert total == sum(x * 2 for x in range(1000))
