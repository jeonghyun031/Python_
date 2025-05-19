with open("prob2-1.bat", "rb") as file:
    dic = pickle.load(file)

search = input("Enter the word to search: ")

try:
    print(f"The meaning of '{search}' you searched for is: '{loaded_dic[search]}'")
except KeyError:
    print(f"'{search}' is a word that does not exist")