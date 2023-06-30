import csv

total_monthly_changes = []
total = 0
date = []
previous_profit = 0
month = 0

with open('PyBank/Resources/budget_data.csv', 'r') as budget_date_csv:
    read_csv_file = csv.reader(budget_date_csv)
    header = next(read_csv_file)

    for row in read_csv_file:
        month += 1
        total += int(row[1])

        if month > 1:
            monthly_change = int(row[1]) - previous_profit
            total_monthly_changes.append(monthly_change)
            date.append(row[0])

        previous_profit = int(row[1])


avg_change = sum(total_monthly_changes) / len(total_monthly_changes)
greatest_increase_in_profits = max(total_monthly_changes)
greatest_decrease_in_profits = min(total_monthly_changes)
greatest_profit_increase_date = date[total_monthly_changes.index(greatest_increase_in_profits)]
greatest_profit_decrease_date = date[total_monthly_changes.index(greatest_decrease_in_profits)]


output = (
    "Financial Analysis\n"
    "-------------------------------------\n"
    f"Total Months: {month}\n"
    f"Total: ${total}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_profit_increase_date} (${greatest_increase_in_profits})\n"
    f"Greatest Decrease in Profits: {greatest_profit_decrease_date} (${greatest_decrease_in_profits})\n"
)


print(output)

with open('PyBank/analysis/output.txt', 'w') as output_file:
    output_file.write(output)