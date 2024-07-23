import datetime
from read import *
from write import *
def stock_display():
    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("S.N.             Laptop Name          Company Name        price         Quantity           Processor            Graphics" )
    print("-------------------------------------------------------------------------------------------------------------------------")
    file = open("nirjal.txt", "r")
    a = 0
    for line in file:
        print(a+1, "\t\t" + line.replace(",", "\t\t"))
        a = a + 1
        if(a ==5):
            break
    file.close()

#this works
def serial_validation(l_d):  
    loop = True
    while loop==True:
        try:
            sn = int(input("Enter the serial number of the laptop: "))
            print("\n")
            while sn <= 0 or sn > len(l_d):
                print("\n")
                print("-------------------------------------")
                print("Provide a valid serial number !!!")
                print("-------------------------------------")
                print("\n")
                sn = int(input("Enter the serial number of the laptop: "))
                print("\n")
            loop = False
        except :
            print("please provide proper integer value!")
    return sn

def quantity_validations_sell(l_d,sn):
    loop =True      
    while loop==True:
            try:
                quantity = int(input("Enter the quantity you want to sell: "))
                laptop_list = l_d[sn][3]
                while quantity <= 0 or quantity > int(laptop_list):
                    print("we don't have the quantity you are looking at admin")
                    print("\n")
                    quantity = int(input("Enter the quantity you want to sell: "))
                    print("\n")
                    print("\n")
                loop = False

            except :
                print("please provide proper integer value!")
    return quantity

def quantity_validations_buy():
    loop =True      
    while loop==True:
            try:
                quantity = int(input("Enter the quantity you want to buy: "))
                while quantity <= 0:
                    print("we don't have the quantity you are looking at admin")
                    print("\n")
                    quantity = int(input("Enter the quantity you want to buy: "))
                    print("\n")
                    print("\n")
                loop = False

            except :
                print("please provide proper integer value!")
    return quantity