import os
import csv

#csvpath = os.path.join('..',"Resources","budget_data.csv")
reading_file = os.path.join('..',"Resources","budget_data.csv")
output_file =  "Analysis/budget_analysis_1.txt"

#My list of variables for my output:
month_list = 0
prev_profit_loss = 0
month_of_change = []
profit_loss_change_list = []
greatest_increase_profits = ["", 0]
greatest_decrease_loss = ["", 99999999999]
total_profit_loss = 0

# Chris told me he didn't know what DictReader was and told me no to use it...
# so I find it interesting that the solved video shows them using DictReader.
# I decided to incorporate it back into my code since I think it is a very useful tool.
with open(reading_file) as revenue_data:
    reader=csv.DictReader(revenue_data)

    prev_profit_loss = 0
    for row in reader:
        #Tracking my total months and net total amount of "Profit/Losses"
        month_list = month_list +1
        total_profit_loss = total_profit_loss + int(row["Profit/Losses"])
        #Tracking the "Profit/Losses" changes
        profit_loss_change = int(row["Profit/Losses"]) - prev_profit_loss
        prev_profit_loss = int(row["Profit/Losses"])
        profit_loss_change_list = profit_loss_change_list + [profit_loss_change]
        month_of_change = month_of_change + [row["Date"]]
        #Calculating the greatest increase in profits
        if (profit_loss_change > greatest_increase_profits[1]):
            greatest_increase_profits[0] = row["Date"]
            greatest_increase_profits[1] = profit_loss_change
        #Calculating the greatest decrease in losses
        if (profit_loss_change < greatest_decrease_loss[1]):
            greatest_decrease_loss[0] = row["Date"]
            greatest_decrease_loss[1] = profit_loss_change
        #Calculating the average profit/loss change
            profit_loss_avg = sum(profit_loss_change_list)/len(profit_loss_change_list)
            #I'm not getting the same number value as the answer in the homework example...
            #but everything else printed the same. Did I write my calculation wrong?
# Creating my output summary
Output= (
f"\nFinancial Analysis\n"
f"Total Months: {month_list}\n"
f"Total: ${total_profit_loss}\n"
f"Average Change: ${profit_loss_avg}\n"
f"Greatest Increase in Profits: {greatest_increase_profits[0]} (${greatest_increase_profits[1]})\n"
f"Greatest Decrease in Revenue: {greatest_decrease_loss[0]} (${greatest_decrease_loss[1]})\n"
)

#Printing my output
print(Output)

#Exporting my results to a text file
with open(output_file,"w") as txt_file:
    txt_file.write(Output)