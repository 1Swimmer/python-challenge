# Modules			
import os
import csv

# Set path for file			
CSVBudget = os.path.join("..","Resources", "budget_data.csv")

#I dicd try sshort verion method but it did not work for me so I used full path
Totalmonths = 0
Nettotal = 0
Profit_losses = []
Average_changes = []
pl_change = []
Date = []
with open(CSVBudget) as csvfile:

    Budget = csv.reader(csvfile)
    next(Budget)

    for col in Budget:
        Totalmonths = Totalmonths +1
        Nettotal = Nettotal + int(col[1])
        Profit_losses.append(col[1])
        Date.append(col[0])
#  Average  Change			
			
		# N=2	
		# cumsum, moving_averages = [0], []	
		# x =2	
#		for  x in range(1,len(Profit_losses)):
#			pl_change.append(int(Profit_losses[x])-int(Profit_Losses[x-1]))	
			# cumsum.append(cumsum[i-1] + x)
			# if i>=N:
			
			
#		Total_Average_Change = sum(pl_change) / len(pl_change)
		#Print(" Average  Change:" + " "+ [{Total_Average_Change}:.2f])	
		#print (f'  Greatest Increase in Profits:  +  " "+ ("Months") + " " + ([max{moving_ave}:.2f)]')	
		#print (f'  Greatest Decrease in Profits:  + ("Months") + " " + ([min{moving_aves}:.2f)]')	
#		plgreatestincrase = max(pl_change)
#		Print(plgreatestincrease)
#		plgreaterdecrease = min(pl_change)
#		Print(plgreaterdecrease)
#		plgreatestincrease_date = Totalmonths[pl_change.index(plgreatestincrease)+1]
#		plgreatestdecrease_date = Totalmonths[pl_change.index(plgreatestdecrease)+1]
# Set variable for output file			
#output_file = os.path.join("..", ,"zpruebas","analysis","Financial_Analysis.txt)			
		
#  Open the output file			
#with open(output_file, "w") as textfile:			
#writer = txt.writer(textfile)		
		
# Write information			
#File_object.write("Financial Analysis")		
#File_object.write("----------------------------")		
#File_object.write(f'Total Months:  {[Total_Months]:.2f}')		
#File_object.write(f'Total: + " "+ {[Total]:.2f}')		
#File_object.write(" Average  Change:" + " "+ [{Total_Average_Change}:.2f])		
#File_object.write(f'  Greatest Increase in Profits:  +  " "+ ("Months") + " " + ([max{moving_ave}:.2f)]')		
#File_object.write(f'  Greatest Decrease in Profits:  + ("Months") + " " + ([min{moving_aves}:.2f)]')		
