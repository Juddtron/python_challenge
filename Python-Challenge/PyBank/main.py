import csv

# Files to load and output (Remember to change these)
file_to_load = "PyBank/Resourrces/budget_data.csv"
file_to_output = "analysis/budget_analysis.txt"

# Track various revenue parameters
total_months = 0
prev_profit = 0
month_of_change = []
profit_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_profit = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as profit_loss_data:
    reader = csv.DictReader(profit_loss_data)

    for row in reader:


        total_months = total_months + 1
        total_profit = total_profit + int(row["Profit/Losses"])

        profit_loss_change = int(row["Profit/Losses"]) - prev_profit
        prev_profit = int(row["Profit/Losses"])
        profit_change_list = profit_change_list + [profit_loss_change]
        month_of_change = month_of_change + [row["Date"]]

        if (profit_loss_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = profit_loss_change

        if (profit_loss_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = profit_loss_change

profit_loss_avg = sum(profit_change_list) / len(profit_change_list)


results = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profit: ${total_profit}\n"
    f"Average Profit Loss Change: ${profit_loss_avg}\n"
    f"Greatest Increase in Profit: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profit: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(results)

output = open("output1.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_profit)}")
line5 = str(f"Average Change: ${str(round(profit_loss_avg,2))}")
line6 = str(f"Greatest Increase in Profits: {row} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {row} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))