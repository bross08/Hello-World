#This function lists the first 10 multiples of the number that is entered by the user
def multiples():
    num = input("Please enter a number: ")
    if num == 0:
        print("No multiples to list")
    else:
        for i in range (1, 11):
            print("{} times {} equals".format(num, i), num * i)

multiples()
