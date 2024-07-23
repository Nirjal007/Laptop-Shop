from operation import stock_display
from write import *
from operation import *
def welcome(): #defining welcome function
    print("-----------------------------------------------------------------------------")
    print("\t \t Welcome, Admin! How can I help you?")
    print("-----------------------------------------------------------------------------\n")
  
def welcome1():
    print("\t\t Here is the list of stock available in our inventory!!!\t\t\t")
    print("-----------------------------------------------------------------------------\n")
    
def dict():
    file = open("nirjal.txt", "r")
    l_d = {}
    list_id = 1
    for line in file:
        line = line.replace("\n", "")
        l_d.update({list_id: line.split(",")})
        list_id = list_id + 1
    file.close()
    return l_d
    
def adding_laptop_tostock():
    print("\n")
    print("--------------------------------------")
    print("The Laptop has been added to the stock")
    print("--------------------------------------")
    print("\n")

#the given below function is called when user press 2
def purchasing_laptop():
    print("\n")
    print("-----------------------------------")
    print("Thank you for purchasing the laptop")
    print("-----------------------------------")
    print("\n")    

#the given below function is called when the user gives invalid input
def invalid_user_input():
    print("\n")
    print("------------------------------------")
    print("invalid input!!!")
    print("Please provide value as 1,2 or 3.")
    print("------------------------------------")
    print("\n")

#the given below function is called when user press 3
def exit_system():
    print("\n")
    print("------------------------------------")
    print("Thank you for using our system")
    print("------------------------------------")
    print("\n")

def ask_user_for_option():
    print("+++++++++++++++++++++++++++++++++++++")
    print("Enter 1 to purchase:   ")
    print("Enter 2 to sell:  ")
    print("Enter 3 to exit:       ")
    print("+++++++++++++++++++++++++++++++++++++")
    print("\n")
            
#calling function to execute while running
welcome()
welcome1()
stock_display()