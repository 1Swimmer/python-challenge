<<<<<<< HEAD
#Modules
import os
import csv

#Set path for file
csvbudget = os.path.join("..","PyBank","Resources","budget_data.csv")

#print header
print("Financial Analysis")
print("----------------------------")

#List to store data
totalmonths = 0
totalbudget = 0
profitloss = []
averagechanges = []
plchange = []
date = []

with open(csvbudget) as csvfile:
    Budget = csv.reader(csvfile)

#read the header row first    
    header = next(Budget)
# print(header)

    for row in Budget:

#Total Months
        totalmonths = totalmonths + 1

        totalbudget = totalbudget + int(row[1])
        profitloss.append(row[1])
        date.append(row[0])
    print(f"Total Months:{totalmonths}")
    print(f"Total : ${totalbudget}")


    for x in range(1,len(profitloss)):
        plchange.append(int(profitloss[x])-int(profitloss[x-1]))


    total_average_change = sum(plchange)/ len(plchange)
    print(f"Average Change: ${total_average_change:.2f}")

    plgreatestincrease = max(plchange)
    plgreatestdecrease = min(plchange)
    plgreatestincrease_date = date[plchange.index(plgreatestincrease)+1]
    plgreatestdecrease_date = date[plchange.index(plgreatestdecrease)+1]

    print(f"Greatest Increase in Profits: {plgreatestincrease_date} ({plgreatestincrease:.0f})")
    print(f" Greatest Decrease in Profits: {plgreatestdecrease_date} ({plgreatestdecrease:.0f})")
    
# Set Variables for output file
output_file = os.path.join("..","PyBank","Analysis","Financial_Analysis.txt")

#open the output file
file = open(output_file, "w")


# Write information			
file.write(f"Financial Analysis\n")		
file.write(f"----------------------------\n")
file.write(f"Total Months:{totalmonths}\n")
file.write(f"Total : ${totalbudget}\n")
file.write(f"Average Change: ${total_average_change:.2f}\n")
file.write(f"Greatest Increase in Profits: {plgreatestincrease_date} ({plgreatestincrease:.0f})\n")
file.write(f"Greatest Decrease in Profits: {plgreatestdecrease_date} ({plgreatestdecrease:.0f})\n")
=======
#Modules
import os
import csv

#Set path for file
csvbudget = os.path.join("..","PyBank","Resources","budget_data.csv")

#print header
print("Financial Analysis")
print("----------------------------")

#List to store data
totalmonths = 0
totalbudget = 0
profitloss = []
averagechanges = []
plchange = []
date = []

with open(csvbudget) as csvfile:
    Budget = csv.reader(csvfile)

#read the header row first    
    header = next(Budget)
    # print(header)

    for row in Budget:

#Total Months
        totalmonths = totalmonths + 1

        totalbudget = totalbudget + int(row[1])
        profitloss.append(row[1])
        date.append(row[0])
    print(f"Total Months:{totalmonths}")
    print(f"Total : ${totalbudget}")


    for x in range(1,len(profitloss)):
        plchange.append(int(profitloss[x])-int(profitloss[x-1]))


    total_average_change = sum(plchange)/ len(plchange)
    print(f"Average Change: ${total_average_change:.2f}")

    plgreatestincrease = max(plchange)
    plgreatestdecrease = min(plchange)
    plgreatestincrease_date = date[plchange.index(plgreatestincrease)+1]
    plgreatestdecrease_date = date[plchange.index(plgreatestdecrease)+1]

    print(f"Greatest Increase in Profits: {plgreatestincrease_date} ({plgreatestincrease:.0f})")
    print(f"Greatest Decrease in Profits: {plgreatestdecrease_date} ({plgreatestdecrease:.0f})")
    
# Set Variables for output file
output_file = os.path.join("..","PyBank","Analysis","Financial_Analysis.txt")

#open the output file
file= open(output_file, "w")

# Write information			
file.write(f'Financial Analysis\n')		
file.write(f'----------------------------\n')
file.write(f'Total Months:{totalmonths}\n')
file.write(f'Total : ${totalbudget}\n')
file.write(f'Average Change: ${total_average_change:.2f}\n')
file.write(f'Greatest Increase in Profits: {plgreatestincrease_date} ({plgreatestincrease:.0f})\n')
file.write(f'Greatest Decrease in Profits: {plgreatestdecrease_date} ({plgreatestdecrease:.0f})\n')
>>>>>>> 2c82aa6b23580147dfc54bf7acb658e29491ba46
