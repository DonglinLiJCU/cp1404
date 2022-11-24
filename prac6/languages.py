"""
Languages
Estimate: 3 minutes
Actual:   3 minutes
"""
from prac6.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

my_list = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
for i in my_list:
    if i.is_dynamic():
        print(i.name)
