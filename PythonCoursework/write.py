import datetime
from read import *
from operation import *
def update_stock(lap):
    file = open("nirjal.txt","w")
    for values in lap.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()

def for_print(customer_name,customer_address, dateandtime, laptop_sold, total, vat, grand_total):
    
            print("\n")
            print("\t \t \t Py Store ")
            print("-----------------------------------------------------------------------------------------------------------------------------")
            print("\n")
            print("\t \t  Maitidevi,Kathmandu | Phone no: 9808438684")
            print("------------------------------------------------------------------------------------------------------------------------------")
            print("\n")
            print("-----------------------------------------------------")
            print("Purchase details: \n")
            print("Company's Name: "+ str(customer_name))
            print("Company Address: "+ str(customer_address))
            print("Date and time of purchase: "+ str(dateandtime))
            print("\n")
            print("---------------------")
            print("Product Details are: ")
            print("------------------------------------------------------------------------------------------------------------------------------")
            print("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
            print("------------------------------------------------------------------------------------------------------------------------------")
            for i in laptop_sold:
                print(i[0], "\t\t\t" ,i[1], "\t\t\t " ,i[2], "\t\t\t " ,"$", i[3] )
            print("------------------------------------------------------------------------------------------------------------------------------")
            print("Your total is : $"+str (total))
            print("Your vat amount is:"+str(vat))
            print("Grand Total with vat: $"+ str(grand_total))
            print("\n")    
         
def bill(customer_name,y,customer_address,dateandtime,laptop_sold,total,vat, grand_total):
        file= open(str(customer_name)+"_"+str(y)+".txt", "w")
        file.write("\n")
        file.write("----------------------------------------------------------")
        file.write("\t \t \Py Store")
        file.write("\n")
        file.write("----------------------------------------------------------")
        file.write("\t \t \t \Jamal,Kathamndu | Contact number: 9746868761")
        file.write("----------------------------------------------------------")
        file.write("\n" )
        file.write("Purchase Details are: ")
        file.write("-----------------------------------------------------")
        file.write("\nCustomer's Name: " + str(customer_name))
        file.write("\nCustomer address: " + str(customer_address))
        file.write("\nDate and time of purchase: " + str(dateandtime))
        file.write("\n" )
        file.write("\n")
        file.write("Product details: \n")
        file.write("\n------------------------------------------------------------------------------------------------------------------------\n" )
        file.write("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
        file.write("\n------------------------------------------------------------------------------------------------------------------------ \n" )


        for i in laptop_sold:
            file.write(str(i[0])+"\t\t\t "+str(i[1])+"\t\t\t\t\t\t "+str(i[2])+"\t\t\t\t\t\t\t"+"$"+str(i[3]) +"\n")


        file.write("-" )
        file.write("\nYour total is : $" + str(total))
        file.write("Your vat amount is:"+str(vat))
        file.write("\nGrand Total with Vat: $" + str(grand_total))
        file.write("\n")
        file.close()
            
def prints(customer_name,customer_address, dt, laptop_sold, total, shipping_cost, grand_total):
        print("\n")
        print("\t \t \Py Store")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        print("\t \t \t \Jamal,Kathamndu | Contact number: 9746868761")
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        print("-----------------------------------------------------")
        print("Purchase details: \n")
        print("Customer's Name: "+ str(customer_name))
        print("Customer Address: "+ str(customer_address))
        print("Date and time of purchase: "+ str(dt))
        print("\n")
        print("---------------------")
        print("Product Details are: ")
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
        print("------------------------------------------------------------------------------------------------------------------------------")
        for i in laptop_sold:
            print(i[0], "\t\t\t" ,i[1], "\t\t\t " ,i[2], "\t\t\t " ,"$", i[3] )
        print("-")
        print("Your total is : $"+str (total))
        print("Your Shipping charge is : $", shipping_cost)
        print("Grand Total : $"+ str(grand_total))
        print("\n")

def bills(customer_name,customer_address,y, dateandtime, laptop_sold, total, shipping_cost, grand_total):
        file= open(str(customer_name)+ str(y)+ "nirjal.txt", "w")
        file.write("----------------------------------------------------------")
        file.write("\t \t \Py Store ")
        file.write("\n")
        file.write("----------------------------------------------------------")
        file.write("\t \t \t \Jamal,Kathamndu | Contact number: 9746868761")
        file.write("----------------------------------------------------------")
        file.write("\n" )
        file.write("Purchase Details are: ")
        file.write("Customer's Name: "+ str(customer_name))
        file.write("Customer address: "+ str(customer_address))
        file.write("\nDate and time of purchase: " + str(dateandtime))
        file.write("\n" )
        file.write("---------------------")
        file.write("Product Details are: ")
        file.write("\n------------------------------------------------------------------------------------------------------------------------\n" )
        file.write("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
        file.write("\n------------------------------------------------------------------------------------------------------------------------ \n" )


        for i in laptop_sold:
            file.write(str(i[0])+"\t\t\t "+str(i[1])+"\t\t\t\t\t\t "+str(i[2])+"\t\t\t\t\t\t\t"+"$"+str(i[3]) +"\n")


        file.write("-" )
        file.write("\nYour total is : $" + str(total))
        file.write("\nYour Shipping charge is : $ " +""+ str(shipping_cost) +"\n")
        file.write("\nGrand Total : $" + str(grand_total))
        file.write("\n")
        file.close()
