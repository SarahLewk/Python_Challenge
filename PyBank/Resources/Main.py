import os
import csv

csvpath = os.path.join('..',"Resources","budget_data.csv")


with open(csvpath, newline="") as csvfile:
    csvreader=csv.DictReader(csvfile)
    
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
    Profit_Losses = ['Profit','Losses']
    Loss_Count = []
    
    for i in Month_list:
        if i not in unique_month_counter:
             unique_month_counter.append(i)
             unique_month_counter=len(unique_month_counter)

        print("Total Months: ", int(totalMonths))
# When I run this I get: "Total Months: 1" it appears it is only reading one value in the first cell and not reading the whole column.


#My attempt at #2: ......(Net Total of Profit/Losses)        
#got error when trying to use float
netprofit=0

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile)
    

    for row in csvreader:
        netprofit += int(row[1])
        print(netprofit)

        break
# (Error):     Traceback (most recent call last):
#              File "Main.py", line 21, in <module>
#              netprofit += int(row[1])
#              ValueError: invalid literal for int() with base 10: 'Profit/Losses'

#My attempt at #3:.......
#Avg pf change in Profit/Losses-Sum of column B sum()

#My attempt at #4:.......
#Greatest increase in profits use max() function

#My attempt at #5:.......
#Greatest decrease in profits use min() function