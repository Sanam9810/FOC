import datetime

def purchasee(laptop_dictionaryy):
    name=input("Please enter your name to generate invoice :")
    user_choice={}
    laptop_dictionary=laptop_dictionaryy
    loop=True
    while loop==True:
        #Printing The details of laptop from text file. 
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("Welcome to Laptop purchasing screen, Here are our Laptop options :")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("S.N. \tLaptop Name \tCompany Name \tPrice \tQuantity   Graphic \tRam")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        for i in range(1,len(laptop_dictionary)+1,1):
            if i==1:
                print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   "+str(laptop_dictionary[i][3])+"\t  "+laptop_dictionary[i][4]+" "+laptop_dictionary[i][5])
            elif i==2:  
                print(str(i)+"\t   "+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   "+str(laptop_dictionary[i][3])+"\t  "+laptop_dictionary[i][4]+" "+laptop_dictionary[i][5])
            elif i==3:
                print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"     "+laptop_dictionary[i][2]+"\t   "+str(laptop_dictionary[i][3])+"\t  "+laptop_dictionary[i][4]+" "+laptop_dictionary[i][5])
            elif i==4:
                print(str(i)+"\t "+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   "+str(laptop_dictionary[i][3])+"\t  "+laptop_dictionary[i][4]+" "+laptop_dictionary[i][5])
            elif i==5:
                print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   "+str(laptop_dictionary[i][3])+"\t  "+laptop_dictionary[i][4]+" "+laptop_dictionary[i][5])
            print("-------------------------------------------------------------------------------------------------------------------------------------")
        #using try except block which checks if input user has entered is invalid or not to avoid program crash.
        try:
            input_=int(input("Please input the S.N. of Laptop would you like to buy:"))
            print("\n")
        except:
            print("\n")
            print("You've entered unexpected value.Please enter a integer/numeric value.")
            print("\n")
            input_= int(input("Which Laptop would you like to buy :"))
        print("--------------------------------------------------------------------------------")
        while input_<=0 or input_> len(laptop_dictionary):
            print("Please provide a valid Laptop Id!!")
            print("--------------------------------------------------------------------------------")
            try:
                input_= int(input("Which Laptop would you like to buy :"))
            except:
                print("\n")
                print("You've entered unexpected value.Please enter a int value.")
                print("\n")
                input_= int(input("Which Laptop would you like to buy :"))
            print("--------------------------------------------------------------------------------")
        #Asking user to input quantity.
        try:
            quantity= int(input("Please provide quantity of laptop you want to buy:"))
        except:
            print("\n")
            print("You've entered unexpected value.Please enter a int value.")
            print("\n")
            quantity= int(input("Please provide quantity of laptop you want to buy:"))
        print("--------------------------------------------------------------------------------")
        #Checking if quantity is available in our system
        laptop_quantity=laptop_dictionary[input_][3]
        while quantity <= 0 or quantity > int(laptop_quantity):
            print("Sorry we don't currently have "+str(quantity)+" "+laptop_dictionary[input_][0]+" laptop right now. Please re-enter the quantity.")
            print("--------------------------------------------------------------------------------")
            try:
                quantity= int(input("Please provide quantity of laptop you want to buy:"))
            except:
                print("\n")
                print("You've entered unexpected value.Please enter a int value.")
                print("\n")
                quantity= int(input("Please provide quantity of laptop you want to buy:"))
            print("--------------------------------------------------------------------------------")
        #Entering the data in dictionary
        user_choice[input_]=quantity
        #Changing quantity after purchase is succesful
        laptop_dictionary[input_][3]=int(laptop_dictionary[input_][3])-int(quantity)
        cont=input("Do you want to continue buying (Y/N) :").upper()
        if cont=="N":
            loop=False
        elif cont=="Y":
            loop=True
        else:
            print("\n")
            cont=input("You've entered invalid input. If you want to continue enter Y, if you want to proceed to invoice generation enter N? :").upper()
            if cont=="N":
                loop=False
    print("--------------------------------------------------------------------------------")
    #Calculating final price.    
    final_price=0
    for sn in user_choice.keys():
        if sn==1:
            razer_price= int(laptop_dictionary[1][2].replace("$",""))
            razer_q=int(user_choice[sn])
            razer_amt=razer_price*razer_q
            final_price+=razer_amt
        elif sn==2:
            xps_price= int(laptop_dictionary[2][2].replace("$",""))
            xps_q=int(user_choice[sn])
            xps_amt=xps_price*xps_q
            final_price+=xps_amt
        elif sn==3:
            alw_price= int(laptop_dictionary[3][2].replace("$",""))
            alw_q=int(user_choice[sn])
            alw_amt=alw_price*alw_q
            final_price+=alw_amt
        elif sn==4:
            swfit_price= int(laptop_dictionary[4][2].replace("$",""))
            swfit_q=int(user_choice[sn])
            swfit_amt=swfit_price*sft_q
            final_price+=swfit_amt
        elif sn==5:
            mac_price= int(laptop_dictionary[5][2].replace("$",""))
            mac_q=int(user_choice[sn])
            mac_amt=mac_price*mac_q
            final_price+=mac_amt

    #Applying discount to the final price.
    discount=0
    grand_total=0
    dip=0.0
    if final_price>0 and final_price<=5000:
        grand_total=final_price
    elif final_price>5000 and final_price<=28000:
        dip=10.0
        discount=(dip*final_price)/100
        grand_total=final_price-discount
    elif final_price>28000 and final_price<=39000:
        dip=20.0
        discount=(dip*final_price)/100
        grand_total=final_price-discount
    elif final_price>39000 and final_price<=800000:
        dip=25.0
        discount=(dip*final_price)/100
        grand_total=final_price-discount
    else:
        dip=30.0
        discount=(dip*final_price)/100
        grand_total=final_price-discount
        
    datimee=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
    unique=str(datimee)      

    #Creating the unique invoice using date time everytime user buys.
    file=open(unique+"-purchase"+name+".txt","w")      
    file.write("=====================================================================")
    file.write("\nEVO STORE          Jawlakhel, Lalitpur \t\t\t\tBill")
    file.write("\n=====================================================================")
    file.write("\nLAPTOP NAME           QUANTITY            PRICE           TOTAL PRICE")                     
    file.write("\n--------------------------------------------------------------------------------------------------------")      
    for input_val in user_choice.keys():           
        if input_val==1:
            file.write(str("\n"+laptop_dictionary[1][0]+"         "+str(user_choice[1])+"                "+laptop_dictionary[1][2]+"               "+str(int(razer_amt))))
        elif input_val==2:
            file.write(str("\n"+laptop_dictionary[2][0]+"                 "+str(user_choice[2])+"                 "+laptop_dictionary[2][2]+"                "+str(int(xps_amt))))
        elif input_val==3:
            file.write(str("\n"+laptop_dictionary[3][0]+"           "+str(user_choice[3])+"                 "+laptop_dictionary[3][2]+"                "+str(int(alw_amt))))
        elif input_val==4:
            file.write(str("\n"+laptop_dictionary[4][0]+"             "+str(user_choice[4])+"                "+laptop_dictionary[4][2]+"                "+str(int(sft_amt))))
        elif input_val==5:
            file.write(str("\n"+laptop_dictionary[5][0]+"       "+str(user_choice[5])+"                 "+laptop_dictionary[5][2]+"                "+str(int(mac_amt))))
    file.write("\n\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\n\t\t\t            Your final amount : "+str(int(final_price)))
    file.write("\n----------------------------------------------------------------------------------------------------------------------")
    file.write("\n\t\t\t            Your "+str(dip)+"% discounted amount is: "+str(int(discount)))
    file.write("\n----------------------------------------------------------------------------------------------------------------------")
    file.write("\n\t\t\t            Your Grand Total is: "+str(int(grand_total)))
    file.write("\n=====================================================================")
    file.close()
    #Printing the invoice.
    print("\n")
    print("--------------------------------------------------------------------------------")
    print("Bill:")
    file=open(unique+"-purchase"+name+".txt","r")
    print(file.read())
    file.close()
    
    return laptop_dictionary

def selling_laptop(laptop_dictionaryy):
    name=input("Please enter your name to generate invoice :")
    user_quantity={}
    laptop_dictionary=laptop_dictionaryy
    loop=True
    while loop==True:
        print("--------------------------------------------------------------------------------")
        print("Welcome to Distributer's screen, Laptop available are shown below :")
        print("--------------------------------------------------------------------------------")
        print("S.N. \tLaptop Name \tCompany Name \tMarket Price")
        print("--------------------------------------------------------------------------------")
        for i in range(1,len(laptop_dictionary)+1,1):
            if i==1:
                print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   ")
            elif i==2:  
                print(str(i)+"\t   "+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   ")
            elif i==3:
                print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"     "+laptop_dictionary[i][2]+"\t   ")
            elif i==4:
                print(str(i)+"\t "+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   ")
            elif i==5:
                print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   ")
            print("--------------------------------------------------------------------------------")
        try:
            input_=int(input("Please input the S.N. of Laptop would you like to buy:"))
            print("\n")
        except:
            print("You've entered unexpected value.Please enter a int value.")
            print("\n")
            input_= int(input("Which Laptop would you like to buy :"))
            print("\n")
        while input_<=0 or input_> len(laptop_dictionary):
            print("Please provide a valid Laptop Id!!")
            print("\n")
            try:
                input_= int(input("Please input the S.N. of Laptop would you like to buy :"))
                print("\n")
            except:
                print("You've entered unexpected value.Please enter a int value.")
                input_= int(input("Please input the S.N. of  Laptop would you like to buy:"))
                print("\n")
        try:
            quantity= int(input("How many laptop would you like to buy :"))
            print("\n")
        except:
            print("You've entered unexpected value.Please enter a int value.")
            print("\n")
            quantity= int(input("How many laptop would you like to buy :"))
            print("\n")
        user_quantity[input_]=quantity
        laptop_dictionary[input_][3]=int(laptop_dictionary[input_][3])+int(quantity)
        more=input("Enter Y if you want to buy more laptops :").upper()
        print("\n")
        if more!="Y":
            loop=False
    final_price=0
    for sn in user_quantity.keys():
        if sn==1:
            razer_price= int(laptop_dictionary[1][2].replace("$",""))
            razer_qty=int(user_quantity[sn])
            razer_amt=razer_price*razer_qty
            final_price+=razer_amt
        elif sn==2:
            xps_price= int(laptop_dictionary[2][2].replace("$",""))
            xps_qty=int(user_quantity[sn])
            xps_amt=xps_price*xps_qty
            final_price+=xps_amt
        elif sn==3:
            alw_price= int(laptop_dictionary[3][2].replace("$",""))
            alw_qty=int(user_quantity[sn])
            alw_amt=alw_price*alw_qty
            final_price+=alw_amt
        elif sn==4:
            swift_price= int(laptop_dictionary[4][2].replace("$",""))
            swift_qty=int(user_quantity[sn])
            swift_amt=swift_price*swift_qty
            final_price+=swift_amt
        elif sn==5:
            mac_price= int(laptop_dictionary[5][2].replace("$",""))
            mac_qty=int(user_quantity[sn])
            mac_amt=mac_price*mac_qty
            final_price+=mac_amt
    discount=0        
    vat=13.0
    final_price=final_price+(vat*final_price)/100        
    grand_total=0
    dip=0.0
    if final_price>0 and final_price<=45000:
        grand_total=final_price
    elif final_price>45000 and final_price<=100000:
        dip=10.0
        discount=(dip*final_price)/100
        grand_total=final_price-discount
    elif final_price>100000 and final_price<=180000:
        dip=15.0
        discount=(dip*final_price)/100
        grand_total=final_price-discount
    elif final_price>180000 and final_price<=250000:
        dip=18.0
        discount=(dip*final_price)/100
        grand_total=final_price-discount
    else:
        dip=25.0
        discount=(dip*final_price)/100
        grand_total=final_price-discount

    datime=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
    unique=str(datime)         

    file=open(unique+"-sell"+name+".txt","w")      
    file.write("=====================================================================")
    file.write("\nEVO STORE          Jawlakhel, Lalitpur \t\t\t\tBill")
    file.write("\n=====================================================================")
    file.write("\nLAPTOP NAME           QUANTITY            UNIT PRICE           TOTAL PRICE")                     
    file.write("\n-------------------------------------------------------------------------------------------------------------------")
     
    for i in user_quantity.keys():           
        if i==1:
            file.write(str("\n" +laptop_dictionary[1][0]+"            "+str(int(user_quantity[1]))+"               "+laptop_dictionary[1][2]+"                "+str(razer_amt)))
        elif i==2:
            file.write(str("\n" +laptop_dictionary[2][0]+"                 "+str(int(user_quantity[2]))+"                   "+laptop_dictionary[2][2]+"                 "+str(xps_amt)))
        elif i==3:
            file.write(str("\n" +laptop_dictionary[3][0]+"              "+str(int(user_quantity[3]))+"                "+laptop_dictionary[3][2]+"               "+str(alw_amt)))
        elif i==4:
            file.write(str("\n" +laptop_dictionary[4][0]+"              "+str(int(user_quantity[4]))+"                    "+laptop_dictionary[4][2]+"               "+str(sft_amt)))
        elif i==5:
            file.write(str("\n" +laptop_dictionary[5][0]+"        "+str(int(user_quantity[5]))+"                 "+laptop_dictionary[5][2]+"                 "+str(mac_amt)))
    file.write("\n\n----------------------------------------------------------------------------------------------------------------------------")
    file.write("\n\t\t\t            Your final amount with 13% VAT : "+str(int(final_price)))   
    file.write("\n------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n\t\t\t            Your "+str(dip)+"% discounted amount is: "+str(int(discount)))
    file.write("\n------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n\t\t\t            So the Grand Total is: $"+str(int(grand_total)))
    file.write("\n=====================================================================")
    file.close()
    print("\n")
    print("--------------------------------------------------------------------------------")
    print("Bill:")
    file=open(unique+"-sell"+name+".txt","r")
    print(file.read())
    file.close()
    return laptop_dictionary
