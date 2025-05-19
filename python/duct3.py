import pickle

with open("prob2-1.bat", "rb") as file:
    dic = pickle.load(file)

dic['python'] = '자바'

with open("prob2-1.bat", "wb") as file:
    pickle.dump(dic, file)

print(dic)