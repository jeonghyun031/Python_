import os, re
os.chdir(r'C:\Users\박정현\OneDrive\바탕 화면')
f = open('friends101.txt', 'r', encoding='utf8')
script101 = f.read()
print(script101[:1000])
f.close