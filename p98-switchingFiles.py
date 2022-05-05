def swapFileData():
    fileName1 = input("Enter 1st file")
    file1 = open(fileName1,"r")
    data_a = file1.read()
    fileName2 = input("Enter 2nd file")
    file2 = open(fileName2,"r")
    data_b = file2.read()
    switchedFile1 = open(fileName1,"w+")
    switchedFile1.write(data_b)
    f1 = switchedFile1.read()
    switchedFile2 = open(fileName2,"w+")
    switchedFile2.write(data_a)
    f2 = switchedFile2.read()
    fileName = input("Enter file name")
    if fileName=="file1.txt":
        print(f1)
    else:
        print(f2)
    


swapFileData()