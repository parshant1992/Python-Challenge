import os
import csv
path = r"C:\Users\pm300\Downloads\Starter_Code (6)\Starter_Code\PyBank"
os.chdir(path)
budget_csv = os.path.join("Resources", "budget_data.csv")
def calculate_average(numbers):
 return sum(numbers) / len(numbers)
# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip header row

    # Iterate through each row
    for row in csvreader:
        # Count total months
        total_months += 1

        # Calculate net total
        profit_loss = int(row[1])
        
        net_total += profit_loss

        # Calculate change and add to the changes list
        if total_months == 1:
            previous_profit_loss = profit_loss
        else:
            change = profit_loss - previous_profit_loss
            previous_profit_loss = int(row[1])
            changes.append(change)

        # Update greatest increase and decrease if applicable
        if change > greatest_increase[1]:
            greatest_increase = [row[0], change]
        if change < greatest_decrease[1]:
            greatest_decrease = [row[0], change]

        previous_profit_loss = profit_loss

# Calculate the average change
average_change = calculate_average(changes)

# Print the results
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write the results to a text file
filepath = os.path.join('Resources', 'PyBank_Results.txt')
with open(filepath, 'w') as txtfile:
    print("Financial Analysis",file = txtfile )
    print("---------------------------")
    print(f"Total Months: {total_months}",file = txtfile )
    print(f"Net Total: ${net_total}",file = txtfile )
    print(f"Average Change: ${average_change:.2f}",file = txtfile )
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})",file = txtfile )
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})",file = txtfile )
