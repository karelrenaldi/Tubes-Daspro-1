import csv


# Fungsi load untuk load program
def load(fileName, mark):
    file = open('../data/'+fileName, 'r')
    reader = csv.reader(file, delimiter=",")
    fileArray = [mark for i in range(100)]
    for i in range(100):
        fileArray[i] = next(reader, mark)
    return(fileArray)


# Fungsi getLength untuk menentukan panjang array
def getLength(array, mark):
    i = 0
    length = 0
    finish = False
    while(i < 100 and finish == False):
        if(array[i] == mark):
            finish = True
        else:
            length += 1
        i += 1
    return(length)


# Fungsi save untuk rewrite file csv
def save(fileName, array, mark):
    file = open('../data/'+fileName, 'w', newline='')
    writer = csv.writer(file, delimiter=",")
    i = 0
    while(array[i] != mark):
        writer.writerow(array[i])
        i += 1
    file.close()
