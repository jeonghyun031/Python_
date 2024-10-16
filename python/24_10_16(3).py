import os, re
os.chdir(r'C:\Users\박정현\OneDrive\바탕 화면')
f3 = open('friends101.txt', 'r', encoding='utf8')
script =f3.read()
monica = re.findall(r'Monica:.+', script)
f3o = open('monica.txt','w')
for line in monica:
    f3o.write(line)
    f3o.write('/n')
f3o.close