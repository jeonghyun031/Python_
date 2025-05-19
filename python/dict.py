import pickle

dic = {"dictionary": "사전","python": "파이썬",
    "zoo": "동물원","School": "학교","University": "대학교"}

with open("prob2-1.bat", "wb") as file:
    pickle.dump(dic, file)

with open("prob2-1.bat", "rb") as file:
    loaded_dic = pickle.load(file)
    for key, value in loaded_dic.items():
        print(f"{key}: {value}")