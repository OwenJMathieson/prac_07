from prac_07.programming_language import ProgrammingLanguage

Ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic","Static", False, 1991)

Languages = [Ruby, python, visual_basic]
print(python)

print("The dynamically typed languages are:")
for Language in Languages:
    if Language.is_dynamic():
            print(Language.name)