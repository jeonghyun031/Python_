import os, re
os.chdir(r'C:\Users\박정현\OneDrive\바탕 화면')
f5 = open('friends101.txt', 'r', encoding='utf8')
script =f5.read()

actor = re.findall(r'[A-Z][a-z]+:', script)

for str in actor:
    print(str[:-1])