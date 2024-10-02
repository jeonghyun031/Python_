import re
data = 'a:3; b:4; c:5'
for i in re.split(';', data):
    print(re.split(':', i))