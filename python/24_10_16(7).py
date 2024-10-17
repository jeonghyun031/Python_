import os, re
os.chdir(r'C:\Users\박정현\OneDrive\바탕 화면')
f6 = open('friends101.txt', 'r', encoding='utf8')
f6.read(100)
f6.seek(0)
sentences = f6.readlines()
sentences[:3]

for i in sentences[:20]:
    if re.match(r'[A-Z][a-z]+:'. i):
        print(i)

lines = [ i for i in sentences if re.match(r'[A-Z][a-z]+:', i)]
lines[:10]

would = [ i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would',i)]

print(would)

take = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('take', i)]
print(take)