def insert_sort(x) :
    for i in range(1,len(x)) :
        j = i-1
        key=x[i]
        while x[j] > key and j>=0:
            x[j+1]=x[j]
            j= j-1
        x[j+1] =key
    return x

x = [5, 2, 1, 8, 4]
print(x)