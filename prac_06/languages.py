from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
print(ruby)
print(visual_basic)
languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
for objects in languages:
    if objects.is_dynamic():
        print(objects.name)
