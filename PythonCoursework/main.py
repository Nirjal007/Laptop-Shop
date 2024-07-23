from datetime import datetime
from read import *
from write import *
from operation import *

l_d=dict()
loop = True
while loop == True:
      try:
          
          ask_user_for_option()
          user_input = int(input("Enter the option to continue: "))
      except:
            print("Provide a integer value")      
      if user_input == 1:
            
            cus_name = input("Enter your company name: ")
            cus_address=input("Enter your address:")
            laptop_sold=[]
            need_more = True
            while need_more == True:
                  stock_display() 
                  sn = serial_validation(l_d)
                  quantity = quantity_validations_buy()
                  adding_laptop_tostock()
                  
                  l_d[sn][3] = int(l_d[sn][3]) + int(quantity)
                  
                  update_stock(l_d)
                  lap_name = l_d[sn][0]
                  lap_quantity = quantity
                  lap_price = l_d[sn][2]
                  Selected_Quantity_Price = l_d[sn][2].replace("$", '')
                  total_price = int(Selected_Quantity_Price) * int(quantity)
                  Graphics_card = l_d[sn][5]
        
                  laptop_sold.append([lap_name, lap_quantity, lap_price, total_price, Graphics_card])
                  ans = input("Do you want to continue (Y/N)?").upper()
                  print("\n")
                  
                  if ans == "Y":
                        need_more = True
                  else:
                        total = 0
                        
                        
                        for i in laptop_sold:
                              total += int(i[3])
                              
                        vat=total *13/100      
                        grand_total = total + vat

                        dt = datetime.datetime.now()
                        x = str(dt).split(" ")
                        s = "_".join(x)
                        y = s.replace(":","_")
                        for_print(cus_name,cus_address, dt, laptop_sold, total, vat, grand_total)  
                        bill(cus_name,cus_address,y, dt, laptop_sold, total, vat, grand_total) 
                        break   

         
      elif user_input == 2:
            
            cus_name = input("Enter the customer name: ")
            cus_address=input("Enter customer address:")
            laptop_sold=[]
            need_more = True
            while need_more == True:
                  stock_display()   
                  sn = serial_validation(l_d)
                  quantity = quantity_validations_sell(l_d,sn)
                  
                  l_d[sn][3] = int(l_d[sn][3]) - int(quantity)
                  
                  update_stock(l_d)
                  lap_name = l_d[sn][0]
                  lap_quantity = quantity
                  lap_price = l_d[sn][2]
                  Selected_Quantity_Price = l_d[sn][2].replace("$", '')
                  total_price = int(Selected_Quantity_Price) * int(quantity)
                  Graphics_card = l_d[sn][5]
        
                  laptop_sold.append([lap_name, lap_quantity, lap_price, total_price, Graphics_card])
                  ans = input("Do you want to continue (Y/N)?").upper()
                  print("\n")
                  
                  if ans == "Y":
                        need_more = True
                  else:
                        total = 0
                        shipping_charge = 100
                        
                        for i in laptop_sold:
                              total += int(i[3])
                              
                        grand_total = total + shipping_charge

                        dt = datetime.datetime.now()
                        x = str(dt).split(" ")
                        s = "_".join(x)
                        y = s.replace(":","_")
                        prints(cus_name,cus_address, dt, laptop_sold, total, shipping_charge, grand_total)  
                        bills(cus_name,cus_address,y, dt, laptop_sold, total, shipping_charge, grand_total) 
                        break   

            
            
      elif user_input == 3:
            exit_system()
            loop = False
      else:
            invalid_user_input()