import functions as fun

print("Welcome to Lab 1!")
print()
status = True
while status:
    print("To view the bank csv file: 'view'\nTo view the headers: 'header'\nTo view the count of customers martial status: 'marital'\nTo view a histogram based on customers age: 'histogram'")
    print()
    
    func = input("Enter the function: ").lower()
    
    if func == 'view':          # Without using the help of any libraries, open the given dataset
        bank, header, data = fun.open_csv("Lab 1/Data/bank.csv")
        print(data)
    
    elif func == 'header':      # Print the headers in the file
        print(fun.get_header(header))
    
    elif func == 'marital':     # Find the count of customers in each category 'marital'
        married, divorced, single = fun.count_marital(data,'"married"','"divorced"','"single"')
        print("Number of Married people are:", married)
        print("Number of Divorced people are:", divorced)
        print("Number of Single people are:", single)
    
    elif func == 'histogram':       # Prepare a histogram for age using a print statements (You can use the scale  of 0-10,11-20,21-30...,91-100)
        print("Following is the historgram for age in the `bank` dataset")
        fun.histogram(data)
    
    else: 
        print("Enter a vaild output!")
    
    if input("Do you want to continue? (y/n) ").lower() == "n":
        status = False
    else:
        continue

print()
print("Thank you")