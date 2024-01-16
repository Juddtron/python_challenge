import csv


file_to_load = "budget_data.csv"
file_to_output = "analysis/budget_analysis.txt"



total_months = 0
prev_profit = 0
month_of_change = []
Profit_Loss_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
net_total_profit = 0
Profit_Loss_change = 0


with open(file_to_load) as Profit_Losses_data:
    reader = csv.DictReader(Profit_Losses_data)

    for row in reader:

        total_months = total_months + 1
        net_total_profit = int(net_total_profit) + int(["Profit/Losses"])

        Profit_Loss_change = int(row["Profit/Losses"]) - prev_profit
        prev_Profit_Losses = int(row["Profit/Losses"])
        Profit_Loss_change_list += [Profit_Loss_change]
        month_of_change = month_of_change + [row["Date"]]

        if (Profit_Loss_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = Profit_Loss_change

        if (Profit_Loss_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = Profit_Loss_change

    profit_loss_avg = sum(Profit_Loss_change_list) / len(Profit_Loss_change_list)

    results = (
        f"\Financial Analysis\n"
        f"Total Months: {total_months}\n"
        f"Net Total Profit: ${net_total_profit}\n"
        f"Average Change in Profit: ${profit_loss_avg}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

    print(results)

