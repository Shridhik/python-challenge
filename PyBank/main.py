import os
import csv

# Set path for the input CSV file
csvpath = os.path.join("Resources", "budget_data.csv")
#census_csv = os.path.join("..", "Resources", )


# Set path for the output text file
output_path = os.path.join("analysis", "financial_analysis.txt")

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

# Read the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)

    # Loop through the rows in the CSV file
    for row in csvreader:
        # Count the number of months
        total_months += 1

        # Calculate the net total of Profit/Losses
        net_total += int(row[1])

        # Calculate the change in Profit/Losses
        current_profit_loss = int(row[1])
        if previous_profit_loss != 0:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)

            # Check for the greatest increase and decrease in profits
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]
        
        previous_profit_loss = current_profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes)

# Generate the analysis report
analysis_report = f'''
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total:,}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,})
'''

# Create the 'analysis' folder if it doesn't exist
os.makedirs("analysis", exist_ok=True)

# Save the analysis report to a text file
with open(output_path, "w") as txtfile:
    txtfile.write(analysis_report)

# Print the analysis report
print(analysis_report)