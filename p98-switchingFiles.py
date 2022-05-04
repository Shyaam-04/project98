def swapFileData():
    file1 = open("C:/Users/pearl/OneDrive/Desktop/python/file1.txt","r")
    data_a = file1.read()
    file2 = open("C:/Users/pearl/OneDrive/Desktop/python/file2.txt","r")
    data_b = file2.read()
    switchedFile1 = open("C:/Users/pearl/OneDrive/Desktop/python/file1.txt","w+")
    switchedFile1.write(data_b)
    f1 = switchedFile1.read()
    switchedFile2 = open("C:/Users/pearl/OneDrive/Desktop/python/file2.txt","w+")
    switchedFile2.write(data_a)
    f2 = switchedFile2.read()
    fileName = input("Enter file name")
    if fileName=="file1.txt":
        print(f1)
    else:
        print(f2)
    


swapFileData()