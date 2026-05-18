def bubble_sort(data): 
    for i in range (len(data)-1):
        for j in range (len(data)-1):
            if data[j]< data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data




if __name__ == "__main__":
    a=[8,9,2,4,6,]
    print(bubble_sort(a))
