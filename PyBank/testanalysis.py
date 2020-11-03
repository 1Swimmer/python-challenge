# Modules			
import os			
import csv			
			
# Set path for file			
CSVBudget = os.path.join("Resources", "budget_data.csv")			
			
# Lists to store data			
Date = []			
Profit&Losses = []			
			
# Open the CSV			
with open(CSVBudget) as csvfile:			
			
# Read the header row first 			
	csv_header = next(csvreader)		
	print(f"CSV Header: {csv_header}")		
			
# CSV reader specifies delimiter and variable that holds contents			
	csvreader = csv.reader(csvfile, delimiter=",")		
	for row in csvreader:		
			
#Print header			
	Print("Financial Analysis")		
	Print("----------------------------")		
			
#Total Months			
		Months = str(row[0])	
		Total_Months.append(Months)	
		print (f'Total Months:  {[Total_Months]:.2f}')	
			
#Total			
		Total_Budget= int(row[1])	
		Total.append(Total_Budget)	
		print (f'Total: + " "+ {[Total]:.2f}')	
			
			
#  Average  Change			
			
		N=2	
		cumsum, moving_averages = [0], []	
			
		for i, x in enumerate(Total_Budget, 1):	
			cumsum.append(cumsum[i-1] + x)
			if i>=N:
			
			
		Total_Average_Change = moving_averages / len	
		Print(" Average  Change:" + " "+ [{Total_Average_Change}:.2f])	
		print (f'  Greatest Increase in Profits:  +  " "+ ("Months") + " " + ([max{moving_ave}:.2f)]')	
		print (f'  Greatest Decrease in Profits:  + ("Months") + " " + ([min{moving_aves}:.2f)]')	
			
# Set variable for output file			
output_file = os.path.join("..", ,"zpruebas","analysis","Financial_Analysis.txt)			
			
#  Open the output file			
with open(output_file, "w") as textfile:			
	writer = txt.writer(textfile)		
			
# Write information			
	File_object.write("Financial Analysis")		
	File_object.write("----------------------------")		
	File_object.write(f'Total Months:  {[Total_Months]:.2f}')		
	File_object.write(f'Total: + " "+ {[Total]:.2f}')		
	File_object.write(" Average  Change:" + " "+ [{Total_Average_Change}:.2f])		
	File_object.write(f'  Greatest Increase in Profits:  +  " "+ ("Months") + " " + ([max{moving_ave}:.2f)]')		
	File_object.write(f'  Greatest Decrease in Profits:  + ("Months") + " " + ([min{moving_aves}:.2f)]')		
