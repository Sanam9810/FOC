import operation
import read
import write

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("                                                           Welcome to Evo Store                                                      ")
print("----------------------------------------------------------------------------------------------------------------------------")
print("\t\tAddress : Jawalakhel,Lalitpur || Contact Number : 015528932")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\n")


conti=True
while conti==True:
    print("We have following services :")
    print("\n")     
    print("1. Purchase laptops from manufacturer")
    print("2. Sell laptops to customers")
    print("3. Exit")
    print("\n")
    try:
        do=int(input("What would you like to do :"))
    except:
        print("\n")
        print("You've entered invalid input.Please enter integer/numeric value.")
        do=int(input("What would you like to do :"))
    print("--------------------------------------------------------------------------------")

    read_file=read.read_file()
    if do==1:
        sell_lap=operation.selling_laptop(read_file)
        write.write_file(sell_lap)
        inp_=input("Enter Y to continue in our system :").upper()
        if inp_!="Y":
            conti=False
    elif do==2:
        buy_lap=operation.purchasee(read_file)
        write.write_file(buy_lap)
        inp_=input("Enter Y to continue in our system :").upper()
        if inp_!="Y":
            conti=False
    elif do==3:
        print("Thank you for visiting us. ")
        break
    else:
        print("Please enter valid input.")
        print("--------------------------------------------------------------------------------")

    

        
