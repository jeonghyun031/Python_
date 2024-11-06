import re,usecsv, os
English = 'She is vegetarian. She does not eat meat. She thinks that animals should not be killed. It is hard for her to hang out with poeple. Many people like to eat meat. She told his parents not to have meat. They lanughed at her. She realized they couldn\'t give up meat.'
Korean = '그녀는 채식주의자입니다. 그년느 고기를 먹지않습니다. 그녀는 동물을 죽이지 말아야 한다고 생각합니다. 그녀가 사람들과 어울리는 것은 어렵습니다. 많은 사람들이 고기를 좋아합니다. 그녀는 부모에게 고기를 먹지 말라고 말했습니다. 그들은 그녀를 비웃었습니다. 그녀는 그들이 고기를 포기할 수 없다는 것을 깨달았습니다.'
os.chdir(r'C:\\Users\\PC')
Korean_list = re.split(r'\.', Korean)
English_list = re.split(r'\.', English)
print(Korean_list)
total = []
for i in range(len(English_list)):
    total.append([English[i], Korean_list[i]])
usecsv.writecsv('Korean_English.csv', total)