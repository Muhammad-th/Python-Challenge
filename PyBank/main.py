# Importing and reading files
import os
import csv
from pathlib import Path 

# file location
file = Path("Resources", "budget_data.csv")

# Looping through rowa
monthtotal = []
profittotal = []
profitchange = []
 
with open(file,newline="", encoding="utf-8") as budget:

    csvR = csv.reader(budget,delimiter=",") 

    header = next(csvR)  

    # Looping through the rowa in the file
    for row in csvR: 

        # Appending the total months and total profit
        monthtotal.append(row[0])
        profittotal.append(int(row[1]))

    # Looping through the profits 
    for i in range(len(profittotal)-1):
        
        profitchange.append(profittotal[i+1]-profittotal[i])
        
# attaining the max and min from the changes
maximum = max(profitchange)
minimum = min(profitchange)

maxIncrease = profitchange.index(max(profitchange)) + 1
minDecrease = profitchange.index(min(profitchange)) + 1 

# Print  and export text file

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(monthtotal)}")
print(f"Total: ${sum(profittotal)}")
print(f"Average Change: {round(sum(profitchange)/len(profitchange),2)}")
print(f"Greatest Increase in Profits: {monthtotal[maxIncrease]} (${(str(maximum))})")
print(f"Greatest Decrease in Profits: {monthtotal[minDecrease]} (${(str(minimum))})")

Export = Path("Analysis", "PyBank_Results.txt")

with open(Export,"w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(monthtotal)}")
    file.write("\n")
    file.write(f"Total: ${sum(profittotal)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(profitchange)/len(profitchange),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {monthtotal[maxIncrease]} (${(str(maximum))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {monthtotal[minDecrease]} (${(str(minimum))})")