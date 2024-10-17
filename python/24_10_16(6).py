import os, re
os.chdir(r'C:\Users\박정현\OneDrive\바탕 화면')
f6 = open('friends101.txt', 'r', encoding='utf8')
script =f6.read()

actor = set(re.findall(r'[A-Z][a-z]+:', script))

chr = [ str[:-1] for str in actor]

