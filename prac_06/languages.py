
from prac_06.programming_language import ProgrammingLanguage


python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

# programming_languages = [ProgrammingLanguage("Python", "Dynamic", True, 1991),
#                          ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
#                          ProgrammingLanguage("Visual Basic", "Static", False, 1991)
#                          ]
# dynamic = [language for language in programming_languages if language.is_dynamic()]
# print(f"The dynamically typed languages are:\n{dynamic}")

programming_languages = [
    ProgrammingLanguage("Python", "Dynamic", True, 1991),
    ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
    ProgrammingLanguage("Visual Basic", "Static", False, 1991)
]

dynamic = [language for language in programming_languages if language.is_dynamic()]

print("The dynamically typed languages are:")

for language in dynamic:
    print(language.name)