# To open a .csv file without any library
def open_csv(path):              #Provide the path of the file as an argument
    df = open(path,"r")
    header = df.readline()
    data = df.readlines()
    return df, header, data

# To get the headers of the file 
def get_header(headers):       #Provide the headers of the file as an argument
    headers = headers.split('"')
    header = []
    for i in headers:
        if i == "" or i == ";" or i == "\n":
            continue
        else:
            header.append(i)
    print(f"{'<<Header>>' : ^30}")
    for i in header:
        print(f"{i : ^30}")

# To get the count of customer in each category of "Marital"
def count_marital(data,cat1,cat2,cat3):        # Provide data and the categories you want as arguments
    lines = []
    for item in data:
        lines.append(item.split(";"))
    line = []
    for item in range(len(lines)):
        line.append(lines[item][2])
    count_category1 = line.count(cat1)
    count_category2 = line.count(cat2)
    count_category3 = line.count(cat3)
    return count_category1, count_category2, count_category3

# To get a histogram for age 
def histogram(data):
    lines = []
    for item in data:
        lines.append(item.split(";"))
    line = []
    for item in range(len(lines)):
        line.append(lines[item][0])

    I=[]
    II=[]
    III=[]
    IV=[]
    V=[]
    VI=[]
    VII=[]
    VIII=[]
    IX = []
    X=[]
    
    for i in line:
        if i == '"age"':
            continue
        else: 
            i = int(i)
            if i in range(0,11):
                I.append(i)
            elif i in range(11,21):
                II.append(i)
            elif i in range(21,31):
                III.append(i)
            elif i in range(31,41):
                IV.append(i)
            elif i in range(41,51):
                V.append(i)
            elif i in range(51,61):
                VI.append(i)
            elif i in range(61,71):
                VII.append(i)
            elif i in range(71,81):
                VIII.append(i)
            elif i in range(81,91):
                IX.append(i)
            elif i in range(91,101):
                X.append(i)
    print("Age 0-10")
    for i in range(int(len(I)/50)):
        print("|",end="")
    print()

    print("Age 11-20")
    for i in range(int(len(II)/50)):
        print("|",end="")

    print()
    print("Age 21-30")
    for i in range(int(len(III)/50)):
        print("|",end="")

    print()
    print("Age 31-40")
    for i in range(int(len(IV)/50)):
        print("|",end="")

    print()
    print("Age 41-50")
    for i in range(int(len(V)/50)):
        print("|",end="")

    print()
    print("Age 51-60")
    for i in range(int(len(VI)/50)):
        print("|",end="")

    print()
    print("Age 61-70")
    for i in range(int(len(VII)/50)):
        print("|",end="")

    print()
    print("Age 71-80")
    for i in range(int(len(VIII)/50)):
        print("|",end="")

    print()
    print("Age 81-90")
    for i in range(int(len(IX)/50)):
        print("|",end="")

    print()
    print("Age 91-100")
    for i in range(int(len(X)/50)):
        print("|",end="")







