#정규표현식
import re
example = '이동민 교수님은 다음과 같이 설명했습니다.(이동민,2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다.(최재영,2019). 또 다른 견해도 있었습니다.(Lion, 2018)'
result = re.findall(r'\((.+?)\)', example)
text = text = "연락처는 010-1234-5678이고, 집 전화는 02-123-4567입니다."
# match, findall, search로 찾는 방법이 있다.
# ^는 다음의 문자로 시작한 문자를 찾음(^'hello' -> hello로 시작하는 것을 찾음)
# .은 임의의 한 문자('h.t' , hat hit hot 등등을 찾음)
# +는 앞의 패턴이 1회 이상 반복됨을 나타냄
# *는 0회 이상 반복 ('ab*c' -> abc abbc abbbc 등을 찾음)
another = re.findall('0\d{1,2}-\d{3,4}-\d{4}', text)
print(result)
print(another)