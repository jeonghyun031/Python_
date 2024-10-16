import os, re
os.chdir(r'C:\Users\박정현\OneDrive\바탕 화면')
f4 = open('friends101.txt', 'r', encoding='utf8')
script =f4.read()

actor = re.findall(r'[A-Z][a-z]+:', script)
actor_set= set(actor)
print(actor_set)