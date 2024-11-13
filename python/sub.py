import csv
import numpy as np
f = open('설문.csv', 'r')
new = csv.reader(f)
quest = np.array(list(new))
quest = quest.astype('int32')
quest[quest > 5] = 5
quest