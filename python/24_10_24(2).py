a = [[ '구', '전체', '내국인', '외국인'],['관악구','519864','542498', '5105'], ['송파구', '686181', '679247', '6934'], ['강동구','428547', '424235', '4312']]
f = open('abc.csv', 'w', newline='', encoding='utf-8-sig')
f2 = open('data2.csv', 'w', encoding='utf-8')
csvobj = csv.writer(f, delimiter=',')
csvobj.writerows(a)
f.close()