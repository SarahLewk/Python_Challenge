import os
import csv

csvpath = os.path.join('..',"Resources","budget_data.csv")

# Should I be using DictReader?
#with open(csvpath, newline="") as csvfile:
#csvreader=csv.DictReader(csvfile)


with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile)
    
#My attempts at #1.......

#1st attempt:
       for i in csvreader:
           Months = i['Date']
           print(set(Months))
           break    
# When I run this I just get the actual date in the first cell populating.
    
#My 2nd attempt:
    Month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    unique_month_counter = []
    #Profit_Losses = ['Profit','Losses']
    #Loss_Count = []
    
    for i in Month_list:
        if i not in unique_month_counter:
            unique_month_counter.append(i)
            unique_month_counter2=len(unique_month_counter)
            print("Total Months: ",int(unique_month_counter2))         
        break
# I feel like I'm so close but when I run this I get: "Total Months: 1" it appears it is only reading one value in the first cell and not reading the whole column.


#My attempt at #2: ......(Net Total of Profit/Losses)       
#got error when trying to use float
netprofit=0   

    for row in csvreader:
        netprofit += int(row[1])
        print(netprofit)

        break
# (No sure what error means):  Traceback (most recent call last):
#                              netprofit += int(row[1])
#                              ValueError: invalid literal for int() with base 10: 'Profit/Losses'

#3:.......
#Use a for loop to calculate the average change looping through each month


#4:.......
#Greatest increase in profits use max() function

#5:.......
#Greatest decrease in profits use min() function