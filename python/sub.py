import os, usecsv
import numpy as np
os.chdir(r'C:\\user')
quest - np.array(usecsv.switch(usecsv.opencsv('quest.csv')))
print(quest)

quest [quest > 5] = 5
print(quest)