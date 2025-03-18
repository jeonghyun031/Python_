def exchangeSort(x) :
    for i in range(len(x)-1) :
        for j in range(i+1,len(x)) :
            if x[j] < x[i]:
                x[i],x[j] = x[j], x[i]
    return x
x = [5,2,1,8,4]
exchangeSort(x)
print(x)