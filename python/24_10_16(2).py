import os, re
os.chdir(r'C:\Users\박정현\OneDrive\바탕 화면')
f2 = open('friends101.txt', 'r', encoding='utf8')
script101 = f2.read()
Line = re.findall(r'Monica:.+', script101)
print(Line[:3])
f2.close()